# EscrowDispute — AI-Arbitrated Marketplace Escrow

Built for GenLayer Agent Tank Hackathon 2026 — **Onchain Justice** track.

## What it does

EscrowDispute is a GenLayer Intelligent Contract that resolves marketplace
disputes between a buyer and a seller using an onchain AI jury, instead of
a human moderator or a centralized platform.

1. A buyer deploys the contract with a seller's address and a plain-language
   job spec (e.g. "Design a vector logo containing a blue dragon").
2. The seller submits their deliverable through `submit_work`.
3. Either party calls `resolve_dispute`. GenLayer validators independently
   run an LLM prompt asking whether the deliverable satisfies the spec, and
   reach consensus on a YES/NO verdict using GenLayer's Equivalence
   Principle (`gl.eq_principle.strict_eq`).
4. The contract automatically updates its status to either
   `RELEASED_TO_SELLER` or `REFUNDED_TO_BUYER` based on the AI jury's
   consensus verdict — no human arbitrator required.

## Why GenLayer

Ordinary smart contracts can only verify deterministic facts (a signature,
a balance, a hash). They can't judge whether a deliverable actually
satisfies a natural-language agreement. GenLayer's Intelligent Contracts
solve this by letting independent validators run an LLM call and reach
consensus on a subjective judgment, which is exactly what a marketplace
dispute needs.

## Deployed Contract

- **Address:** `[PASTE YOUR FINAL CONTRACT ADDRESS HERE]`
- **Network:** GenLayer Studio (Studio Next / Devnet)
- **Explorer / Studio link:** `[PASTE YOUR STUDIO LINK HERE]`

## Contract Methods

| Method | Type | Description |
|---|---|---|
| `get_status()` | view | Returns current status: `OPEN`, `SUBMITTED`, `RELEASED_TO_SELLER`, or `REFUNDED_TO_BUYER` |
| `submit_work(work_link: str)` | write | Seller submits proof/link to the completed deliverable |
| `resolve_dispute()` | write | Triggers the AI jury to judge the deliverable against the spec and settle the escrow |

## How to Test

1. Open the contract in GenLayer Studio using the address above.
2. Deploy or connect to the existing instance.
3. Call `submit_work` with any short text description of a deliverable
   (e.g. `"Blue dragon vector logo attached."`).
4. Call `resolve_dispute` and wait a few seconds for validator consensus.
5. Call `get_status` to see the final verdict.

To see the refund path, deploy a fresh instance and submit a deliverable
that clearly does **not** match the spec (e.g. spec asks for a "blue
dragon logo" but you submit "a poem about cats") — `get_status` should
return `REFUNDED_TO_BUYER`.

## Tech

- Language: Python (GenLayer SDK / GenVM)
- Consensus: GenLayer Optimistic Democracy, `gl.eq_principle.strict_eq`
- LLM judging: `gl.nondet.exec_prompt`

## Author

`[YOUR NAME / HANDLE]`
