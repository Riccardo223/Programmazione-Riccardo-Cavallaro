# 🎭 Mood LED + Spotify — Guida Completa

## Cosa fa il progetto
Scrivi il tuo **mood** nella Serial Monitor di Arduino → il **LED RGB** si illumina del colore giusto → **Spotify** apre automaticamente la playlist perfetta per come ti senti.

---

## 🔧 Componenti necessari
| Componente | Quantità |
|---|---|
| Arduino Uno | 1 |
| LED RGB catodo comune (4 pin) | 1 |
| Resistenze 220Ω | 3 |
| Cavi jumper | ~6 |
| Breadboard | 1 |

---

## 🔌 Schema di collegamento LED RGB

```
LED RGB (catodo comune) — 4 pin, il più lungo è GND

        R    GND   G    B
        |     |    |    |
        |     |    |    |
    [220Ω]   |  [220Ω] [220Ω]
        |     |    |    |
      Pin9  GND  Pin10 Pin11
     Arduino      Arduino
```

**In pratica:**
- **Pin più lungo (GND/catodo)** → GND di Arduino (riga blu della breadboard)
- **Pin R** → Resistenza 220Ω → **Pin 9** di Arduino
- **Pin G** → Resistenza 220Ω → **Pin 10** di Arduino  
- **Pin B** → Resistenza 220Ω → **Pin 11** di Arduino

> ⚠️ Le resistenze sono obbligatorie! Senza di esse il LED si brucia.

---

## 🎨 Mappa mood → colori LED

| Mood | Colore LED | RGB |
|---|---|---|
| felice | 🟡 Giallo caldo | (255, 200, 0) |
| triste | 🔵 Blu profondo | (0, 50, 200) |
| arrabbiato | 🔴 Rosso acceso | (255, 0, 0) |
| rilassato | 🩵 Verde acqua | (0, 200, 150) |
| energico | 🟠 Arancione | (255, 80, 0) |
| romantico | 🩷 Rosa/Magenta | (255, 20, 80) |
| ansioso | 🟣 Viola intenso | (180, 0, 255) |
| sorpreso | 🩵 Ciano | (0, 255, 255) |

---

## 💻 Installazione

### 1. Libreria Python necessaria
Apri il terminale/prompt dei comandi e digita:
```bash
pip install pyserial
```

### 2. Carica il codice su Arduino
1. Apri **Arduino IDE**
2. Apri il file `mood_arduino.ino`
3. Seleziona: **Strumenti → Scheda → Arduino Uno**
4. Seleziona: **Strumenti → Porta** (prendi nota della porta, es. COM3)
5. Clicca il pulsante **Carica** (freccia →)

### 3. Trova la tua porta seriale
- **Windows**: Gestione dispositivi → Porte COM (es. `COM3`)
- **Mac**: `/dev/tty.usbmodem...` oppure `/dev/ttyACM0`
- **Linux**: `/dev/ttyACM0` oppure `/dev/ttyUSB0`

### 4. Modifica la porta nel codice Python
Apri `mood_spotify.py` e cambia questa riga:
```python
PORTA_SERIALE = "COM3"  # <-- metti la tua porta qui
```

### 5. (Opzionale) Personalizza le playlist
Nel file Python trovi il dizionario `PLAYLIST`.
Per ogni mood puoi mettere il link alla tua playlist preferita:
1. Apri Spotify
2. Vai sulla playlist
3. Clicca `...` → Condividi → Copia link alla playlist
4. Incolla il link nel codice

---

## ▶️ Come usare il progetto

1. Collega Arduino via USB
2. **Chiudi** la Serial Monitor di Arduino IDE (se è aperta)
3. Lancia il programma Python:
   ```bash
   python mood_spotify.py
   ```
4. Scrivi il tuo mood nella Serial Monitor (o in qualsiasi terminale seriale)
5. Premi **INVIO**
6. Il LED si accende + Spotify apre la playlist! 🎉

---

## 🐛 Problemi comuni

| Problema | Soluzione |
|---|---|
| `SerialException: could not open port` | Chiudi Arduino IDE Serial Monitor, controlla la porta COM |
| Il LED non si accende | Controlla i collegamenti, verifica che sia catodo comune |
| Spotify non si apre | Controlla che Spotify sia installato, o si aprirà nel browser |
| Il mood non viene riconosciuto | Scrivi tutto in minuscolo, senza spazi extra |
| Colori sbagliati | Se R e B sono invertiti, scambia i pin 9 e 11 |

---

## 📁 Struttura file
```
mood_led/
├── mood_arduino.ino   → Codice per Arduino (C++)
├── mood_spotify.py    → Codice per il computer (Python)
└── README.md          → Questa guida
```
