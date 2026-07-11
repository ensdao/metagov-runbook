# Governance Contract Hierarchy

All on-chain DAO power flows through one pipeline: **ENS token → Governor → Timelock**. The Timelock is the execution endpoint and treasury custodian. Addresses live in [addresses.md](addresses.md).

```
ENS token (ERC20Votes)  →  voting power
        │
ENS Governor            →  proposal + voting (OZ Governor)
        │ holds PROPOSER_ROLE + EXECUTOR_ROLE
        ▼
ENS Timelock = DAO Wallet (wallet.ensdao.eth)
        →  2-day delay, execution, treasury custody
```

## The three contracts

| Contract | Type | Role |
|----------|------|------|
| **ENS token** (`token.ensdao.eth`) | ERC20Votes, 100M supply | Delegated balance = voting power for every Governor vote. |
| **ENS Governor** (`governor.ensdao.eth`) | OZ Governor | Runs proposal/voting; holds PROPOSER_ROLE/EXECUTOR_ROLE on the Timelock. |
| **ENS Timelock** (`wallet.ensdao.eth`) | OZ TimelockController (**not a Safe**) | Treasury custodian + execution endpoint; owns core protocol contracts and the Endowment Safe. |

The Timelock and the DAO Wallet are the **same address**: one contract, two ENS names ([ENS DAO Contracts](https://basics.ensdao.org/ens-dao-contracts)). ENS docs sometimes loosely call it "the Metagov multisig"; it is **not**. It is the Governor timelock, distinct from the Meta-Gov WG operating Safe.

## Key parameters

On-chain execution config of the Governor/Timelock pipeline:

| Parameter | Value |
|-----------|-------|
| Voting delay | 1 block |
| Voting period | ~45,818 blocks (~6.4 days) |
| Timelock delay | minimum 2 days (172,800 s) |

Source: [ENS DAO Contracts](https://basics.ensdao.org/ens-dao-contracts); [governance process](https://docs.ens.domains/dao/governance/process/). Proposal-submission threshold, quorum, and approval bars are proposal-lifecycle parameters. See [proposals.md](../01-governance/proposals.md). An approved Executable Proposal must wait out the 2-day timelock before it can be executed ([submit a proposal](https://docs.ens.domains/dao/proposals/submit/)).

## Why it matters operationally

Every material treasury move leaves the Timelock only after a full governance cycle. The Timelock owns the Endowment Safe 1/1, so even karpatkey-managed funds are ultimately DAO-controlled. See [03-treasury-and-endowment/](../03-treasury-and-endowment/) and [security-council.md](security-council.md) for the cancel/veto path.
