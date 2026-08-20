# Working-Group Multisigs

Day-to-day DAO spend runs through Gnosis Safes (v1.3.0), each funded from the Timelock by executable proposal. Exact thresholds and addresses live in the [canonical table](addresses.md); the steward + Secretary signer model is described in [Stewards & Roles](../01-governance/stewards-and-roles.md).

## Meta-Governance main Safe: `main.mg.wg.ens.eth`

The only operational WG Safe as of Term 7. Historically its signers followed the Meta-Gov [seat model](../01-governance/stewards-and-roles.md) of three elected stewards plus one appointed Secretary; the threshold and address are in [addresses.md](addresses.md).

The Term 7 rotation is **executed**. Current owners, threshold, and the dedicated `steward.*` signing subnames are in the [canonical address table](addresses.md#meta-gov-safe-signers-term-7), verified on-chain 2026-08-19 (nonce 243). Two things about the result are worth stating plainly, because neither matches what the transition was expected to produce:

- **The threshold is 2 of 4, not the anticipated 2 of 3.** Any two of the four owners can execute.
- **The fourth seat is the DAO Timelock itself**, not a Secretary. `wallet.ensdao.eth` is the Timelock (see the [canonical table](addresses.md)); it replaces the Secretary seat in the historical [seat model](../01-governance/stewards-and-roles.md).

Verified against the [Safe Transaction Service](https://api.safe.global/tx-service/eth/api/v1/safes/0x91c32893216dE3eA0a55ABb9851f581d4503d39b/) and a direct `getThreshold()` / `getOwners()` call.

## SPP stream safe: `stream.mg.wg.ens.eth`

Owners are the DAO Timelock + the Meta-Gov main Safe; threshold and address in [addresses.md](addresses.md). Receives the SPP USDC stream from the Timelock and forwards it on via Superfluid. Mostly dormant since a single 2024-02 distribution. A "3/5" figure seen elsewhere is **incorrect** for this address ([Safe API](https://api.safe.global/tx-service/eth/api/v1/safes/0xB162Bf7A7fD64eF32b787719335d06B2780e31D1/)). See [03-treasury-and-endowment/](../03-treasury-and-endowment/) for the streaming flow.

## Legacy WG Safes (dissolved for Term 7)

The Ecosystem and Public Goods WGs were dissolved entering Term 7 (EP6.44 / ["Path forward"](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107)). Their Safes, `main.eco.wg.ens.eth` and `main.pg.wg.ens.eth`, remain on-chain but are **historical**; unspent WG funds return to the treasury per WG Rule 2.3. Addresses and thresholds in [addresses.md](addresses.md).

## Related

- Endowment Safe (Timelock-owned) and karpatkey fee Safe: [03-treasury-and-endowment/](../03-treasury-and-endowment/).
- Security Council Safe and the emergency veto procedure: [security-council.md](security-council.md).
- Signing procedures and anti-phishing verification: [../04-runbook/](../04-runbook/).
