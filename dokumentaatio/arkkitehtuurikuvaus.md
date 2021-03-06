# Arkkitehtuurikuvaus

## Rakenne

Ohjelma käyttää `gui` pakkausta käyttöliittymän toteuttamiseen, `code` sisältää koodin käsittelyyn sisältyvän logiikan, `fileops` tiedon tallentamiseen sekä lukemiseen liittyvät asiat ja database sisältää tietokannan käsittelyn.

![Rakenne](./kuvat/sovellus.png)

## Käyttöliittymä

Ohjelma sisältää graafisen käyttöliittymän. Käyttöliittymä sisältää päänäkymän, sekä päänäkymästä aukeavia ikkunoita, joita käytetään toimintojen syöttöön.

Päänäkymästä käyttäjä näkee työstettävän HTML sisällön, sekä painikkeet eri toimintojen käyttämiseen. Päänäkymän ylälaidasta löytyy pudotusvalikko ohjelman sulkemiseen, sekä tiedoston työn tallentamiseen. 

Työkalupainikkeista aukeaa työkaluun liittyvä ikkuna, kuten suoran koodin syöttäminen code-ikkunasta. (Täydennetään tähän työkalujen kuvauksia, kun niitä valmistuu)

## Sovelluslogiikka

### Kuvan lisääminen koodiin
Käyttäjä painaa GUI:sta kuvanlisäysnappia, joka avaa käyttöliittymään uuden ikkunan kuvan lisäämistä varten. Ikkunasta käyttäjä voi joko syöttää suoraan polun käsin tai käyttää selausta toimintoa ja hakea kuvan hakemistoista. Ohjelma tämän jälkeen lisää kuvan näkymään ja sallii tiedoston tallentamisen

![Rakenne](./kuvat/kuvan_lisaaminen.png)

## Tiedon tallennus

Sovellus käyttää `fileops` luokkaa tietojen tallentamiseen. Sovellus muodostaa käyttäjän haluamalla nimellä html-tiedoston työstettävästä sisällöstä.

## Tiedon luku

Sovellus käyttää `fileops` luokkaa myös tietojen lukemiseen. Sovellus hakee käyttäjän määrittämän tiedoston ja parsii siitä työstettävän pohjan muokattavaksi