# Schnittstellen

 Wie kommunizieren **Mensch**, „**Cyber**“ und **Physik** miteinander?

### „Aus CPS-Sicht“

HCI vs M2M vs CPS

```mermaid
flowchart LR
  Mensch <--HCI--> Cyber
  subgraph CPS[Cyber-physisches System]
    subgraph Cyber[Cyber System]
      Computer1 <--M2M--> Computer2
    end
    subgraph PS[Physisches System]
      subgraph Schnittstelle
        Aktuator
        Sensor
      end
      subgraph I[Geräte / Anlagen]
        Maschine1
        Maschine2
      end
    end
    PS --messen--> Cyber
    Cyber --ansteuern--> PS
  end
  Mensch <-..-> PS
```

#### HCI
(**H**uman–**c**omputer **i**nteraction / **H**uman-**c**omputer **I**nterface)

-> **M**ensch-**M**aschine-**I**nteraktion / Benutzerschnittstelle

#### M2M
(Machine-to-Machine)

#### CPS
(**C**yber-**p**hysical **s**ystem)


### „Aus Sicht eines [Prozessors](https://de.wikipedia.org/wiki/Prozessor#Verarbeitung_eines_einzelnen_Befehls)“
(**Rechnerarchitektur** / **Prozessorarchitektur**)

> IHK-Zwischenprüfung Herbst 2018: Aufgabe 2.2

#### stark vereinfacht

```mermaid
flowchart LR
subgraph Computersystem
  Arbeitsspeicher
  subgraph Devices
    subgraph Peripherie
      Speichermedien
      Netzwerkkarten
      HID[Human Interface Device]
    end
    Controller
    Koprozessoren
  end
  subgraph Prozessor
    Bus <--> Register
    Bus <--> Rechenwerk <--> Register
    Bus <--> Steuerwerk <--> Register
    Steuerwerk <--> Rechenwerk
  end
end
Arbeitsspeicher <--> Bus
Devices <--> Bus
```

[![cpu](https://upload.wikimedia.org/wikipedia/commons/3/3a/ABasicComputer.svg)](https://en.wikipedia.org/wiki/Central_processing_unit#Structure_and_implementation)

#### detailierter

```mermaid
flowchart TB
  subgraph Motherboard[Motherboard / SoC]
    Arbeitsspeicher <--MMU--> Northbridge
    subgraph CPU-Chip
      Northbridge <--FSB--> Bus
      subgraph Prozessor-Kern
        Bus <--> Register
        Bus <--> Rechenwerk <--> Register
        Bus <--> Steuerwerk <--> Register
        Steuerwerk <--> Rechenwerk
      end
    end
    Northbridge <--DMI-->  Southbridge
  end
  subgraph Welt[Rest der Welt]
    subgraph Devices
      Device1
      Device2
      Device3
    end
  end
  Southbridge <--MMIO-->Device1 
  Southbridge <--PMIO--> Device2
  Register <--GPIO--> Device3
```

##### [SoC](https://de.wikipedia.org/wiki/System-on-a-Chip)
(**S**ystem-**o**n-a-**C**hip)

##### [FSB](https://de.wikipedia.org/wiki/Front_Side_Bus)
(**F**ront **S**ide **B**us)

##### [DMI](https://de.wikipedia.org/wiki/Direct_Media_Interface)
(**D**irect **M**edia **I**nterface)

##### [MMU](https://de.wikipedia.org/wiki/Memory_Management_Unit)
(**M**emory **M**anagement **U**nit)

##### [MMIO](https://de.wikipedia.org/wiki/Memory_Mapped_I/O)
(**M**emory-**m**apped **I**/**O**)

##### [PMIO](https://de.wikipedia.org/wiki/Memory_Mapped_I/O)
(**P**ort-**m**apped **I**/**O**)

##### [GPIO](https://de.wikipedia.org/wiki/GPIO)
(**G**eneral **P**urpose **I**nput/**O**utput)


> `lstopo -.txt`
>
> [Beispiel Skylake Microarchitectures](https://en.wikichip.org/wiki/intel/microarchitectures/skylake_(client)#Block_Diagram)

