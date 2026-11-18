---
title: "Start"
menu_title: "Start"
description: "Installiere Python und PyStage und starte dein erstes Programm, Schritt für Schritt."
nav: kids
weight: 2
lead: "Installiere Python und PyStage und starte dann dein erstes Programm. Das dauert etwa zehn Minuten."
translation_of: "start.md"
source_hash: "12cdd4360aecab6b"
---

## Was du brauchst

Du brauchst einen Computer mit Windows, macOS oder Linux. Bitte eine erwachsene Person um Hilfe, wenn du keine Programme installieren darfst.

## Schritt 1: Python installieren

Python ist die Programmiersprache. Geh auf [python.org/downloads](https://www.python.org/downloads/), klick auf den großen gelben Knopf und starte die Datei, die du bekommst.

Unter Windows setzt du auf der ersten Seite des Installationsprogramms den Haken bei **Add python.exe to PATH**. Das ist wichtig.

Du brauchst Python 3.10 oder neuer.

## Schritt 2: PyStage installieren

Öffne ein Terminal. Unter Windows suchst du im Startmenü nach „Eingabeaufforderung“. Unter macOS öffnest du die App „Terminal“. Tippe dann Folgendes ein und drücke die Eingabetaste:

```
pip install pystage
```

Warte, bis dort steht, dass es fertig ist. Wenn dein Computer `pip` nicht kennt, probiere stattdessen `python -m pip install pystage`.

## Schritt 3: Einen Editor besorgen

Dein Programm schreibst du in eine Textdatei. Ein Editor macht das leicht. [Thonny](https://thonny.org/) ist für Anfänger gemacht und bringt sein eigenes Python mit. Wenn du Thonny benutzt, kannst du PyStage auch darin installieren: Klick auf *Werkzeuge*, dann auf *Pakete verwalten*, such nach `pystage` und klick auf *Installieren*.

## Schritt 4: Dein erstes Programm

Tippe das hier in deinen Editor und speichere es als `erstes.py`. Starte es dann: In Thonny klickst du auf den grünen Start-Knopf. In einem Terminal tippst du `python erstes.py`.

```python {run=true}
from pystage.de import Figur, Bühne

bühne = Bühne()
zombie = bühne.füge_eine_figur_hinzu()

def los(zombie: Figur):
    for i in range(4):
        zombie.gehe_schritte(10)
        zombie.drehe_dich_nach_links_um_grad(90)
        zombie.warte_sekunden(1)

zombie.wenn_programm_startet(los)

bühne.abspielen()
```

Ein Fenster öffnet sich. Der Zombie läuft ein kleines Quadrat. Gut gemacht, du hast dein erstes PyStage-Programm geschrieben!

### Was steht in dem Programm?

- `from pystage.de import Figur, Bühne` holt die Teile, die du brauchst.
- `bühne = Bühne()` macht die Bühne, den Ort, an dem alles passiert.
- `zombie = bühne.füge_eine_figur_hinzu()` setzt eine Figur auf die Bühne. Du kannst ihr jeden Namen geben.
- `def los(zombie):` ist dein Skript. Alles, was nach rechts eingerückt ist, gehört dazu.
- `for i in range(4):` ist wie „wiederhole 4 mal“ in Scratch.
- `zombie.wenn_programm_startet(los)` ist der Hut-Block „Wenn die grüne Flagge angeklickt wird“.
- `bühne.abspielen()` öffnet das Fenster. Lass es als letzte Zeile stehen.

## Etwas ist schiefgegangen?

- Wenn du `No module named pystage` siehst, führe `pip install pystage` noch einmal aus. Achte darauf, dass du in deinem Editor dasselbe Python benutzt.
- Wenn du früher das alte `pygame` installiert hast, entferne es mit `pip uninstall pygame` und führe dann `pip install pystage` noch einmal aus.
- Frag auf [Discord](https://discord.gg/MSGrs3UCCz) nach Hilfe.

## Wie geht es weiter?

- Lass den Zombie laufen und reden: [Projekte](/projects/walk-and-talk/).
- Blöcke nachschlagen: [Blöcke](/blocks/).
- Ein Scratch-Projekt in Python umwandeln: [Umwandeln](/convert/).
