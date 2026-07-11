# Spending Controls: Who Signs What

Every material spend ultimately traces back to a DAO governance proposal. This is the authorization matrix for **which path** authorizes which kind of outflow, and what signing it requires.

## Authorization matrix

| Outflow | Authorized by | Signing / threshold |
|---------|---------------|---------------------|
| Funds leaving the **main treasury** | Executable proposal | Governor vote + **2-day timelock**, then executes from the Timelock. Vote thresholds in [`../01-governance/proposals.md`](../01-governance/proposals.md) |
| **WG operating spend** (within approved budget) | Working Group stewards | Meta-Gov WG Safe (threshold in [addresses.md](../02-contracts-and-multisigs/addresses.md); seat model in [`../01-governance/stewards-and-roles.md`](../01-governance/stewards-and-roles.md)) |
| **SPP provider streams** | EP6.13 (pre-authorized) | Stream Management Pod forwards 100% via Superfluid; exposure capped ~50 days. See [service-provider-program.md](service-provider-program.md) |
| **karpatkey DeFi actions** in the endowment | Zodiac **Roles Modifier V2** whitelist | Manager EOA acts within whitelist only; no per-action vote. See [endowment-permissions.md](endowment-permissions.md) |
| **karpatkey monthly management fee** | Safe **Allowance Module** (authorized once) | `executeAllowanceTransfer` module tx; no per-payment vote. Allowance/reset in [addresses.md](../02-contracts-and-multisigs/addresses.md) |
| **Runway top-up** (endowment → Timelock) | Zodiac runway permission (EP6.39) | ETH/USDC to the Timelock only; no per-transfer vote. See [treasury-automation.md](treasury-automation.md) |

Thresholds and signer composition are verified in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md).

## The normative basis: Constitution Article III

All spending is bound by **[Article III](https://docs.ens.domains/dao/constitution/)** of the ENS Constitution: treasury funds must first ensure the long-term viability of ENS and fund its development, with surplus directed to public goods. Within an approved budget, WG stewards have discretion to reallocate ([Working Group Rule 10.5](https://docs.ens.domains/dao/wg/rules/)) but cannot violate the Constitution.

## Verification hazards (anti-phishing)

Before signing **any** multisig transaction:

- **Verify the full checksummed address AND its ENS name.** The Meta-Gov Safe history contains **address-poisoning lookalikes** and **homoglyph fake-"USDC"** tokens (e.g. Cyrillic `USDС`) showing fictitious transfers. These are phishing, not DAO activity.
- **Never trust "last interacted" autofill.** Re-derive recipients from the governing proposal / roster.

> ⚠️ **Open question:** Some Safe payouts (e.g. 75,000 USDC and recurring 18,000 USDC transfers in 2026) have unconfirmed purpose/recipient. Confirm against a governing EP before treating them as routine.
