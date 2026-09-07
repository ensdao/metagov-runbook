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

## Historical spend record

Every WG Safe's transactions 2022–2026, categorised and described, are archived from SafeNotes → [wg-transaction-history.md](../reference/wg-transaction-history.md). The 2026 Meta-Gov payouts once flagged here as unconfirmed are annotated there: 75,000 USDC (2026-05-01) was the final [EP 6.30](https://docs.ens.domains/dao/proposals/6.30/) milestone payment, and the 18,000 USDC transfers (2026-04-15, 2026-05-08) are legal-counsel fees to the recipient now listed in [addresses.md](../02-contracts-and-multisigs/addresses.md#recurring-payout-recipients).

> ⚠️ **Open question:** The legal engagement itself (firm, authorising budget line, whether it continues in Term 7) is not documented on the forum → [OPEN-QUESTIONS Q-16](../OPEN-QUESTIONS.md).
