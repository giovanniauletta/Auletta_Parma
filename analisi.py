import csv

FILE = "dati/spotify-canzoni.csv"

def carica(nomefile):
    dati = []
    scartate = 0
    with open(nomefile, "r", encoding="utf-8-sig", newline="") as f:
        for riga in csv.DictReader(f):
            try:
                riga = {k.strip(): v for k, v in riga.items()}
                riga["track_popularity"] = int(riga["track_popularity"])
                riga["duration_ms"] = int(riga["duration_ms"])
                riga["tempo"] = float(str(riga["tempo"]).replace(",", "."))
                riga["danceability"] = float(str(riga["danceability"]).replace(",", "."))
                dati.append(riga)
            except (ValueError, TypeError):
                scartate += 1
    return dati, scartate


def domanda1(dati):
    totale_righe = len(dati)
    
    
    id_diversi = set(riga["track_id"] for riga in dati)
    
    
    occorrenze = {}
    nomi_canzoni = {}
    for riga in dati:
        tid = riga["track_id"]
        occorrenze[tid] = occorrenze.get(tid, 0) + 1
        nomi_canzoni[tid] = f"{riga['track_artist']} - {riga['track_name']}"
    
   
    piu_playlist = [tid for tid, count in occorrenze.items() if count > 1]
    
    
    id_max = max(occorrenze, key=occorrenze.get)
    canzone_top = nomi_canzoni[id_max]
    max_playlist = occorrenze[id_max]
    
    return {
        "righe_totali": totale_righe,
        "canzoni_diverse": len(id_diversi),
        "in_piu_playlist": len(piu_playlist),
        "piu_presente": (canzone_top, max_playlist)
    }


def ms_a_minuti_secondi(ms):
    secondi_totali = ms // 1000
    minuti = secondi_totali // 60
    secondi = secondi_totali % 60
    return f"{minuti}:{secondi:02d}"

def domanda2(dati):
    canzoni_uniche = {}
    for riga in dati:
        tid = riga["track_id"]
        if tid not in canzoni_uniche:
            canzoni_uniche[tid] = {
                "nome": f"{riga['track_artist']} - {riga['track_name']}",
                "durata": riga["duration_ms"],
                "tempo": riga["tempo"]
            }
            
    durate = [c["durata"] for c in canzoni_uniche.values()]
    tempi = [c["tempo"] for c in canzoni_uniche.values()]
    
    min_durata = min(durate)
    max_durata = max(durate)
    media_durata_ms = sum(durate) / len(durate)
    
    
    piu_lunga = next(c["nome"] for c in canzoni_uniche.values() if c["durata"] == max_durata)
    piu_corta = next(c["nome"] for c in canzoni_uniche.values() if c["durata"] == min_durata)
    
    tempo_medio = round(sum(tempi) / len(tempi), 2)
    
    return {
        "minima": ms_a_minuti_secondi(min_durata),
        "massima": ms_a_minuti_secondi(max_durata),
        "media": ms_a_minuti_secondi(int(media_durata_ms)),
        "canzone_piu_lunga": piu_lunga,
        "canzone_piu_corta": piu_corta,
        "tempo_medio_bpm": tempo_medio
    }

def domanda3(dati):
    somma_pop = {}
    conteggi = {}
    for riga in dati:
        genere = riga["playlist_genre"]
        pop = riga["track_popularity"]
        somma_pop[genere] = somma_pop.get(genere, 0) + pop
        conteggi[genere] = conteggi.get(genere, 0) + 1
    tabella = []
    for genere in somma_pop:
        media_pop = round(somma_pop[genere] / conteggi[genere], 2)
        tabella.append([genere, conteggi[genere], media_pop])
    tabella.sort(key=lambda x: x[2], reverse=True)
    return tabella


def domanda_nostra(dati):
    ballabili = [riga["track_popularity"] for riga in dati if riga["danceability"] > 0.8]
    tutte_popolarita = [riga["track_popularity"] for riga in dati]
    media_ballabili = sum(ballabili) / len(ballabili) if ballabili else 0
    media_generale = sum(tutte_popolarita) / len(tutte_popolarita) if tutte_popolarita else 0
    return {
        "popolarita_media_ballabili": round(media_ballabili, 2),
        "popolarita_media_generale": round(media_generale, 2),
        "commento": "Le canzoni molto ballabili hanno popolarità superiore alla media." if media_ballabili > media_generale else "Non c'è una forte correlazione."
    }

def scrivi_risultati(nomefile, intestazione, tabella):
    with open(nomefile, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(intestazione)
        writer.writerows(tabella)

def main():
    dati, scartate = carica(FILE)
    print(f"Righe buone: {len(dati)}, scartate: {scartate}")
    print("Domanda 1:", domanda1(dati))
    print("Domanda 2:", domanda2(dati))
    tabella = domanda3(dati)
    scrivi_risultati("risultati.csv", ["Genere", "Numero_Righe", "Popolarita_Media"], tabella)
    print("Domanda nostra:", domanda_nostra(dati))

if __name__ == "__main__":
    main()