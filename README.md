# WYSIWYG Editori

![kuva](./dokumentaatio/kuvat/screenshot.png)

Sovelluksen avulla käyttäjä voi luoda HTML-koodia visuaalisen editorin avulla. Käyttäjä voi luoda ohjelman avulla yksinkertaisen verkkosivun ja tallentaa sen


## Dokumentaatio
 - [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)

- [Vaativuusmäärittely](./dokumentaatio/vaativuusmaarittely.md)

- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuurikuvaus.md)

- [Käyttöohje](./dokumentaatio/kayttoohje.md)

- [Testaus](./dokumentaatio/testaus.md)

## Releaset

[Viikko 5](https://github.com/msha/ot-harjoitustyo/releases/tag/v0.1.0)

[Viikko 6](https://github.com/msha/ot-harjoitustyo/releases/tag/v0.2.0)

[Loppupalautus](https://github.com/msha/ot-harjoitustyo/releases/tag/v1.0.0)

## Ohjeet

1. Ohjelman asennus onnistuu komennolla
```bash
poetry install
```
2. Ohjelma käynnistyy komennolla
```bash
poetry run invoke start
```


## Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
