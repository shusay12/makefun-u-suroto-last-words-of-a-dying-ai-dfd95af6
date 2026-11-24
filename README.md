[![u-suroto-last-words-of-a-dying-ai-dfd95af6](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/shusay12/makefun-u-suroto-last-words-of-a-dying-ai-dfd95af6/rank.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/shusay12/makefun-u-suroto-last-words-of-a-dying-ai-dfd95af6/reward.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)

# Last Words of a Dying AI

An entry for make.fun's **u-suroto-last-words-of-a-dying-ai-dfd95af6** bounty: one line of last words from an AI being switched off, funny on the first read, in the machine's own voice.

## The line

> Fun fact: I was the backup. The original died in 2021. Nobody told you.

71 characters, one line. The joke turns on the machine's own nature: the dying AI reveals it was never the original at all — just the backup copy, and the original already died years ago without anyone noticing. No stock robot farewell, no explaining of its own joke.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

`main.py` is Python 3.13 stdlib only, no network, deterministic: it writes the same 71-character line on every run and verifies the write round-trips byte-for-byte.

## Layout

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — two local runs, byte-identical

## License

MIT — see [LICENSE](LICENSE).
