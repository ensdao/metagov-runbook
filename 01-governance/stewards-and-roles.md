# Stewards & Roles

Each Working Group is run by elected Stewards, with role definitions set out in the [Working Group Rules](https://docs.ens.domains/dao/wg/rules/). How stewards are elected: see [elections.md](elections.md).

## Roles

| Role | How appointed | Responsibilities |
| --- | --- | --- |
| **Steward** | Elected per the [election cycle](elections.md); three seats per Working Group. | Run the Working Group; reallocate within approved budget (WG Rule 10.5). |
| **Lead Steward** | Appointed from the elected stewards within **5 days** of term start. Removable by simple majority of the group's stewards. | Operational management, approving resource requests, initiating fund disbursement, posting DAO updates. |
| **Secretary** | Appointed by majority vote of all stewards. | Coordinates cross-WG communication and meetings; serves as a multisig keyholder; compensated by Meta-Gov. |
| **Scribe** | — | _Not documented in the available sources._ |

> ⚠️ **Open question:** Whether the Secretary role is retained now that Meta-Gov is the sole Working Group is unverified — its cross-WG-coordination purpose is reduced, and the ["Path forward"](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107) thread indicates Term 7 stewards may opt not to appoint one (duties handled collectively).

## The multisig seat model

The Meta-Gov operating multisig is a Gnosis Safe whose signer seats are the **3 elected stewards + 1 appointed Secretary** (four seats) ([Meta-Gov WG](https://basics.ensdao.org/metagovernance-wg)). The same seat model applied to the legacy WG multisigs. For the live signing threshold, signer composition, and addresses, see the [multisigs reference](../02-contracts-and-multisigs/multisigs.md) and the canonical [address table](../02-contracts-and-multisigs/addresses.md). Current stewards: see the [directory](../directory.md).

> ⚠️ **Open question:** The ["Path forward"](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107) thread indicates Term 7 moves toward a **2-of-3** signing structure with the Secretary optional; the post-transition Safe configuration is unverified.
