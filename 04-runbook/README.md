# 04: Operational Runbook

> 🚨 **Emergency:** Malicious proposal queued in the Timelock → **[../02-contracts-and-multisigs/security-council.md](../02-contracts-and-multisigs/security-council.md)**. Suspected phishing / poisoned address → **[verification-and-safety.md](verification-and-safety.md)**.

Step-by-step procedures for the recurring on-chain operations the Meta-Governance Working Group runs out of its Safe multisigs, the "how to actually do it" pages: onboarding, safety, compensation, funding, token distribution, and treasury-manager fees.

## Before you do anything: safety first

Every signer **must** read **[verification-and-safety.md](verification-and-safety.md)** before approving any transaction. The Meta-Gov Safe history contains address-poisoning lookalikes and homoglyph fake-token spam designed to trick signers ([Safe Tx Service](https://app.safe.global/)). Treat checksum + ENS-name verification as mandatory, not optional.

## Pages

| Page | When / cadence |
|---|---|
| [onboarding.md](onboarding.md) | New steward, day one |
| [verification-and-safety.md](verification-and-safety.md) | Every signature |
| [calendar.md](calendar.md) | Annual operating cadence |
| [monthly-compensation.md](monthly-compensation.md) | ~Monthly (1st–2nd) |
| [funding-request.md](funding-request.md) | Per term (+ automated runway) |
| [token-distribution.md](token-distribution.md) | Per governing EP |
| [treasury-manager-fees.md](treasury-manager-fees.md) | Monthly (automated) |
| [signers.md](signers.md) | On seat change / signer setup |

## Conventions

- **Addresses & thresholds:** all canonical addresses and Safe thresholds live in [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md). Verify there, never from autofill.
- **Batches:** multi-recipient operations use the Safe **Transaction Builder** so all signers review one batch instead of N transactions.

## Related

- Treasury & endowment flows → [../03-treasury-and-endowment/](../03-treasury-and-endowment/)
- Proposal history (EPs referenced here) → [../reference/governance-history.md](../reference/governance-history.md)
