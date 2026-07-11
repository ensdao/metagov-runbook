# The Endowment

The Endowment is the DAO's long-term reserve, professionally managed by **karpatkey** with independent financial reporting by **Steakhouse**. It lives in a dedicated Gnosis Safe, `endowment.ensdao.eth`, **owned 1/1 by the Timelock**.

## Non-custodial custody model

karpatkey is **not** a Safe signer. It operates the endowment only through a **Zodiac Roles Modifier V2** whitelist that defines exactly which protocols and actions the manager EOA may take. karpatkey cannot self-grant permissions or move funds outside the whitelist; every new integration requires a DAO executable proposal. How that whitelist is changed is covered in [endowment-permissions.md](endowment-permissions.md). Endowment Safe, Roles Modifier, and manager EOA addresses are in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md).

## Manager selection & policy

- **Manager selection** — karpatkey was selected over other candidates via ranked-choice vote [EP2.2.5](https://snapshot.box/#/s:ens.eth/proposal/0x1ab7ef84f6e904582d5b5b921944b5b1a8e36dbff1f1248fde87fef02b046816) (Nov 2022), establishing the manager relationship and fee model.
- **Investment Policy Statement (IPS)** — [EP5.20](https://docs.ens.domains/dao/proposals/5.20/) (Snapshot, Oct 2024) is the governing IPS for asset allocation and the manager mandate.
- **Fees** — 0.5%/yr management fee (paid **monthly in ETH**) + 10% performance fee on yields. The management fee is paid without a per-payment vote via a Safe Allowance Module — see [spending-controls.md](spending-controls.md).

## Funding tranches

| Tranche | Proposal | Notes |
|---------|----------|-------|
| First | [EP3.4](https://docs.ens.domains/dao/proposals/3.4/) (2023) | Stood up the Endowment Safe + Roles permission framework; Ackee/Sub 7 audited |
| Second | [EP4.2](https://docs.ens.domains/dao/proposals/4.2/) (2023) | Funded after the first performance review |
| Third | [EP6.2](https://docs.ens.domains/dao/proposals/6.2/) (2025) | Raised capital utilisation; tuned the fee Allowance Module reset |

## Reporting cadence

- **Monthly** endowment reports posted by karpatkey ([rolling thread](https://discuss.ens.domains/t/endowment-monthly-reports/17614)); **monthly** financial updates from Steakhouse.
- **Weekly** endowment updates + **monthly** financial updates presented at Meta-Gov calls.
- **Biannual / annual** forum reviews.
- Live figures: **[reports.kpk.io/ens](https://reports.kpk.io/ens)** — _as of 2026-06-20_, prefer this over any hardcoded AUM.
