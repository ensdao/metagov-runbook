# Revenue Flow

How `.eth` registration revenue moves from a user payment into the DAO's managed reserves. Since [EP6.39 Treasury Flow Automation](https://discuss.ens.domains/t/executable-treasury-flow-automation/21923), the destination is the **Endowment** rather than the Timelock.

## The flow (current)

```
.eth registration / renewal
        │  fees accrue in
        ▼
ETHRegistrarController(s)
        │  anyone calls withdraw()  (permissionless)
        ▼
Registrar Manager  (owns the controllers)
        │  sweeps ETH directly to
        ▼
Endowment Safe  (endowment.ensdao.eth)
        │  karpatkey manages / converts within policy
        ▼
runway top-ups pushed back to the Timelock  (see treasury-automation.md)
```

## Steps

1. **A user registers or renews a `.eth` name.** Fees accrue in the [ETHRegistrarController(s)](https://docs.ens.domains/faq/).
2. **Anyone calls `withdraw()`.** The sweep is **permissionless**: no privileged signer, no vote. Historically this swept ETH to `wallet.ensdao.eth`; under EP6.39 the **Registrar Manager** now owns the controllers and routes the ETH **directly to the Endowment Safe** (`endowment.ensdao.eth`).
3. **karpatkey manages the proceeds** inside the Endowment under its DAO-voted permissions, including ETH→stables conversion via CoW Swap (no per-swap vote).
4. **Operating runway is topped back up** from the Endowment to the Timelock via a scoped Zodiac permission, detailed in [treasury-automation.md](treasury-automation.md).

## Notes

- The **Registrar Manager** is a new component introduced by EP6.39; it owns the registrar controllers and exposes the permissionless `withdraw()`. Its address is in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md).
- The `controller.ens.eth` ENS alias lags the canonical controller deployment ([source-of-truth deployments wiki](https://github.com/ensdomains/ens-contracts/wiki/ENS-Contract-Deployments)); verify the active controller before relying on the alias.
- Background on how protocol revenue is generated: [ENS Protocol Revenue](https://basics.ensdao.org/protocol-revenue).
