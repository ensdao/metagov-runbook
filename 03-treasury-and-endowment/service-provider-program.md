# Service Provider Program (SPP)

The SPP is the **single largest recurring outflow** the Meta-Gov group oversees: a yearly budget streamed to ecosystem service providers via Superfluid.

## SPP1 → SPP2

| Season | Budget | Set by |
|--------|--------|--------|
| **SPP1** | ~$3.6M/yr | [EP5.2](https://docs.ens.domains/dao/proposals/5.2/) — Commence Streams for Service Providers (2024) |
| **SPP2** | $4.5M/yr | [EP6.3](https://snapshot.box/#/s:ens.eth/proposal/0x0cca1cf36731203e235b0e2de9041be3a16d9cdeadff6e15e1f1215c611e12ef) (budget, ranked-choice; beat $3.6M and $2.7M) |

SPP2 providers were selected by Copeland ranked-choice vote [EP6.10](https://snapshot.box/#/s:ens.eth/proposal/0x98c65ac02f738ddb430fcd723ea5852a45168550b3daf20f75d5d508ecf28aa1) and implemented via [EP6.13](https://docs.ens.domains/dao/proposals/6.13/), which routes the $4.5M/yr across 8 providers.

## How payments stream

The Timelock funds USDC into the **Stream Management Pod** Safe, which forwards **100%** on to each provider as a **Superfluid** stream. Exposure is capped at **~50 days** of funding for safety.

```
Timelock ──USDC──▶ Stream Management Pod ──Superfluid stream──▶ each provider
```

The Stream Management Pod address, threshold, and the Superfluid contracts are in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md). Its role in the authorization matrix is in [spending-controls.md](spending-controls.md).

## Source of truth

The DAO forum's **[Service Provider Program category](https://discuss.ens.domains/c/service-provider-program/75)** is the authoritative source for the live provider roster, per-provider stream rates, durations, and quarterly reports — link to it rather than hardcoding per-provider amounts here. The implementing proposal is [EP6.13](https://docs.ens.domains/dao/proposals/6.13/).

> ⚠️ **Open question:** Current SPP2 per-provider stream rates and remaining durations (basic vs extended scopes), and how stream on/off-boarding is operationally handled by the Stream Management Pod, are not pinned here — check the SPP category and EP6.13. The Pod's exact membership/signers are also unverified.

_Cross-link:_ provider profiles (blockful, ETH.LIMO, NameHash Labs, etc.) are catalogued in the runbook directory — see [`../directory.md`](../directory.md).
