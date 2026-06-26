/*
  ============================================================
  MOOD LED - Codice Arduino
  ============================================================
  Cosa fa questo programma:
  1. Aspetta che tu scriva il tuo mood sulla Serial Monitor
  2. Accende il LED RGB del colore corrispondente
  3. Manda un messaggio di conferma al computer (che Python leggerà)

  Hardware necessario:
  - Arduino Uno
  - LED RGB catodo comune (4 pin)
  - 3 resistenze da 220 ohm

  Collegamento LED RGB catodo comune:
  - Pin più lungo (GND/catodo) --> GND di Arduino
  - Pin R (rosso)  --> Resistenza 220Ω --> Pin 9
  - Pin G (verde)  --> Resistenza 220Ω --> Pin 10
  - Pin B (blu)    --> Resistenza 220Ω --> Pin 11
  ============================================================
*/

// --- DEFINIZIONE DEI PIN ---
// Usiamo pin PWM (quelli con il simbolo ~) per poter
// regolare la luminosità con valori da 0 a 255
const int PIN_ROSSO  = 9;
const int PIN_VERDE  = 10;
const int PIN_BLU    = 11;

// --- SETUP: viene eseguito UNA SOLA VOLTA all'avvio ---
void setup() {
  // Impostiamo i pin come OUTPUT (usciamo segnale verso il LED)
  pinMode(PIN_ROSSO, OUTPUT);
  pinMode(PIN_VERDE, OUTPUT);
  pinMode(PIN_BLU,   OUTPUT);

  // Avviamo la comunicazione seriale a 9600 baud
  // (deve essere lo stesso valore usato in Python!)
  Serial.begin(9600);

  // Messaggio di benvenuto
  Serial.println("=== MOOD LED PRONTO ===");
  Serial.println("Scrivi il tuo mood: felice, triste, arrabbiato,");
  Serial.println("rilassato, energico, romantico, ansioso, sorpreso");
  Serial.println("========================");

  // Spegniamo il LED all'avvio (tutti i colori a 0)
  impostaColore(0, 0, 0);
}

// --- LOOP: viene eseguito IN CONTINUAZIONE ---
void loop() {
  // Controlliamo se sono arrivati dati dalla porta seriale
  if (Serial.available() > 0) {

    // Leggiamo la stringa intera fino a quando l'utente preme INVIO
    String mood = Serial.readStringUntil('\n');

    // Rimuoviamo spazi e andiamo a capo residui
    mood.trim();

    // Convertiamo tutto in minuscolo per evitare errori
    // (es. "Felice" e "felice" vengono trattati uguale)
    mood.toLowerCase();

    Serial.print("Mood ricevuto: ");
    Serial.println(mood);

    // --- SELEZIONE DEL COLORE IN BASE AL MOOD ---
    // impostaColore(rosso, verde, blu) con valori da 0 a 255

    if (mood == "felice") {
      impostaColore(255, 200, 0);   // Giallo caldo
      Serial.println("MOOD:felice");

    } else if (mood == "triste") {
      impostaColore(0, 50, 200);    // Blu profondo
      Serial.println("MOOD:triste");

    } else if (mood == "arrabbiato") {
      impostaColore(255, 0, 0);     // Rosso acceso
      Serial.println("MOOD:arrabbiato");

    } else if (mood == "rilassato") {
      impostaColore(0, 200, 150);   // Verde acqua / turchese
      Serial.println("MOOD:rilassato");

    } else if (mood == "energico") {
      impostaColore(255, 80, 0);    // Arancione brillante
      Serial.println("MOOD:energico");

    } else if (mood == "romantico") {
      impostaColore(255, 20, 80);   // Rosa/magenta
      Serial.println("MOOD:romantico");

    } else if (mood == "ansioso") {
      impostaColore(180, 0, 255);   // Viola intenso
      Serial.println("MOOD:ansioso");

    } else {
      // Mood non riconosciuto
      impostaColore(255, 255, 255); // Bianco = "non so"
      Serial.println("Mood non riconosciuto. Prova con:");
      Serial.println("felice, triste, arrabbiato, rilassato,");
      Serial.println("energico, romantico, ansioso, sorpreso");
      Serial.println("MOOD:sconosciuto");
    }

    
  }
}

// --- FUNZIONE HELPER: imposta il colore del LED ---
// Riceve tre valori (0-255) per rosso, verde e blu
// analogWrite() usa PWM per simulare intensità variabile
void impostaColore(int r, int g, int b) {
  analogWrite(PIN_ROSSO, r);
  analogWrite(PIN_VERDE, g);
  analogWrite(PIN_BLU,   b);
}
