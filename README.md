# Republic of Pluvia — Passport Spread

[![Competition](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)
[![Rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/Kiowayyy2109/makefun-passport/rank.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)
[![Reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/Kiowayyy2109/makefun-passport/reward.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)

An open passport spread for the Republic of Pluvia, a small country where it
rains 300 days a year. The left page is the data page for Maris Vello of
Nimbara: a raincoat portrait, bilingual Pluvian/English fields, the printed
condition "Bearer must carry an umbrella at all times", and a two-line
machine-readable zone whose number, birth date and expiry match the printed
fields. The right page is a visas page whose stamps tell one consistent
journey — departed Pluvia 02 Jun 2024, arrived in the Kingdom of Solenne the
same day, departed Solenne 09 Jun 2024, arrived in the Federated Isles of
Corvane 10 Jun 2024 — plus a purple RAIN TAX — PAID stamp from Nimbara.
The passport was issued in Nimbara on 14 Mar 2022 and expires 13 Mar 2032;
every stamp falls after the issue date.

## Run it

```sh
mkdir -p /output
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies
`artwork.png` to `/output/entry.png` byte-for-byte and verifies the copy
against its recorded SHA-256, so two runs always produce identical bytes.
The image is 1024x1024 PNG, under the 1 MiB limit.
