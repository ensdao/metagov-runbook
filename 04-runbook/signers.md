# Signer Good Practices & Rotation

Standard for anyone who holds a key on the [Meta-Gov multisig](../02-contracts-and-multisigs/addresses.md). The seat model (elected stewards + Secretary) is described in [stewards & roles](../01-governance/stewards-and-roles.md); the current threshold and owner set are in the [address table](../02-contracts-and-multisigs/addresses.md).

## Good-practices standard

- **Dedicated signing identity.** Each signer registers a `steward.<their-ens>.eth` subdomain (e.g. `steward.netto.eth`) used **only** for signing on the multisig. Owners on the Safe should resolve to these names.
- **Separation of signing and payment.** The signing address **MUST differ** from the address that receives the signer's compensation. The comp address may stay private — it never needs to appear on the Safe.
- **Dedicated hardware wallet.** The signing key lives on a hardware wallet (e.g. Ledger) kept on the person and used **only** for this multisig. The DAO can budget a new dedicated device per signer.
- **Verify before signing.** Confirm checksummed addresses and that each recipient resolves to its expected ENS name — never trust "last interacted" autofill. Full anti-phishing standard: [verification-and-safety.md](verification-and-safety.md).

## Rotation mechanics

On a seat change (see [elections](../01-governance/elections.md)):

| Change | Safe action |
|---|---|
| Add a new signer | `addOwnerWithThreshold(newOwner, threshold)` — preserve the threshold |
| Replace a signer in place | `swapOwner(prevOwner, oldOwner, newOwner)` — preserve the threshold |

Before and after rotation, **verify each owner resolves to the expected `steward.*` name** (via `getOwners()` on the Safe). The incoming signer should provision their dedicated hardware wallet and `steward.<ens>.eth` subdomain **before** being added.

> ⚠️ **Open question:** The [Path forward vote](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107) indicates Term 7 moves toward **2-of-3** signing with the Secretary optional. Re-verify the Safe threshold and owner set after the Term 7 transition before applying these rotation steps.
