from flask import Flask,  render_template, request, url_for
from funzioni import (
    conta_parole, conta_sillabe, conta_sillabe_verso,
    conta_sinalefe, pulisci_testo, geolocalizza, regione_to_class
)
from funzioni import REGIONI_POESIA
from collections import Counter

app = Flask(__name__)  # Crea l'app Flask


# pagina principale che risponde ai metodi sia a GET che POST
@app.route("/", methods=['GET', 'POST'])
def pagina_iniziale():
    # Mostra semplicemente la pagina iniziale con il form per inserire la poesia
    return render_template("index.html")


# Pagina per l'analisi base della poesia
@app.route("/analizzazione", methods=['POST'])
def pagina_2():
    poesia = request.form["poesia"]  # Prende il testo della poesia dal form inviato

    parole = pulisci_testo(poesia)  # Pulisce il testo: minuscole, rimuove punteggiatura, split in parole

    conteggio = conta_parole(poesia)  # Conta il numero totale di parole

    conta = Counter(parole)  # Conta la frequenza di ogni parola

    # Filtra solo le parole che appaiono più di una volta
    risultati = {parola: freq for parola, freq in conta.items() if freq > 1}

    # Calcola il totale di sillabe di tutte le parole
    sillabe_totali = sum(conta_sillabe(p) for p in parole)

    righe = poesia.split('\n')  # Divide la poesia in versi (righe)
    versi_evidenziati = []

    # Per ogni verso calcola le sillabe corrette
    for riga in righe:
        if not riga:
            continue  # Salta righe vuote
        numero_sillabe = conta_sillabe_verso(riga)
        testo_verso = f"{riga}  ({numero_sillabe} sillabe)"

        # Se è un verso endecasillabo (11 sillabe) evidenzialo con <mark>
        if numero_sillabe == 11:
            versi_evidenziati.append(f"<mark>{testo_verso}</mark>")
        else:
            versi_evidenziati.append(testo_verso)

    # Ritorna la pagina con i dati elaborati
    return render_template(
        "index_analizzato.html",
        poesia=poesia,
        conteggio=conteggio,
        sillabe_totali=sillabe_totali,
        poesia_evidenziata="<br>".join(versi_evidenziati),  # Versi con evidenziazioni e a capo in HTML
        risultati=risultati  # parole ripetute con frequenza
    )


# Rotta per l'analisi geografica della poesia (geolocalizzazione in base a parole chiave)
@app.route("/analizzazione2", methods=['POST'])
def pagina_3():
    poesia = request.form["poesia"]  # Prende il testo della poesia

    parole = pulisci_testo(poesia)  # Pulisce il testo in lista di parole

    regione, punteggi = geolocalizza(parole)  # Determina la regione più probabile e punteggi

    # Se nessuna regione è stata trovata, metti valori di default
    if regione == "Nessuna regione trovata":
        punteggi_massimi = 0
        classe_regione_css = "generica"  # Classe CSS generica per stile neutro
    else:
        punteggi_massimi = punteggi[regione]  # Numero di parole corrispondenti alla regione
        classe_regione_css = regione_to_class(regione)  # Converte nome regione in nome classe CSS

    # Ritorna la pagina con i risultati della geolocalizzazione
    return render_template(
        "index_analizzato2.html",
        regione=classe_regione_css,  # Passa la classe CSS per lo stile dinamico
        regione_nome=regione,  # Passa il nome originale della regione per mostrarlo a video
        punteggi_massimi=punteggi_massimi,  # Quante parole sono state riconosciute per la regione
        poesia=poesia
    )


if __name__ == "__main__":
    app.run(debug=True)  # Avvia il server Flask in modalità debug per facilitare lo sviluppo
