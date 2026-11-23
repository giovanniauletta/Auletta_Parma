# Analisi di un dataset reale: canzoni su Spotify

Questo progetto analizza un file CSV con 32.833 righe di canzoni prese da
playlist di sei generi (pop, rap, rock, latin, r&b ed edm). I dati sono del
2020 e arrivano dall'API di Spotify. Per leggere il file abbiamo usato solo
il modulo `csv` di Python.

## Come si esegue

Per prima cosa metti `spotify-canzoni.csv` nella cartella `dati`. Poi, dalla
cartella del progetto, lancia `python3 analisi.py`. Il programma stampa le
risposte alle domande e crea il file `risultati.csv`.

## Risultati

**Domanda 1.** Il file contiene 32.833 righe, ma le canzoni diverse sono
28.356 (le abbiamo contate con `track_id`). Ben 3.166 canzoni compaiono in più
di una playlist, e quella che compare più spesso è "The Chainsmokers - Closer
(feat. Halsey)", presente in 10 playlist.

**Domanda 2.** Contando ogni canzone una volta sola, la durata minima è 0:04,
la massima 8:37 e la media 3:46. La più lunga è "Anuel AA - 47 - Remix", la
più corta è "DREAMS COME TRUE - Hi, How're You Doin'?". Il tempo medio è di
120,96 battiti al minuto.

**Domanda 3.** La classifica dei generi per popolarità media, con il numero di
righe di ciascuno, è nel file `risultati.csv`. In cima c'è il pop con 47,74,
seguito dal latin con 47,03, mentre all'ultimo posto troviamo l'edm con 34,83.

**La nostra domanda.** Ci siamo chiesti se le canzoni più ballabili (con
danceability sopra 0,8) siano anche le più popolari. La loro popolarità media
è 45,49, contro 42,48 di tutte le canzoni. La differenza è di circa 3 punti su
100, quindi più che una relazione forte vediamo una leggera tendenza.

## Scelte e problemi incontrati

Le righe con dati che non si riescono a convertire vengono scartate, ma nel
nostro caso non ce n'era nessuna. Per la durata e il tempo medio abbiamo
contato ogni canzone una volta sola: la stessa canzone compare in più playlist
e, se la contassimo ogni volta, peserebbe più delle altre nella media.