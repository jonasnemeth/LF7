# MQTT

„**M**essage **Q**ueuing **T**elemetry **T**ransport“

* Publish/Subscribe

* Clients können ein „Topic“ abonnieren
  * TCP-Verbindung wird offen gehalten
  * Server kann Clients über bestehende Verbindung über Updates informieren

```bash
mosquitto  ## start the broker
mosquitto_sub -h 127.0.0.1 -p 1883 -u fi -P geheim -t fi/buttonGPIO2
mosquitto_pub -h 127.0.0.1 -p 1883 -u fi -P geheim -t fi/buttonGPIO2 -m '1'
```
