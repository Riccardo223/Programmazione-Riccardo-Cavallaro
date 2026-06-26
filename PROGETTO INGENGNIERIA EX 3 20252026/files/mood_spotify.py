"""
============================================================
MOOD LED + SPOTIFY + TEACHABLE MACHINE 
============================================================

1. Carica il modello di Teachable Machine 
2. Apre la webcam e riconosce il tuo gesto in tempo reale
3. Quando è abbastanza sicuro del gesto, manda il mood ad Arduino
4. Apre la playlist Spotify corrispondente

File necessari nella stessa cartella:
- keras_model.h5  (scaricato da Teachable Machine)
- labels.txt      (scaricato da Teachable Machine)
============================================================
"""

import serial
import webbrowser
import time
import sys
import cv2
import numpy as np
from keras.models import load_model

# ============================================================
# CONFIGURAZIONE
# ============================================================

PORTA_SERIALE = "COM8"       # <-- cambia con la tua porta
BAUD_RATE = 9600

MODELLO_PATH = "files/keras_model.h5"
LABELS_PATH  = "files/labels.txt"

# Soglia di confidenza: il modello deve essere almeno all'70%
# sicuro prima di mandare il segnale. 
CONFIDENZA_MINIMA = 0.70

# Secondi da aspettare prima di poter cambiare mood.
# Evita che cambi playlist ogni mezzo secondo!
COOLDOWN_SECONDI = 5

# ============================================================
# PLAYLIST SPOTIFY 
# ============================================================

PLAYLIST = {
    "felice":      {"link": "https://open.spotify.com/playlist/1Un5RNdck0Hj14AKFv9UtW?si=c6f45099873341f7"},
    "triste":      {"link": "https://open.spotify.com/playlist/0XEXbV7uyGRq3VNrFbYgzv?si=fceff5587dac4eab"},
    "arrabbiato":  {"link": "https://open.spotify.com/playlist/4rg0tOWdkT8ScqekiYQ4tQ?si=4bf4a4d6578e4507"},
    "rilassato":   {"link": "https://open.spotify.com/playlist/5JuzL74hX4M2Sj0exO5Vjc?si=28fdd88fa8494a09"},
    "energico":    {"link": "https://open.spotify.com/playlist/6Wfqe5yBg1QZgJrNKKtR0A?si=dd2225973446486d"},
    "romantico":   {"link": "https://open.spotify.com/playlist/7CgldbLwy46cuJGBuQVuvE?si=eaf94defaad24933"},
    "ansioso":     {"link": "https://open.spotify.com/playlist/3gFEzWh6YVZq5YtTVg6RKQ?si=1c8fe48c73404c14"},
}

# ============================================================
# FUNZIONI 
# ============================================================

def apri_spotify(mood):
    if mood in PLAYLIST:
        print(f"  Apro Spotify per mood: {mood}...")
        webbrowser.open(PLAYLIST[mood]["link"])
    else:
        print(f"  Nessuna playlist per il mood '{mood}'")


def connetti_arduino():
    try:
        print(f"Connessione ad Arduino su {PORTA_SERIALE}...")
        arduino = serial.Serial(PORTA_SERIALE, BAUD_RATE, timeout=1)
        print("⏳ Attendo che Arduino si avvii (2 secondi)...")
        time.sleep(2)
        print("Connesso ad Arduino!\n")
        return arduino
    except serial.SerialException as e:
        print(f"\nERRORE: Impossibile connettersi ad Arduino!")
        print(f"  Dettaglio: {e}")
        return None

def manda_ad_arduino(arduino, mood):
    messaggio = mood + "\n"
    arduino.write(messaggio.encode('utf-8'))
    time.sleep(0.5)
    while arduino.in_waiting > 0:
        risposta = arduino.readline().decode('utf-8', errors='ignore').strip()
        if risposta:
            print(f"  [Arduino] {risposta}")


# ============================================================
# FUNZIONI - Teachable Machine
# ============================================================

