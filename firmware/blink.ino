void setup() {
  // Thiết lập chân LED_BUILTIN là đầu ra
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // Bật LED
  delay(1000);                       // Chờ 1 giây
  digitalWrite(LED_BUILTIN, LOW);    // Tắt LED
  delay(1000);                       // Chờ 1 giây
}
