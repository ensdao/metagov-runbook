#!/usr/bin/env python3
"""Check whether the runbook's stated facts are still TRUE.

Companion to verify.py, which checks whether the docs are well-FORMED. The two
are deliberately separate: verify.py is deterministic, offline, and gates every
PR; this one makes network calls and runs on a schedule, so a flaky endpoint
never blocks a contributor.

Checks:
  A (fatal)       every "Safe, N/M" threshold in addresses.md matches the chain
  B (reported)    age of every "as of YYYY-MM-DD" stamp

Run from the repo root:  python3 scripts/check_currency.py
"""
import os, re, sys, glob, json, datetime, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

ADDR_FILE = "02-contracts-and-multisigs/addresses.md"
SAFE_API = "https://api.safe.global/tx-service/eth/api/v1/safes/{}/"
STAMP_MAX_AGE_DAYS = 120
fail = 0


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "metagov-runbook-currency-check"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


# --- A) stated Safe thresholds vs the chain -------------------------------
# Rows look like: | Name | ens | `0x…` | Safe, 2/4 | source |
row = re.compile(r"`(0x[a-fA-F0-9]{40})`.*?Safe,\s*(\d+)\s*/\s*(\d+)")
claims = []
for line in open(ADDR_FILE, encoding="utf-8"):
    m = row.search(line)
    if m:
        claims.append((m.group(1), int(m.group(2)), int(m.group(3)), line.split("|")[1].strip()))

print(f"Checking {len(claims)} stated Safe configuration(s) against the chain\n")
for addr, want_thr, want_own, name in claims:
    try:
        d = get(SAFE_API.format(addr))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"  SKIP  {name}: Safe API unreachable ({e})")
        continue
    thr, own = int(d["threshold"]), len(d["owners"])
    if (thr, own) == (want_thr, want_own):
        print(f"  OK    {name}: {thr}/{own}")
    else:
        fail += 1
        print(f"  FAIL  {name} ({addr})")
        print(f"        docs say {want_thr}/{want_own}, chain says {thr}/{own}")
        print(f"        owners: {', '.join(d['owners'])}")

# --- B) age of "as of" stamps --------------------------------------------
# changelog.md is excluded: its dates record when a revision happened, which is
# history, not a freshness claim that can go stale.
SKIP = {"reference/changelog.md"}
md = [f for f in glob.glob("**/*.md", recursive=True)
      if not f.startswith("_facts/") and ".claude/" not in f
      and f.replace(os.sep, "/") not in SKIP]
stamp = re.compile(r"as of (\d{4})-(\d{2})-(\d{2})", re.I)
today = datetime.date.today()
stamps = []
for f in md:
    for n, ln in enumerate(open(f, encoding="utf-8"), 1):
        m = stamp.search(ln)
        if m:
            d = datetime.date(*map(int, m.groups()))
            stamps.append(((today - d).days, f, n, d))

print(f"\n{len(stamps)} dated claim(s), oldest first:")
for age, f, n, d in sorted(stamps, reverse=True):
    flag = "  <-- re-verify" if age > STAMP_MAX_AGE_DAYS else ""
    print(f"  {age:>4}d  {d}  {f}:{n}{flag}")
stale = [s for s in stamps if s[0] > STAMP_MAX_AGE_DAYS]
if stale:
    print(f"\n{len(stale)} stamp(s) older than {STAMP_MAX_AGE_DAYS} days. Not a failure: "
          "re-verify against the source, then update the date. Never bump a date "
          "without re-checking the underlying fact.")

print("\nPASS" if not fail else f"\n{fail} check(s) FAILED")
sys.exit(1 if fail else 0)
