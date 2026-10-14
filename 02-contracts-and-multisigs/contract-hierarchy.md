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
| **ENS Timelock** (`wallet.ensdao.eth`) | OZ TimelockController (**not a Safe**) | Treasury custodian + execution endpoint; owns core protocol contracts. Owned the Endowment Safe until 2026-08-11 (see below). |

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

Every material treasury move leaves the Timelock only after a full governance cycle. See [03-treasury-and-endowment/](../03-treasury-and-endowment/) and [security-council.md](security-council.md) for the cancel/veto path.

## The Endowment control chain (since 2026-08-11)

The Endowment no longer sits under the Governor → Timelock pipeline. The executable ["Next Era of ENS DAO: Empowering the ENS Foundation"](https://discuss.ens.domains/t/22329) moved its ownership to a separate timelock ([tx](https://etherscan.io/tx/0xd38d35f55f4387301b5cdf738aabc16d38189df02cafa50c8a47a70605779422)):

```
ENS Foundation Safe (3/5)            Security Council Safe (5/8)
        │ PROPOSER_ROLE: schedule            │ owns
        ▼                                    ▼
EndowmentTimelock  ◄── cancel ──  EndowmentSecurityCouncil
        │  9-day delay, anyone executes
        ▼ sole owner (1/1)
Endowment Safe (endowment.ensdao.eth)
        ├─ Roles Modifier      → karpatkey actions (no timelock)
        └─ Allowance Module    → monthly fee via Meta-Gov Safe (no timelock)
```

The DAO Timelock holds no role on the EndowmentTimelock (checked on-chain 2026-10-14). Tokenholders keep the power to appoint and remove Foundation directors ([proposal text](https://discuss.ens.domains/t/22329)). Roles, delays and the module paths: [endowment-permissions.md](../03-treasury-and-endowment/endowment-permissions.md). Addresses: [addresses.md](addresses.md).
