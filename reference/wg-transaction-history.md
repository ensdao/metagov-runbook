# Working-Group Transaction History (SafeNotes archive)

The transaction-level ledger of every ENS Working Group Safe from July 2022 to July 2026, annotated with a category and purpose from 2024-01-01 onward. It is the answer to "what did WG _N_ pay for, when, and from which Safe" without re-deriving history from raw Etherscan/Safe logs. It is a **historical record**: for anything you are about to sign, verify on-chain against [addresses.md](../02-contracts-and-multisigs/addresses.md) and follow [verification & safety](../04-runbook/verification-and-safety.md).

## Provenance

- **What SafeNotes was.** A public annotation layer over the WG Safes: "SafeNotes lets teams annotate their multisig transactions with descriptions and categories", announced 2025-02-13 ([Introducing SafeNotes](https://discuss.ens.domains/t/introducing-safenotes-a-new-standard-for-dao-spending-transparency/20245)). It was built, maintained and hand-annotated by the then-DAO Secretary, limes.eth (forum handle dylanb) ([shutdown post](https://discuss.ens.domains/t/safenotes-shutting-down/22398); ["I have hand categorized and described every one of the…"](https://discuss.ens.domains/t/21616)). Its annotations fed the quarterly [ENS Working Group Spending Summaries](https://discuss.ens.domains/t/ens-working-group-spending-summaries/20706) (cash-basis, per WG, H2 2022 → Q1 2026).
- **Shutdown.** On 2026-09-01 dylanb announced that safenotes.xyz "will be going dark soon", citing "Meta-Governance deciding not to continue supporting its use", and published the data so "the record remains available" ([SafeNotes Shutting Down](https://discuss.ens.domains/t/safenotes-shutting-down/22398)). No replacement annotation practice is documented → [OPEN-QUESTIONS Q-30](../OPEN-QUESTIONS.md).
- **The archive.** [github.com/gofordylan/ens-wg-transactions](https://github.com/gofordylan/ens-wg-transactions): one file, [`ens_wg_transactions.csv`](https://github.com/gofordylan/ens-wg-transactions/blob/main/ens_wg_transactions.csv). This page was written against commit [`b2a495a`](https://github.com/gofordylan/ens-wg-transactions/commit/b2a495aec740b3c594ab738fcaada01e037069fc) (2026-09-01); file SHA-256 `524302e617805ed9c591f1cb06c295d368501e44d3301d1a9f86271909340959`. Re-check the hash if the repo is updated.

## What the file contains

Per the [repo README](https://github.com/gofordylan/ens-wg-transactions#readme): 1,056 transactions across 8 Safes, July 2022 → July 2026, annotated from 2024-01-01; rows before 2024 carry `Category = None`; `Internal Transfer` rows are movements between WG Safes, not spend. Checked against the file (2026-09-01): first row 2022-07-02, last row 2026-07-11; no annotated row is dated before 2024-01-01; 21 rows from 2024 onward are unannotated (mostly spam-token and dust inflows, plus a block of Meta-Gov rows dated 27–30 Nov 2024).

| Column | Format | Notes |
|---|---|---|
| `Date` | `Mon D, YYYY` (e.g. `Jul 11, 2026`) | Can differ by a day from the UTC execution date (a `Jan 3, 2026` row executed [2026-01-04 UTC](https://etherscan.io/tx/0xa1d221d41690a6662bc0bec10e1bb27b17eaff0e3c325b361e8b5d0998864ede)). |
| `Safe` | checksummed address | One of the 8 Safes below. |
| `Amount` | signed, thousands separators, token symbol (`-18,000 USDC`, `+5.0 ETH`) | Negative = outflow. **Rounded display values**, not exact on-chain amounts (`-37,145 ENS` for 37,144.633483 ENS on-chain, [term 6](../05-terms/term-06.md#activity)). |
| `To/From` | counterparty address | Recipient for outflows, sender for inflows. |
| `Category` | one of 12 labels or `None` | See below. |
| `Description` | free text, `-` when empty | Often carries a forum link to the governing grant / proposal. |

**Categories** (rows): Services 296 · None 287 · Grants 148 · Hackathons 85 · Events 59 · Internal Transfer 57 · Governance Distribution 37 · Misc 24 · DAO Tooling 23 · Swap 23 · WG Wind Down 9 · Bounty 6 · Audit Support 2. `Swap` = ETH↔USDC conversions; `Governance Distribution` = ENS-token grants and steward vesting (Hedgey); `WG Wind Down` = return of funds to the Timelock at the Term 6 close-out. Tokens seen: USDC (826 rows), ETH (138), ENS (66), plus SAFE/WETH/DAI/LINK and spam tokens (SAITABIT, ZIK, HEX).

## Safes covered

`Safe` values in the file, mapped to their ENS names (reverse records resolved 2026-09-01; the same eight are labelled in the [SEAL Safe Harbor executable](https://discuss.ens.domains/t/executable-adopt-the-seal-safe-harbor-agreement/21226)). Full addresses, owners and thresholds live in [addresses.md](../02-contracts-and-multisigs/addresses.md) and [multisigs.md](../02-contracts-and-multisigs/multisigs.md).

| `Safe` (truncated) | ENS name | Role | Rows | Rows dated | Annotated | Status _(2026-09-01)_ |
|---|---|---|---|---|---|---|
| `0x91c3…d39b` | `main.mg.wg.ens.eth` | Meta-Gov main | 297 | 2023-02-13 → 2026-07-11 | 266 | active |
| `0x2686…5d03` | `main.eco.wg.ens.eth` | Ecosystem main | 253 | 2022-08-17 → 2026-06-30 | 190 | wound down 2026-06-30 |
| `0xcD42…D87d` | `main.pg.wg.ens.eth` | Public Goods main | 189 | 2023-03-30 → 2026-07-02 | 105 | wound down 2026-07-02 |
| `0x9B9c…966D` | `hackathons.eco.wg.ens.eth` | Ecosystem hackathon sponsorships | 133 | 2022-08-22 → 2026-06-25 | 87 | wound down 2026-06-25 |
| `0x5360…1819` | `irl.eco.wg.ens.eth` | Ecosystem IRL events | 104 | 2022-07-02 → 2026-06-30 | 49 | wound down 2026-06-30 |
| `0x13aE…6ea2` | `newsletter.eco.wg.ens.eth` | Ecosystem newsletter | 42 | 2023-07-26 → 2026-04-29 | 35 | dormant, near-zero balance |
| `0xebA7…6F62` | `largegrants.pg.wg.ens.eth` | Public Goods large grants | 33 | 2024-06-14 → 2025-03-28 | 32 | dormant, near-zero balance |
| `0xB162…31D1` | `stream.mg.wg.ens.eth` | SPP stream Safe | 5 | 2024-02-06 → 2024-02-07 | 5 | active (dormant) |

"Wound down" = the Safe's `WG Wind Down` rows returning funds to the Timelock, corroborated for Ecosystem by the [close-out post](https://discuss.ens.domains/t/ens-ecosystem-working-group-close-out-final-term/22227). Balances per the [Safe Transaction Service](https://api.safe.global/tx-service/eth/api/v1/safes/0x13aEe52C1C688d3554a15556c5353cb0c3696ea2/balances/?trusted=true).

## Known gaps and caveats

- **Pre-2024 rows are unannotated** by design (Terms 2–4 have amounts and counterparties only).
- **Not complete even after 2024.** Verified omissions on the Meta-Gov Safe: the [2026-03-25 batch](https://etherscan.io/tx/0xdc3b69a1289f9eae33b8dd282004927c86a9d6610483204b2e9c5ac8a6374926) (50,000 USDC EP 6.30 milestone + 8,500 USDC; the file has **no** Meta-Gov row dated March 2026) and the [2026-05-01 compensation batch](https://etherscan.io/tx/0x2a5934624d75cfd0a131a6ba2d4252f2f02db68d246c62f61c6c54a25300d420) (10 transfers). No other month was reconciled line by line → [Q-31](../OPEN-QUESTIONS.md). For totals, reconcile against the [Safe Transaction Service](https://api.safe.global/tx-service/eth/api/v1/safes/0x91c32893216dE3eA0a55ABb9851f581d4503d39b/transfers/); use the archive for purpose and category.
- **Ends 2026-07-11.** Nothing after: not the [2026-07-30 signer rotation](../02-contracts-and-multisigs/multisigs.md), the Aug 2026 compensation run, or the [DAO Communications retainer](../04-runbook/monthly-compensation.md#dao-communications-retainer-separate-transfer).
- **EP labels may use a proposal's original number.** The 2026-02-07 inbound 125,000 USDC is labelled "[EP 6.28] ENS Retro"; the docs archive files it as [EP 6.30](https://docs.ens.domains/dao/proposals/6.30/) ("originally published as EP 6.28").
- **Spam and poisoning rows are included** (dust inflows, fake tokens, mostly `None`). Never treat a counterparty in such a row as real → [verification & safety](../04-runbook/verification-and-safety.md).

## What it settles for this runbook

- **The 2026 Meta-Gov payouts previously flagged as unverified** ([Q-16](../OPEN-QUESTIONS.md)) are annotated: 75,000 USDC on 2026-05-01 is "Fulfillment of payment for completion of Metagov.org review", the final milestone of [EP 6.30](https://docs.ens.domains/dao/proposals/6.30/) (125,000 USDC [received 2026-02-07](https://etherscan.io/tx/0x6464aca3757d68a42ca8448af53207036b67c20ec8693f1d5ba4cc79d3881d72); 50,000 USDC [paid 2026-03-25](https://etherscan.io/tx/0xdc3b69a1289f9eae33b8dd282004927c86a9d6610483204b2e9c5ac8a6374926); 75,000 USDC [paid 2026-05-01](https://etherscan.io/tx/0xa88bbfebbb01e13c7116f86be0be0e7885b01685aec4614806f614a776583099)). The 18,000 USDC transfers of 2026-04-15 and 2026-05-08 are "Legal Services" / "Recurring legal counsel fees", the continuation of 6,000 USDC payments in [Jan](https://etherscan.io/tx/0xa1d221d41690a6662bc0bec10e1bb27b17eaff0e3c325b361e8b5d0998864ede) and [Feb](https://etherscan.io/tx/0xf75e3f9cc37c5113ab87a650d51ceadc35e9cee2aedf1cf2fd74759bcca89692) 2026 to the same recipient, now listed in [addresses.md](../02-contracts-and-multisigs/addresses.md#recurring-payout-recipients). The earlier note calling that recipient a poisoning lookalike had the real and fake addresses reversed → corrected in [verification & safety](../04-runbook/verification-and-safety.md).
- **Term 6 wind-down.** Ecosystem (main, hackathons, IRL) and Public Goods returned their remaining funds to the Timelock between 2026-06-25 and 2026-07-02 → [term-06.md](../05-terms/term-06.md#activity).
- **Compensation history.** The per-person `Steward compensation` / `Secretary + Steward compensation` / `Scribe compensation` rows on the Meta-Gov Safe are the record of past comp runs through July 2026, useful for the roster diff in [monthly-compensation.md](../04-runbook/monthly-compensation.md).

## Using the file

```bash
git clone https://github.com/gofordylan/ens-wg-transactions
```

```python
import csv, datetime as dt, collections
rows = list(csv.DictReader(open("ens-wg-transactions/ens_wg_transactions.csv")))
for r in rows:
    r["date"] = dt.datetime.strptime(r["Date"], "%b %d, %Y").date()
    r["out"] = r["Amount"].startswith("-")
# Meta-Gov Safe outflows in 2025, by category (count only; amounts are rounded strings)
mg = [r for r in rows if r["Safe"].lower().startswith("0x91c3") and r["out"] and r["date"].year == 2025]
print(collections.Counter(r["Category"] for r in mg))
```

Filter by `Safe` for one multisig, exclude `Internal Transfer` and `Swap` for spend, and read `Description` for the governing forum link.
