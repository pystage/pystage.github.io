---
title: "Der Zombie läuft und redet"
description: "Ein erstes Projekt: eine Figur, die redet, läuft und mit der Tastatur gesteuert werden kann."
weight: 1
lead: "Ein Zombie, eine Bühne, ein paar Worte. Baue es in fünf kleinen Schritten."
translation_of: "projects/walk-and-talk.md"
source_hash: "0785cf5aa1198507"
---

Du brauchst PyStage. Wenn du es noch nicht hast, geh zuerst auf [Start](/start/).

In jedem Schritt bekommst du ein ganzes Programm. Tipp es ab (kopiere es nicht, Abtippen ist die beste Art zu lernen) und starte es. Ändere dann etwas und sieh, was passiert.

## Schritt 1: Ein Zombie auf der Bühne

```python {run=true}
from pystage.de import Bühne

bühne = Bühne()
zombie = bühne.füge_eine_figur_hinzu()

bühne.abspielen()
```

Du siehst ein Fenster mit einem Zombie in der Mitte. Er macht noch nichts. Schließe das Fenster, um das Programm zu beenden.

## Schritt 2: Lass ihn reden

Ein Skript ist eine Funktion. Wir verbinden sie mit „Wenn Programm startet“, wie die grüne Flagge in Scratch.

```python {run=true}
from pystage.de import Bühne

bühne = Bühne()
zombie = bühne.füge_eine_figur_hinzu()

def los(zombie):
    zombie.sage_für_sekunden("Hallo! Ich bin ein Zombie.", 2)
    zombie.sage("Komm, wir gehen spazieren.")

zombie.wenn_programm_startet(los)

bühne.abspielen()
```

`sage_für_sekunden` ist „sage Hallo für 2 Sekunden“. Danach sagt der Zombie das Nächste. Probiere eigene Worte aus.

## Schritt 3: Lass ihn laufen

```python {run=true}
from pystage.de import Bühne

bühne = Bühne()
zombie = bühne.füge_eine_figur_hinzu()

def los(zombie):
    zombie.sage_für_sekunden("Hallo! Ich bin ein Zombie.", 2)
    zombie.sage("Komm, wir gehen spazieren.")
    for i in range(20):
        zombie.gehe_schritte(10)
        zombie.warte_sekunden(0.1)
    zombie.sage("Puh, das war weit.")

zombie.wenn_programm_startet(los)

bühne.abspielen()
```

`for i in range(20):` wiederholt alles, was darunter steht, 20 mal, wie „wiederhole 20 mal“ in Scratch. Lass den Zombie weiter oder schneller laufen, indem du die 20, die 10 und die 0.1 änderst.

## Schritt 4: Steuere ihn mit der Tastatur

Jetzt bestimmst du, wohin der Zombie geht. Eine zweite Funktion wird mit der Taste „Leertaste“ verbunden und zwei weitere mit den Pfeiltasten.

```python {run=true}
from pystage.de import Bühne

bühne = Bühne()
zombie = bühne.füge_eine_figur_hinzu()

def los(zombie):
    zombie.sage_für_sekunden("Hallo! Ich bin ein Zombie.", 2)
    zombie.sage("Mit den Pfeiltasten läufst du, mit der Leertaste redest du.")

def nach_rechts(zombie):
    zombie.ändere_x_um(10)

def nach_links(zombie):
    zombie.ändere_x_um(-10)

def reden(zombie):
    zombie.sage_für_sekunden("Gehirne!", 1)

zombie.wenn_programm_startet(los)
zombie.wenn_taste_gedrückt_wird("Pfeil nach rechts", nach_rechts)
zombie.wenn_taste_gedrückt_wird("Pfeil nach links", nach_links)
zombie.wenn_taste_gedrückt_wird("Leertaste", reden)

bühne.abspielen()
```

## Schritt 5: Denken und drehen

Wir bauen eine Überraschung ein. Wenn du die Taste „t“ drückst, denkt der Zombie nach, dreht sich um und läuft zurück.

```python {run=true}
from pystage.de import Bühne

bühne = Bühne()
bühne.füge_bühnenbild_hinzu("grid")
zombie = bühne.füge_eine_figur_hinzu()

def los(zombie):
    zombie.sage_für_sekunden("Drück t für eine Überraschung.", 3)

def überraschung(zombie):
    zombie.denke_für_sekunden("Hmm, falsche Richtung.", 2)
    zombie.drehe_dich_nach_links_um_grad(180)
    for i in range(10):
        zombie.gehe_schritte(10)
        zombie.warte_sekunden(0.1)

zombie.wenn_programm_startet(los)
zombie.wenn_taste_gedrückt_wird("t", überraschung)

bühne.abspielen()
```

## Jetzt bist du dran

- Füge eine zweite Taste hinzu, mit der der Zombie hoch und runter geht.
- Ändere, was der Zombie sagt.
- Mit `zombie.setze_größe_auf(150)` wird der Zombie größer.

Weitere Projekte folgen. Wenn du etwas Schönes gebaut hast, zeig es uns auf [Discord](https://discord.gg/MSGrs3UCCz).
