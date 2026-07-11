#!/usr/bin/env python3
"""Validate the metagov-runbook docs: internal links, placeholders, address consistency.

Run from the repo root:  python3 scripts/verify.py
Exits non-zero if any check fails. Used by the update-runbook skill and CI.
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
md = [f for f in glob.glob("**/*.md", recursive=True)
      if not f.startswith("_facts/") and ".claude/" not in f]
fail = 0

# 1) Internal links resolve
link = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
broken = []
for f in md:
    base = os.path.dirname(f)
    for m in link.finditer(open(f, encoding='utf-8').read()):
        t = m.group(1).strip()
        if t.startswith(('http://', 'https://', '#', 'mailto:')):
            continue
        path = t.split('#')[0]
        if not path:
            continue
        tgt = os.path.normpath(os.path.join(base, path))
        if not (os.path.exists(tgt) or os.path.isdir(tgt)):
            broken.append((f, t))
if broken:
    fail += 1
    print(f"FAIL: {len(broken)} broken internal link(s):")
    for f, t in broken:
        print(f"  {f} -> {t}")
else:
    print("OK: internal links resolve")

# 2) No placeholders (keyword + unfilled <ANGLE-BRACKET> tokens like <DATE>, <ID>, <owner-1>)
ph = re.compile(r'\b(TODO|TBD|FIXME|XXX|lorem ipsum|PLACEHOLDER)\b', re.I)
# All-caps tokens (<DATE>, <ID>, <TX>), word-then-digit (<owner-1>), or <...>.
# Deliberately spares lowercase template notation like <name> / <their-ens>.
angle = re.compile(r'<[A-Z][A-Z0-9_]*>|<[a-z]+-\d+>|<\.\.\.>')
hits = [(f, n + 1) for f in md
        for n, ln in enumerate(open(f, encoding='utf-8'))
        if ph.search(ln) or angle.search(ln)]
if hits:
    fail += 1
    print(f"FAIL: {len(hits)} placeholder(s):")
    for f, n in hits:
        print(f"  {f}:{n}")
else:
    print("OK: no placeholders")

# 3) Every 20-byte contract address outside addresses.md must appear in it
addr_file = "02-contracts-and-multisigs/addresses.md"
canon = set(a.lower() for a in re.findall(
    r'0x[a-fA-F0-9]{40}(?![a-fA-F0-9])', open(addr_file).read()))
stray = []
for f in md:
    if f == addr_file:
        continue
    for m in re.finditer(r'0x[a-fA-F0-9]+', open(f, encoding='utf-8').read()):
        h = m.group(0)
        if len(h) == 42 and h.lower() not in canon:  # exactly address length, not a 64-hex id
            stray.append((f, h))
if stray:
    fail += 1
    print(f"FAIL: {len(stray)} contract address(es) not in {addr_file}:")
    for f, h in sorted(set(stray)):
        print(f"  {f}: {h}")
else:
    print(f"OK: all contract addresses are in {addr_file}")

print("PASS" if not fail else f"\n{fail} check(s) FAILED")
sys.exit(1 if fail else 0)
