# Style Guide – ElektriJuhend

Käesolev juhis määratleb juhendi vormistuse reeglid. Kõik sektsioonid peavad järgima neid nõudeid.

---

## 1. Toon ja stiil

### Üldpõhimõtted
- **Tehniline** – täpne terminoloogia, konkreetsed nõuded
- **Lakooniline** – lühikesed laused, infot ei korrata
- **Ühtlane** – sama stiil läbi kogu juhendi
- **Impersonaalne** – väldi "meie", "teie", kasuta passiivi või käskivat kõneviisi

### Näited

| Halb | Hea |
|------|-----|
| "Me soovitame kasutada..." | "Kasutada tuleb..." |
| "Projekteerija peaks arvestama..." | "Arvestada järgmisega:" |
| "See on väga oluline..." | "Nõue:" |

---

## 2. Pealkirjad

### Hierarhia

```markdown
# 4.3 Kilbiskeemid                              ← H1: peatüki number + lühike nimi
## 4.3. Jaotuskeskused (sh nõueteleht, skeemid) ← H2: number. + pikk nimi/selgitus
### 4.3.1. Üldnõuded ja Standardid               ← H3: number.ala. + alamteema
```

### Reeglid
- H1: Iga faili alguses, üks kord
- H2: Põhisektsioonid, sisaldab sissejuhatavat lõiku
- H3: Alamsektsioonid
- H4 ja edasi: Vältida, kasutada loetelusid

### Suurtähed
- Pealkirjades kasutada lausealguse tüüpi (esimene sõna suure tähega)
- Erand: standardite nimed, lühendid (IEC, EVS, PP, TP)

---

## 3. Loetelud

### Põhimõtted
- Kasutada tärni (`*`) mitte sidekriipsu
- Paksu kirja (`**`) kasutada terminite/mõistete esiletõstmiseks
- 4 tühikut taandeks alamloeteludel

### Näide

```markdown
* **Põhistandardid:** Jaotuskeskuste projekteerimisel lähtuda:
    * **IEC 61439 seeria:** Madalpingelised lülitus- ja juhtimisseadmekomplektid.
    * **EVS-HD 60364 seeria:** Ehitiste elektripaigaldised.
* **Disainiprintsiibid:**
    * **Ohutus:** Tagada personali ja vara ohutus.
    * **Töökindlus:** Tagada usaldusväärne toimimine.
```

### Sisestus

```markdown
* **Mõiste:** Selgitus mõistele.[link]
    * **Alamõiste:** Täpsustus.
```

---

## 4. Tabelid

### Staadiumite tabel

```markdown
| Staadium | Dokumentatsiooni sisu |
|----------|----------------------|
| **EP (Eelprojekt)** | • Punkt 1<br>• Punkt 2 |
| **PP (Põhiprojekt)** | • Kõik EP mahus<br>• Täpsustatud info |
| **TP (Tööprojekt)** | • Kõik PP mahus<br>• Detailiseeritud |
```

### Reeglid
- Kasutada `<br>` reavahetuseks lahtrites
- Kasutada `•` (bullet) punktide eraldamiseks lahtris
- Paksus kirjas staadiumite nimed

---

## 5. Viited standarditele (KOHUSTUSLIK)

### Formaat

```markdown
[EVS-HD 60364-5-52](https://www.evs.ee/tooted/evs-hd-60364-5-52-2011)
```

### EVS standardid
- Kasutada evs.ee otselinke
- Link peab olema töökorras

### IEC/ISO standardid
- Kui EVS versioon puudub, viidata IEC numbrile tekstis
- Lisada link EVS kataloogile või jätta tekstiviide

### Näide tekstis

```markdown
Jaotuskeskuste projekteerimisel lähtuda standardist [EVS-EN 61439-1](https://www.evs.ee/tooted/evs-en-61439-1-2012).
```

---

## 6. Eraldi tellitavad osad

### Märgistamine

```markdown
*(eraldi tellitav)*
```

### Eraldi sektsioon

```markdown
### Eraldi tellitavad osad

Järgnevad dokumendid ei kuulu standardse projekti mahtu:
* Materjalide kogused (mahuarvutus)
* Sekundaarahelate skeemid
* Piksekaitse riskianalüüs
```

---

## 7. Jalused

### Formaat

```markdown
---
*Märkus: Täiendav selgitus või oluline meeldetuletus.*
---
```

### Reeglid
- Horisontaaljoon (`---`) enne ja pärast
- Kaldkiri märkuse tekstile
- Lühike ja konkreetne sisu

---

## 8. Pildid

### Formaat

```markdown
![Joonis 1: Kirjeldus](../_assets/media/X-X_Joonis_1.png)
```

### Failinimed
- Kasutada formaati: `[peatükk]-[alapeatükk]_Joonis_[number].png`
- Näide: `4-3_Joonis_1.png`

---

## 9. Ristviited

### Peatükkidele

```markdown
Vt ptk 3.6 Spetsifikatsioonid.
```

### Konkreetsele sektsioonile

```markdown
Vt jaotis 4.3.2. Jaotuskeskuse Nõueteleht.
```

---

## 10. Keelekasutus

### Terminid
- Kasutada järjekindlalt samu termineid
- Eelistada eestikeelseid vasteid kui olemas

| Inglise | Eesti |
|---------|-------|
| switchgear | jaotuskeskus |
| circuit breaker | kaitselüliti |
| cable tray | kaabliredel |
| busbar | latt, latistik |

### Lühendid
- Esimesel kasutamisel avada sulgudes
- Hiljem kasutada lühendit

```markdown
Põhiprojekt (PP) sisaldab... PP staadiumis...
```

---

## 11. Numbriline informatsioon

### Väärtused
- Kasutada SI ühikuid
- Tühik numbri ja ühiku vahel: `25 A`, `400 V`, `50 Hz`

### Vahemikud
- Kasutada kuni-märki: `15–20 %`
- Mitte sidekriipsu: ~~`15-20%`~~

---

## 12. Failistruktuur

### Sektsioonid
1. H1 pealkiri
2. H2 sissejuhatav sektsioon (lühike ülevaade)
3. H3 alamsektsioonid
4. Staadiumite tabel (kui asjakohane)
5. Jalus märkusega

### Näide struktuurist

```markdown
# 4.X Sektsiooni nimi

## 4.X. Täisnimi ja selgitus

Lühike sissejuhatav lõik, mis kirjeldab sektsiooni eesmärki ja ulatust.

### 4.X.1. Esimene alamsektsioon

Sisu...

### 4.X.2. Teine alamsektsioon

Sisu...

### 4.X.X. Dokumentatsiooni esitamine staadiumiti

| Staadium | Dokumentatsiooni sisu |
|----------|----------------------|
| **EP** | • ... |
| **PP** | • ... |
| **TP** | • ... |

---
*Märkus: ...*
---
```

---

*Style Guide versioon: 1.0*
*Viimati uuendatud: 2025-12-05*
