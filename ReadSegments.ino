// Importamos la libreria general para comunicaciones por SPI
#include <SPI.h>
// Importamos la libreria para el modulo
#include <MFRC522.h>

// Los pines que usamos para conectarnos
#define RST_PIN 8          
#define SDA_PIN 9 // Tambien conocido como SS

MFRC522 mfrc522(SDA_PIN, RST_PIN);  

void setup() {
  // Iniciamos el Monitor serial
  Serial.begin(9600);
  
  // Iniciamos el SPI
  SPI.begin();
  
  // Iniciamos el modulo
  mfrc522.PCD_Init();
  
  Serial.println("Pase una tarjeta por el modulo para leerla...");
}

void loop() {
  // Si hay tarjeta nueva leida
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    
    // Mostramos informacion sobre la tarjeta por el Monitor serial
    mfrc522.PICC_DumpToSerial(&(mfrc522.uid));
  }
}
