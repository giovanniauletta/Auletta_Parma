import csv

FILE = "dati/nome-del-vostro-file.csv"

def carica(nomefile):
    """
    Legge il file CSV di Spotify, converte i campi numerici principali 
    e restituisce la lista delle righe valide e quelle scartate.
    """
    dati = []
    scartate = 0
    with open(nomefile, "r", encoding="utf-8", newline="") as f:
        for riga in csv.DictReader(f):
            try:
                # Conversione dei campi numerici utili per le domande
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
    
    # Set per contare i track_id unici
    id_diversi = set(riga["track_id"] for riga in dati)
    
    # Dizionario per contare in quante playlist/righe compare ciascun track_id
    occorrenze = {}
    nomi_canzoni = {} # Per ricordarci il titolo e l'artista
    for riga in dati:
        tid = riga["track_id"]
        occorrenze[tid] = occorrenze.get(tid, 0) + 1
        nomi_canzoni[tid] = f"{riga['track_artist']} - {riga['track_name']}"
    
    # Canzoni che compaiono in più di una playlist (occorrenze > 1)
    piu_playlist = [tid for tid, count in occorrenze.items() if count > 1]
    
    # Trovare quella che compare in più playlist di tutte
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
    """Converte i millisecondi nel formato stringa mm:ss"""
    secondi_totali = ms // 1000
    minuti = secondi_totali // 60
    secondi = secondi_totali % 60
    return f"{minuti}:{secondi:02d}"

def domanda2(dati):
    # Salviamo ogni canzone una volta sola usando un dizionario con chiave track_id
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
    
    # Trovare la più lunga e la più corta
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
    """Risponde alla domanda 3. Restituisce la tabella
    che finirà in risultati.csv: una lista di righe."""
    return []


def domanda_nostra(dati):
    """La domanda inventata dal gruppo."""
    return None


def scrivi_risultati(nomefile, intestazione, tabella):
    """Scrive la tabella in un CSV con csv.writer."""
    pass


def main():
    dati, scartate = carica(FILE)
    print(f"Righe buone: {len(dati)}, scartate: {scartate}")
    print("Domanda 1:", domanda1(dati))
    print("Domanda 2:", domanda2(dati))
    tabella = domanda3(dati)
    scrivi_risultati("risultati.csv", ["colonna1", "colonna2"], tabella)
    print("Domanda nostra:", domanda_nostra(dati))


main()