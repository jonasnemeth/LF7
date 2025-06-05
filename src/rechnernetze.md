# Rechnernetze

## [Topologien](https://de.wikipedia.org/wiki/Topologie_(Rechnernetz))

> Welche Topologien kennt ihr? Wo finden sie Anwendung?

> Welche Vor- und Nachteile haben verschiedene Topologien?

![topologien](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/NetzwerkTopologien.svg/1920px-NetzwerkTopologien.svg.png)

## Bussysteme

> Für welche Einsatzzwecke sind Bussysteme attraktiv? Warum?

![chipset](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Chipset_schematic.svg/800px-Chipset_schematic.svg.png)

```mermaid
graph TB
  Bussysteme --> On-Chip[On-Chip Bus]
  Bussysteme --> Inter-Chip[Inter-Chip Bus]
  Inter-Chip -..-> FSB[Front Side Bus]
  Inter-Chip -..-> DMI[Direct Media Interface]
  Bussysteme --> Peripheriebus
  Peripheriebus -..-> intern
  intern -..-> PCI
  intern -..-> sata[Serial ATA]
  intern -..-> I2C
  intern -..-> SPI
  Peripheriebus -..-> extern
  extern -..-> seriell[Serielle Schnittstelle]
  extern -..-> parallel[Parallele Schnittstelle]
  extern -..-> USB
  Bussysteme --> Feldbus -..-> CAN[z.B. CAN]
```

### [SPI](https://de.wikipedia.org/wiki/Serial_Peripheral_Interface)
(**S**erial **P**eripheral **I**nterface)

![SPI](https://upload.wikimedia.org/wikipedia/commons/f/fc/SPI_three_slaves.svg)

* 4 Signalleitungen
  * SCLK = Serial Clock
  * MOSI / PICO = Master Out / Slave In bzw. Peripheral In / Controller Out
  * MISO / POCI = Master In / Slave Out bzw. Peripheral Out / Controller In
  * SS / CS = Slave Select bzw. Chip Select

### [I²C](https://de.wikipedia.org/wiki/I%C2%B2C)
![I²C](https://upload.wikimedia.org/wikipedia/commons/0/04/I2C_controller-target.svg)

* Master-Slave-Bus
* zwei Signalleitungen
  * SCL = Serial Clock
  * SDA = Serial Data

* 7-bit Adressraum

> Beispiel: [I2C-LCD-Display](https://wokwi.com/projects/359400194112248833)

#### [Anwendungsfälle](pi.md#serielle-protokolle)
