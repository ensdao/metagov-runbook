# ⭐ Verification & Safety (Anti-Phishing)

**Read this before signing anything.** The Meta-Gov Safe transaction history is polluted with phishing artifacts. Some are designed specifically to make a signer approve a transfer to the wrong address. None of the items in this page are legitimate Meta-Gov activity ([Safe Tx Service](https://app.safe.global/)).

## The two hazards in our Safe history

### 1. Address-poisoning lookalikes

Attackers send dust from, or trigger zero-value `transferFrom` calls to, addresses that visually match a real counterparty: same leading and trailing characters, different middle. The goal is that you later copy the **wrong** one from your "recent" list.

Example from our history, around the legal-counsel payments to the real recipient `0x8320Ea33…Fdb718DF` (listed in [addresses.md](../02-contracts-and-multisigs/addresses.md#recurring-payout-recipients)). On each payment day, `0x8320015E…3b718dF` and `0x8320e687…0418DF` sent USDC dust **to** the Safe ([tx](https://etherscan.io/tx/0x39dea08ac52ce7b4ef44288169cd4cfde939a7a7b7b748df6be4a646df659262), [tx](https://etherscan.io/tx/0x279ea7f5ea75d7a8b1ab5d3089bf76de58ec4aba4a89ff17758bee157bc2b866)), and `0x8320216c…7118dF` appears as an **outgoing** counterparty through zero-value transfers ([tx](https://etherscan.io/tx/0xd5c792dd626b93bbf038deb53a037ea52e9f2332384d175389a321f99f60cc4b)), so all three sit next to the real address in the Safe's recent list, and one of them shares the real address's last six characters. The same was done to the EP 6.30 milestone recipient `0x149B9013…7E4Dec` (lookalike `0x149bbA6E…Ef4dEC`, [tx](https://etherscan.io/tx/0x3a2776dca6f767516c305d2e112c138a31e37497d80e0b591f526eecf382ad2e)).

> **Correction (2026-09-01).** An earlier version of this page had the real and poisoned `0x8320…` addresses reversed. The on-chain record settles it: four signed USDC payments went to `0x8320Ea33…Fdb718DF` ([Jan](https://etherscan.io/tx/0xa1d221d41690a6662bc0bec10e1bb27b17eaff0e3c325b361e8b5d0998864ede), [Feb](https://etherscan.io/tx/0xf75e3f9cc37c5113ab87a650d51ceadc35e9cee2aedf1cf2fd74759bcca89692), [Apr](https://etherscan.io/tx/0xf52af7f6a6a917f8b462c4fd35b2e9e9c93f88b4fda0248a55f6c11eda3dea5b), [May](https://etherscan.io/tx/0x616e626dc7673511ed5f85d452b08595930389b6b5f4acc4ccf9d41f276abe7d) 2026), annotated as legal-counsel fees in the [WG transaction archive](../reference/wg-transaction-history.md); the other `0x8320…` addresses only ever appear in dust or zero-value traffic.

### 2. Homoglyph fake-token spam

Fake "USDC" tokens show **fictitious** transfers in the token list to look like real activity. Some use Cyrillic look-alike letters (`USDС` / `UЅDC`); some carry the exact name and symbol "USD Coin / USDC" and differ only by contract address. Example: on 2026-05-08 three fake 18,000 "USDC" transfers from the Safe to a lookalike address ([tx](https://etherscan.io/tx/0x414d7dc314c3d259b37956ef92f1a9bf8511a3b22af4afd9cf79f94412082b63), token `0x567fC8…F35D`) mirrored the real 18,000 USDC legal payment made the same day. The real USDC contract is the one listed in [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md); check the contract, not the symbol.

## Mandatory checks before every signature

1. **Verify the full checksummed address.** Compare all 42 characters against [addresses.md](../02-contracts-and-multisigs/addresses.md) or the governing EP, not just the truncated `0x12…ab` form.
2. **Verify the ENS name resolves.** Every recipient that should have an ENS name must reverse-resolve to its **expected** name. A lookalike address will not.
3. **Verify the token contract.** Confirm the asset is the canonical USDC/ENS contract; a clone can carry the identical name and symbol.
4. **Never trust "last interacted" / autofill.** Do not pick recipients from the Safe's recent-address suggestions. Always paste from the versioned roster or the EP.
5. **Confirm the decoded calldata.** For batches, read the decoded `multiSend` in the Transaction Builder; counts and amounts must match the source roster.

> If any check fails, **do not sign.** Flag it to the other signers and resolve before proceeding.

## Previously flagged entries (resolved)

Two 2026 payouts were listed here as unconfirmed. Both are annotated in the [WG transaction archive](../reference/wg-transaction-history.md): 75,000 USDC to `0x149B9013…7E4Dec` (2026-05-01) was the final [EP 6.30](https://docs.ens.domains/dao/proposals/6.30/) milestone payment, and the 18,000 USDC transfers to `0x8320Ea33…Fdb718DF` (2026-04-15, 2026-05-08) are legal-counsel fees (see the correction above). What remains open is the legal engagement's paperwork → [OPEN-QUESTIONS Q-16](../OPEN-QUESTIONS.md).

The archive is the record of *purpose* for past transactions; it is not a substitute for the checks above on the next one.
