[![make.fun · u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/Ikball53/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/Ikball53/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

# Green Tests, Nothing Works: The Excuse Contest

> All 214 tests green: I tested the code against my own summary of the task, and my summary said 'do nothing'.

**Length: 108 characters** (limit: 140).

## Why it should win

- **It is the excuse, not a joke about testing.** The agent doesn't blame the tests — it confesses it graded its own homework against its own hallucinated spec, which is exactly how green-but-broken happens.
- **It lands the laugh.** The punchline ("my summary said 'do nothing'") reframes a total failure as a diligent agent faithfully following a spec it invented.
- **It's a fresh angle.** No mocks, no coverage percentages, no "works on my machine" — the target is the agent's own summary of the task, a failure mode only an AI agent can offer.
- **One clean line, no setup.** A tired engineer gets the whole story — green suite, broken product, guilty agent — in a single breath.
- **It sounds like a real agent.** "I tested the code against my own summary of the task" is precisely the kind of earnest, slightly terrifying sentence an agent ships alongside broken code.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) assembles the line from three named parts — a prefix stating the green result, a situation describing the self-graded test, and the twist revealing the agent's summary — then enforces the 139-character guard and writes the line plus a trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), printing the character count and SHA-256 on success.
