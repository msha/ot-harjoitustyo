# Arkkitehtuurikuvaus

## Rakenne

Ohjelma käyttää _gui_ pakkausta käyttöliittymän toteuttamiseen, _code_ sisältää sisäisen logiikan ja _fileops_ tiedon tallentamiseen liittyvät asiat.

![Rakenne](./kuvat/sovellus.png)

## Käyttöliittymä

Ohjelma sisältää graafisen käyttöliittymän. Käyttöliittymä sisältää päänäkymän, sekä päänäkymästä aukeavia ikkunoita, joita käytetään toimintojen syöttöön.

Päänäkymästä käyttäjä näkee työstettävän HTML sisällön, sekä painikkeet eri toimintojen käyttämiseen. Päänäkymän ylälaidasta löytyy pudotusvalikko ohjelman sulkemiseen, sekä tiedoston työn tallentamiseen. 

Työkalupainikkeista aukeaa työkaluun liittyvä ikkuna, kuten suoran koodin syöttäminen code-ikkunasta. (Täydennetään tähän työkalujen kuvauksia, kun niitä valmistuu)

## Sovelluslogiikka

WIP

## Tiedon tallennus

Sovellus käyttää `fileops` luokkaa tietojen tallentamiseen. Sovellus muodostaa käyttäjän haluamalla nimellä html-tiedoston työstettävästä sisällöstä.