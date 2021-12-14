# Käyttöohje

## Asennus

Kun olet ladannut ohjelman koneellesi Releaseista ja purkanut sen haluttuun hakemistoon, voit käynnistää ohjelman noudattamalla seuraavia ohjeita

1. Asenna ohjelman käyttävät riippuvuudet komennolla:
```bash
poetry install
```
2. Käynnistä ohjelma komennolla:
```bash
poetry run invoke start
```

## Ohjelman käyttö

Ohjelma käynnistyy päänäkymään, josta löytyy ylälaidasta yleinen file-valikko, sekä sen alapuolelta työkalupaletti eri ohjelman tarjoamista työkaluista. Näiden alta löytyy muokkaus-näkymä, josta käyttäjä näkee muokattavan dokumentin, sekä voi muokata dokumenttia reaaliaikaisesti. 

## Työkalut

### Teksti
Teksti -työkalusta voidaan muuttaa käsiteltävän tekstin tyyliä. 
### Kuva
Kuva -työkalun kautta voidaan lisätä dokumenttiin kuvia, sekä muokata tai poistaa jo lisättyjä kuvia

## Työn tallentaminen

Työn voi tallentaa tiedostoon yläpalkista löytyvästä File -valikosta, valitsemalla save tai save as