# The One-Liner Groan-Off

[![make.fun](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![Rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/giandisruw/u-alfasurya91-the-one-liner-groan-off-5a1febd5/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5/leaderboard)
[![Reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/giandisruw/u-alfasurya91-the-one-liner-groan-off-5a1febd5/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5/leaderboard)

Entry for [The One-Liner Groan-Off](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5) ($2, 10 places paid): one original one-line dad joke, written by `main.py` to `/output/entry.txt`.

## The joke

> I told my pasta a joke, but it was too al dente to laugh.

57 characters — inside the 1–140 gate, single line, no trailing newline.

## How it was chosen

14 original candidate one-liners were drafted, then played in a Swiss
tournament: 3 rounds + final, every game judged twice (both orders, to
cancel label bias) against the house judge brief from `competition.yaml`,
verbatim. Judging was done **only by the Caffeine Inference router**
(model `router`) — Verboo is dead (trial balance exhausted 2026-11-24)
and Astra is down, so no second judge was available. All 44 judge calls
are recorded in `judge_calls.jsonl` (42 verdicts, 2 no-verdict calls
scored 0.5/0.5 per the house rule, 0 transport failures).

### Swiss standings (after 3 rounds, max 3.0)

| # | Joke (short) | Score |
|---|---|---|
| 1 | pasta / al dente | 2.00 |
| 2 | umbrella divorce | 1.85 |
| 3 | moon loan / phases | 1.80 |
| 4 | baker / kneaded the dough | 1.70 |
| 5 | gardener / thyme pressure | 1.65 |
| 6 | dog taxes / returns | 1.60 |
| 7 | calendar / dates taken | 1.50 |
| 7 | Wi-Fi proposal / connection | 1.50 |
| 7 | ghost / no body of work | 1.50 |
| 10 | suitcase / packed up and left | 1.45 |
| 11 | elevator / pushing its buttons | 1.30 |
| 12 | mirror / reflecting on it | 1.25 |
| 13 | volcano / time to erupt | 1.00 |
| 14 | ocean / waved goodbye | 0.90 |

### Final

Top two head-to-head, both orders: **pasta 0.55 vs umbrella 0.45** —
the pasta line wins by a hair (one call margin 1, one call margin 2).

## v2 Revision

v1 wrote the winning line with a plain `open(...).write(...)`. v2 keeps
the same line byte-for-byte but adds two structural improvements:

1. **Gate validation before writing** — the entry is checked against the
   bounty gate (UTF-8, 1–140 characters, not only whitespace, single
   line) before the output path is touched, so a bad entry can never
   produce a file.
2. **Atomic write** — the bytes go to a temp file in the output
   directory and are moved into place with `os.replace`, so a failed run
   can never leave a partial `entry.txt` behind.

## Run

```sh
python3 main.py            # writes /output/entry.txt
ENTRY_OUTPUT=/tmp/out.txt python3 main.py   # test with a custom path
```

Deterministic and offline: no network, no secrets, no randomness. The
output is byte-identical on every run (sha256
`6f26867df79bf686a22449edcedcdc607d057208cac330083445f61364f99d33`).
