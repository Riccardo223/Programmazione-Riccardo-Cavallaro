from collections import Counter

import re

# Dizionario che associa regioni italiane ad autori e alle parole chiave tipiche delle loro poesie
REGIONI_POESIA = {
    "Liguria": {
        "Eugenio Montale": [
            "macchia", "cicale", "gabbiani", "fuscelli", "terra", "bruciata",
            "roccia", "spiaggia", "sale", "riva", "mare", "onde",
            "vento", "ponente", "aspro", "calura", "arsura", "luminoso", "pallido",
            "ulivi", "limoni", "corbezzolo", "gabbiani", "cicale",
            "insetti", "fuscelli",
            "meriggiare", "assorto", "silenzio", "solitudine", "ombre", "calma",
            "sospeso", "soffio",
            "muraglia", "scorza", "crinale", "montagna", "collina",
            "ponte", "paese", "vicoli", "sentiero",
        ]
    },
    "Veneto": {
        "Francesco Petrarca": [
            "acque", "fresche", "chiare", "dolci", "fonti", "ruscello", "ombra",
            "pini", "allori", "faggi", "selva", "bosco", "colline", "monti",
            "aria", "vento", "sera", "giro", "ombra", "fronde",
            "pace", "dolcezza", "sereno", "riposo", "piacevole", "rugiada",
            "lieve", "tranquillo", "silenzio",
            "amor", "core", "dolce", "gentile", "spirto", "lume", "ardore",
            "vita", "pianto", "piace",
            "seno", "bel", "fior", "tempo", "tempo", "perché", "fugge",
            "ombra", "vento", "calma",
        ]
    },
    "Toscana": {
        "Francesco Petrarca": [
            "dolore", "pianto", "lacrime", "amore", "passione", "tristezza","rimpianto", "piacevolezza", "sospiri", "angoscia", "danno", "affanni",
            "rime", "suono", "arte", "versi", "lingua", "parole", "canto","spirto", "core", "ardore", "fiamma", "ardente", "foco",
            "arbor", "foglia", "fiore", "ombre", "vento", "sera", "notte","tempo", "stagioni", "giro", "cielo", "stelle",
            "voi", "auditor", "popolo", "amici", "spiriti","vita", "morte", "speme", "sogno", "desio", "piacer", "fuga","dolcezza", "inganno"
        ]
    },
    "Friuli-Venezia Giulia": {
        "Umberto Saba": [
            "modesta", "domestica", "onesta", "cucina", "armadio", "pentola", "scodella",
            "paese", "sedia", "piatti", "mestiere", "gatto", "mucca", "pollastra", "asino",
            "ombra", "grigio", "giorno", "piccolo", "tetto", "cortile", "pavimento",
            "famiglia", "casa", "moglie", "vita", "donna", "serva", "compagna",
            "animali", "povero", "umile", "fedele", "silenziosa", "abitare", "stanza",
            "quartiere", "strada", "Trieste", "nord", "città", "matrimonio", "marito",
        ]
    }
}

# Funzione che conta il numero totale di parole in una poesia
def conta_parole(poesia):
    # Trova tutte le parole nel testo (sequenze di caratteri alfanumerici)
    word = re.findall(r'\b\w+\b', poesia.lower())
    return len(word)

# Funzione che conta il numero di sillabe in una singola parola
def conta_sillabe(parola):
    # Cerca sequenze consecutive di vocali (anche accentate) nella parola
    gruppi_vocali = re.findall(r'[aeiouàèéìòù]+', parola.lower(), re.IGNORECASE)
    # Il numero di gruppi vocalici corrisponde al numero di sillabe
    return len(gruppi_vocali)

# Funzione che conta il numero di sinalefe in un ver00000000000000so
def conta_sinalefe(verso):
    # Cerca coppie di vocali separate da uno o più spazi che possono formare sinalefe
    pattern = r'([aeiouàèéìòù])\s+([aeiouàèéìòù])'
    matches = re.findall(pattern, verso.lower())
    # Conta quante volte si verifica la sinalefe
    return len(matches)

# Funzione che conta il numero corretto di sillabe in un verso, tenendo conto della sinalefe
def conta_sillabe_verso(verso):
    # Rimuove tutti i caratteri che non sono lettere o spazi (pulizia del verso)
    verso_pulito = re.sub(r'[^a-zàèéìòù\s]', '', verso)
    # Normalizza gli spazi multipli in uno solo
    verso_pulito = re.sub(r'\s+', ' ', verso_pulito)
    # Divide il verso in parole
    parole = verso_pulito.split()
    # Conta le sillabe meccaniche come somma delle sillabe di ogni parola
    sillabe_meccaniche = sum(conta_sillabe(p) for p in parole)
    # Conta quante sinalefi ci sono nel verso
    sinalefi = conta_sinalefe(verso_pulito)
    # La conta finale delle sillabe tiene conto delle sinalefi (sillabe meccaniche - sinalefi)
    sillabe_corrette = max(sillabe_meccaniche - sinalefi, 1)  # almeno 1 sillaba per verso
    return sillabe_corrette

# Funzione per ripulire il testo da caratteri speciali e dividerlo in parole
def pulisci_testo(poesia):
    testo_ripulito = poesia.lower()
    # Rimuove tutto ciò che non è una lettera o spazio
    testo_ripulito = re.sub(r'[^a-zàèéìòù\s]', '', testo_ripulito)
    # Normalizza gli spazi multipli
    testo_ripulito = re.sub(r'\s+', ' ', testo_ripulito)
    # Divide in parole e restituisce la lista
    parole = testo_ripulito.split()
    return parole

# Funzione che, data una lista di parole, determina la regione italiana più probabile a cui appartiene la poesia
def geolocalizza(parole):
    # Inizializza un dizionario con punteggi per ogni regione
    punteggi = {"Liguria": 0, "Toscana": 0, "Veneto": 0, "Friuli-Venezia Giulia": 0}
    parole = [p.lower() for p in parole]  # Assicura che tutte le parole siano minuscole per confronto
    # Scorre ogni regione e autore, e conta quante parole della poesia sono presenti nelle parole chiave
    for regione, autori in REGIONI_POESIA.items():
        for autore, parole_chiave in autori.items():
            for parola in parole:
                if parola in parole_chiave:
                    punteggi[regione] += 1
    print("Debug punteggi:", punteggi)  # Stampa i punteggi per debug
    # Se nessuna parola corrisponde a nessuna regione, ritorna messaggio di nessuna corrispondenza
    if all(p == 0 for p in punteggi.values()):
        return "Nessuna regione trovata", punteggi

    # Seleziona la regione con il punteggio più alto
    regione_probabile = max(punteggi, key=punteggi.get)
    return regione_probabile, punteggi

# Funzione che trasforma il nome di una regione in una stringa formattata adatta per una classe CSS o simile
def regione_to_class(regione):
    # Trasforma tutto in minuscolo e sostituisce gli spazi con trattini
    return regione.lower().replace(" ", "-")