def carica_modello():
    """Carica il modello .h5 e le etichette dal file labels.txt"""
    print("Carico il modello di Teachable Machine...")
    modello = load_model(MODELLO_PATH, compile=False)

    with open(LABELS_PATH, "r") as f:
        # Ogni riga è tipo "0 felice", "1 triste", ecc.
        # Prendiamo solo la seconda parola (il nome del mood)
        labels = [riga.strip().split(" ")[1] for riga in f.readlines()]

    print(f"Modello caricato! Gesti riconosciuti: {labels}\n")
    return modello, labels


def prepara_immagine(frame):
    """
    Ridimensiona e normalizza il frame della webcam
    nel formato che si aspetta Teachable Machine (224x224).
    """
    immagine = cv2.resize(frame, (224, 224))
    immagine = np.asarray(immagine, dtype=np.float32).reshape(1, 224, 224, 3)
    immagine = (immagine / 127.5) - 1  # normalizzazione standard di TM
    return immagine


# ============================================================
# LOOP PRINCIPALE CON WEBCAM
# ============================================================

def ciclo_webcam(arduino, modello, labels):
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not webcam.isOpened():
        print("ERRORE: impossibile aprire la webcam!")
        return

    print("Webcam avviata! Fai un gesto con la mano.")
    print("Premi Q per uscire.\n")

    mood_precedente = ""
    ultimo_cambio   = 0  # timestamp dell'ultimo mood inviato

    while True:
        ret, frame = webcam.read()
        if not ret:
            print("Errore nella lettura della webcam.")
            break

        # --- Previsione ---
        immagine   = prepara_immagine(frame)
        previsione = modello.predict(immagine, verbose=0)  # verbose=0 = niente spam in console
        indice     = np.argmax(previsione)
        confidenza = previsione[0][indice]
        mood       = labels[indice]

        # --- Testo da mostrare sulla finestra webcam ---
        colore = (0, 255, 0) if confidenza >= CONFIDENZA_MINIMA else (0, 165, 255)
        # verde se sicuro, arancione se incerto
        testo = f"{mood}  {confidenza*100:.0f}%"
        cv2.putText(frame, testo, (10, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, colore, 2)

        # Barra del cooldown (quanto manca prima che possa cambiare mood)
        tempo_passato  = time.time() - ultimo_cambio
        cooldown_rimasto = max(0, COOLDOWN_SECONDI - tempo_passato)
        if cooldown_rimasto > 0:
            cv2.putText(frame, f"Prossimo cambio: {cooldown_rimasto:.1f}s",
                        (10, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv2.imshow("MOOD LED + SPOTIFY", frame)

        # --- Manda il segnale solo se: ---
        # 1. Il modello è abbastanza sicuro
        # 2. Il mood è cambiato rispetto all'ultimo inviato
        # 3. È passato abbastanza tempo dall'ultimo invio (cooldown)
        if (confidenza >= CONFIDENZA_MINIMA
                and mood != mood_precedente
                and tempo_passato >= COOLDOWN_SECONDI):

            print(f"\nMood riconosciuto: {mood} ({confidenza*100:.0f}% di sicurezza)")
            manda_ad_arduino(arduino, mood)
            apri_spotify(mood)

            mood_precedente = mood
            ultimo_cambio   = time.time()

        # Premi Q per uscire
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\nUscita richiesta.")
            break

    webcam.release()
    cv2.destroyAllWindows()


# ============================================================
# AVVIO DEL PROGRAMMA
# ============================================================

if __name__ == "__main__":
    print("=== MOOD LED + SPOTIFY + TEACHABLE MACHINE ===\n")

    # 1. Collega Arduino
    arduino = connetti_arduino()
    if not arduino:
        print("Impossibile avviare senza Arduino.")
        sys.exit(1)

    # 2. Carica il modello
    modello, labels = carica_modello()

    # 3. Avvia la webcam
    try:
        ciclo_webcam(arduino, modello, labels)
    finally:
        arduino.close()
        print("Porta seriale chiusa.")