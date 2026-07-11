# ENS Protocol Control

Distinct from treasury power: this is who controls the **ENS name system** itself. Ultimately the DAO administers it through the Timelock and the Root contract. Addresses in [addresses.md](addresses.md).

## The Root contract: `root.ens.eth`

Controls allocation and replacement of **all TLDs except `.eth`** (which is permanently locked to the `.eth` registrar), and the TLD→registrar mapping. Root ownership was moved toward the DAO by social proposal **EP 4.10** ([Transfer ENS Root Key Ownership to the DAO](https://docs.ens.domains/dao/proposals/4.10/)), away from the legacy 7-keyholder `multisig.ens.eth`.

> ⚠️ **Open question:** The Root owner currently resolves to `0x4Fe4e666…e3e0e8` (a DAO-side controller). This is **not** the same address as `wallet.ensdao.eth` (the Timelock). Whether it is the Timelock proper, a dedicated DAO-controlled root multisig, or a wrapper is unverified. The exact DAO→root chain of control needs confirmation.

## Core protocol contracts

Administered through the root/registrar hierarchy, ultimately under DAO control via the Timelock ([ENS deployments](https://docs.ens.domains/learn/deployments/)):

| Contract | Role |
|----------|------|
| **ENS Registry** | Root registry mapping nodes → owners/resolvers. |
| **`.eth` BaseRegistrar** | Owns `.eth` registrations (ERC-721); owner may add/remove controllers. |
| **ETHRegistrarController** | `.eth` registration & renewal pricing/flow (a controller on the BaseRegistrar). |
| **DNSRegistrar / DNSSEC** | Lets anyone claim names/TLDs by proving DNS ownership via the DNSSEC oracle; sits under the Root's TLD→registrar mapping. |
| **NameWrapper** | Wraps ENS names as ERC-1155 with fuses/permissions. |
| **PublicResolver** | Default resolver mapping names → records. |

## Controller alias lag

The current ETHRegistrarController per the [ens-contracts deployments wiki](https://github.com/ensdomains/ens-contracts/wiki/ENS-Contract-Deployments) (the source of truth) is `0x59E1…eA547` ("ENS: ETH Registrar Controller 2"), deployed ~mid-2024 and actively processing register/renew txs.

> ⚠️ **Open question:** The human-readable alias `controller.ens.eth` still resolves to the **older** `0x2535…303b`, lagging the deployments-repo source of truth. Verify the active controller against the deployments wiki before relying on the alias.

## Related

- Registration revenue flow (controllers → withdraw → treasury) and the EP 6.39 Registrar Manager: [03-treasury-and-endowment/](../03-treasury-and-endowment/).
- The Timelock that admins these contracts: [contract-hierarchy.md](contract-hierarchy.md).
- Annotated registry/root-control EP timeline (EP 3.5 / 4.10 / 5.27 / 6.7): [../reference/governance-history.md](../reference/governance-history.md).
