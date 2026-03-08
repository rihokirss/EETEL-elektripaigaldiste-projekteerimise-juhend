# Elektripaigaldiste projekteerimise juhend

Eesti Elektritööde Ettevõtjate Liidu (EETEL) koostatud juhend elektripaigaldiste projekteerimise alustele ja parimatele praktikatele. Juhend sisaldab põhjalikku infot elektripaigaldiste projekteerimise erinevate aspektide kohta, alates sissejuhatusest kuni spetsiifiliste tehniliste detailideni.

**Veebileht:** [juhend.elektriprojekteerimine.info](https://juhend.elektriprojekteerimine.info)

## Sisukord

1. **Sissejuhatus** — juhendi eesmärk, kasutamine, terminid, normatiivsed viited, vastutus ja pädevus
2. **Projekteerimine** — etapid, lähteülesanne, koostöö, riskianalüüs ja ohutus
3. **Dokumentatsioon** — üldnõuded, digitaalne vormistamine, struktuur, joonised, skeemid, spetsifikatsioonid, arvutused
4. **Tugevvool** — üldskeemid, kilbiskeemid, kaabliteed, jõupaigaldised, maandus ja piksekaitse
5. **Valgustus** — valgustuspaigaldised, välisvalgustus, valgustusdisain
6. **Nõrkvool** *(arendamisel)*
7. **Hooneautomaatika** — üldnõuded, seletuskiri, struktuurskeemid, tasapinnaplaanid, loetelud, BIM nõuded
8. **BIM** — BIM nõuded elektriprojekteerimises
9. **Kvaliteet** *(arendamisel)*
10. **Lisad** *(arendamisel)*

## Funktsioonid

- 10 peatükki elektripaigaldiste projekteerimisest
- Material for MkDocs teema
- Hele/tume režiim
- Täisteksti otsing
- PDF allalaadimine
- Eestikeelne sisu

## Tehnilised nõuded

- Python 3.8+
- MkDocs 1.4.0+
- MkDocs Material teema
- mkdocs-with-pdf (PDF eksport)

## Paigaldus

```bash
# Klooni repositoorium
git clone https://github.com/rihokirss/EETEL-elektripaigaldiste-projekteerimise-juhend.git

# Liigu projekti kausta
cd EETEL-elektripaigaldiste-projekteerimise-juhend

# Loo virtuaalkeskkond ja paigalda sõltuvused
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Käivita arendusserver
mkdocs serve

# Ehita koos PDF-iga
ENABLE_PDF_EXPORT=1 mkdocs build
```

## Kaastöö

Kui soovid kaasa aidata juhendi täiendamisel:

1. Tee fork repositooriumist
2. Loo uus haru (`git checkout -b feature/amazing-feature`)
3. Tee oma muudatused
4. Commit muudatused (`git commit -m 'Lisa uus funktsionaalsus'`)
5. Push haru (`git push origin feature/amazing-feature`)
6. Ava Pull Request

## Litsents

See projekt on litsentseeritud MIT litsentsi all.

## Kontakt

- Riho Kirss — [riho@kirss.ee](mailto:riho@kirss.ee) — [@rihokirss](https://github.com/rihokirss)
- Dmitri Gridin — [@dmitrig372](https://github.com/dmitrig372)
