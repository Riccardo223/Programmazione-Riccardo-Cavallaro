#  Mood LED + Spotify — Guida Completa

## Cosa fa il progetto
La macchina tramite la teachable machine e la webcam del dispositivo riesce a capire il tuo mood, dopo averlo capito manda il codice python apre una playlist dedicata per il tuo mood su spotify e manda un segnale ad arduino che accende un led rgb del colore giusto in base alla tua emozione.

---

## <> Componenti necessari
| Componente | Quantità |
|---|---|
| Arduino Uno | 1 |
| LED RGB catodo comune (4 pin) | 1 |
| Resistenze 220Ω | 3 |
| Cavi jumper | ~6 |
| Breadboard | 1 |

---

##  Schema di collegamento LED RGB

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

---

##  Mappa mood → colori LED

| Mood | Colore LED | RGB |
|---|---|---|
| felice |  Giallo caldo | (255, 200, 0) |
| triste |  Blu profondo | (0, 50, 200) |
| arrabbiato |  Rosso acceso | (255, 0, 0) |
| rilassato |  Verde acqua | (0, 200, 150) |
| energico |  Arancione | (255, 80, 0) |
| romantico |  Rosa/Magenta | (255, 20, 80) |
| ansioso |  Viola intenso | (180, 0, 255) |
| sorpreso |  Ciano | (0, 255, 255) |

---



---

##  Struttura file
```
PROGETTO INGENGNERIA EX3 2025/2026/
├── mood_arduino.ino   → Codice per Arduino (C++)
|__ Keras_model.h5
|__ Labels.txt
|
├── mood_spotify.py    → Codice per il computer (Python)
└── README.md          → Questa guida
```
