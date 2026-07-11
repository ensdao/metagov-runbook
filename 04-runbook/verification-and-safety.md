# ⭐ Verification & Safety (Anti-Phishing)

**Read this before signing anything.** The Meta-Gov Safe transaction history is polluted with phishing artifacts. Some are designed specifically to make a signer approve a transfer to the wrong address. None of the items in this page are legitimate Meta-Gov activity ([Safe Tx Service](https://app.safe.global/)).

## The two hazards in our Safe history

### 1. Address-poisoning lookalikes

Attackers send dust from an address that visually matches a real counterparty — same first/last characters, different middle. Example seen in our history: `0x8320ea…718df` (poison) vs. the real `0x8320216c…118df` ([Safe Tx Service](https://app.safe.global/)). The goal is that you later copy the **wrong** one from your "recent" list.

### 2. Homoglyph fake-token spam

Fake "USDC" tokens minted with Cyrillic look-alike letters — e.g. `USDС` / `UЅDC` (Cyrillic `С`/`Ѕ`) — show **fictitious** transfers in the token list to look like real activity ([Safe Tx Service](https://app.safe.global/)). The real USDC contract is the one listed in [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md).

## Mandatory checks before every signature

1. **Verify the full checksummed address** — compare all 42 characters against [addresses.md](../02-contracts-and-multisigs/addresses.md) or the governing EP, not just the truncated `0x12…ab` form.
2. **Verify the ENS name resolves** — every recipient that should have an ENS name must reverse-resolve to its **expected** name. A lookalike address will not.
3. **Verify the token contract** — confirm the asset is the canonical USDC/ENS contract, not a homoglyph clone.
4. **Never trust "last interacted" / autofill** — do not pick recipients from the Safe's recent-address suggestions. Always paste from the versioned roster or the EP.
5. **Confirm the decoded calldata** — for batches, read the decoded `multiSend` in the Transaction Builder; counts and amounts must match the source roster.

> If any check fails, **do not sign.** Flag it to the other signers and resolve before proceeding.

## Known unverified entries

Some payouts in the history are **not confirmed** as legitimate Meta-Gov activity and should not be treated as precedent.

> ⚠️ **Open question:** Purpose and recipient of 75,000 USDC to `0x149b9013…4dec` (2026-05-01) and the recurring 18,000 USDC to `0x8320ea…718df` (2026-04-15, 2026-05-08) are unconfirmed; the second recipient is a known poisoning lookalike ([Safe Tx Service](https://app.safe.global/)).
