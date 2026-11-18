---
title: "Für Lehrkräfte"
menu_title: "Für Lehrkräfte"
description: "Wie PyStage Scratch und Python verbindet, wie Sie es im Unterricht einrichten und was Sie über den Umwandler wissen sollten."
nav: teachers
weight: 10
lead: "PyStage schlägt die Brücke zwischen Scratch und Python: Schülerinnen und Schüler behalten die Ideen, die sie aus Scratch kennen, und lernen, wie dasselbe Programm in einer textbasierten Sprache aussieht."
translation_of: "teachers.md"
source_hash: "abb1e972116c6e42"
---

## Was PyStage ist

PyStage ist eine kostenlose Python-Bibliothek mit einer Methode für jeden Scratch-Block, für Figuren und für die Bühne. Skripte, die mit einem Hut-Block beginnen, werden zu Funktionen, die mit demselben Ereignis verbunden sind. Ein Umwandler macht aus Scratch-3-Projekten Python-Code, der diese Methoden benutzt, sodass die Lernenden ihre eigenen Projekte als Text ansehen können. Grafik und Klang laufen auf [PyGame](https://www.pygame.org/news).

Die Seiten für Kinder ([Start](/start/), [Blöcke](/blocks/), [Projekte](/projects/)) sind für Schülerinnen und Schüler ab etwa 10 Jahren geschrieben, die Scratch kennen. Unter [Material](/material/) finden Sie, was Sie im Unterricht verwenden können.

## Wie sich der Code wie Scratch verhält

Einiges funktioniert anders als in normalen Python-Programmen, weil sich der Code wie ein Scratch-Skript verhält.

### Schleifen aktualisieren den Bildschirm

Der Bildschirm wird nach jedem Durchlauf einer Schleife und nach Blöcken, die Zeit brauchen, aktualisiert, zum Beispiel nach `warte_sekunden`. Die Lernenden müssen keine Spielschleife schreiben.

### Funktionen sind eigene Blöcke

Funktionen in derselben Datei, die Sie aus Ihrem Code aufrufen, verhalten sich wie eigene Blöcke in Scratch. Sie können deshalb ebenfalls Schleifen und `warte_sekunden` enthalten.

### Ohne Bildschirmaktualisierung ausführen

Markieren Sie eine Funktion mit `@ohne_bildschirmaktualisierung`, dann läuft sie in einem Zug, wie „ohne Bildschirmaktualisierung“ bei eigenen Blöcken in Scratch. Im folgenden Beispiel wird das Quadrat sofort gezeichnet.

```python {run=true}
from pystage.de import Figur, Bühne, ohne_bildschirmaktualisierung

bühne = Bühne()
zombie = bühne.füge_eine_figur_hinzu()

def springe(zombie: Figur, höhe):
    for i in range(10):
        zombie.ändere_y_um(höhe / 10)
    for i in range(10):
        zombie.ändere_y_um(-höhe / 10)

@ohne_bildschirmaktualisierung
def zeichne_quadrat(zombie: Figur):
    # Wie "ohne Bildschirmaktualisierung" in Scratch:
    # Das Quadrat ist sofort da.
    zombie.schalte_stift_ein()
    for i in range(4):
        zombie.gehe_schritte(50)
        zombie.drehe_dich_nach_links_um_grad(90)
    zombie.schalte_stift_aus()

def los(zombie: Figur):
    zeichne_quadrat(zombie)
    while True:
        springe(zombie, 80)
        zombie.warte_sekunden(1)

zombie.wenn_programm_startet(los)

bühne.abspielen()
```

### Fehler werden angezeigt

Wenn im Code ein Fehler steckt, wird die Meldung im Fenster und im Terminal angezeigt.

## Im Unterricht einrichten

- **Python:** PyStage braucht Python 3.10 oder neuer, das kostenlos auf [python.org](https://www.python.org/downloads/) erhältlich ist. Unter Windows sollte im Installationsprogramm die Option „Add python.exe to PATH“ angehakt sein.
- **PyStage:** `pip install pystage` installiert PyStage und [pygame-ce](https://pyga.me/). Ist das klassische `pygame` installiert, entfernen Sie es zuerst (`pip uninstall pygame`). Auf verwalteten Schulrechnern bitten Sie Ihre IT-Administration, PyStage für alle Benutzer zu installieren oder die Installation von Paketen mit `pip` zu erlauben, oder Sie verwenden eine virtuelle Umgebung im Home-Verzeichnis der Lernenden.
- **Editor:** Jeder Editor funktioniert. [Thonny](https://thonny.org/) ist eine gute Wahl für Anfänger, weil es Python mitbringt und eine einfache Paketverwaltung hat. Editoren mit Autovervollständigung helfen den Lernenden, die Methoden zu finden.
- **Ohne Installation:** Im Browser läuft nichts. Die Lernenden brauchen einen Computer, auf dem sie Python-Programme ausführen dürfen.

## Eine Sprache für die Klasse wählen

Die API gibt es in mehreren Sprachen: `pystage.en` (Englisch) und `pystage.de` (Deutsch, mit den Blocknamen des deutschen Scratch). Nicht nur die Methodennamen ändern sich mit der Sprache. Die Werte der Auswahlmenüs von Scratch (Tasten, Listenpositionen, besondere Figuren wie der Mauszeiger, mathematische Funktionen) können in der Sprache der API angegeben werden, und auch die Meldungen im Fenster richten sich danach. Wählen Sie eine Sprache pro Klasse und bleiben Sie dabei.

## Scratch-Projekte umwandeln

Die Lernenden können ihre Projekte mit dem [Online-Umwandler](https://convert.pystage.org) umwandeln, siehe [Umwandeln](/convert/).

### Datenschutz

Hochgeladene Projekte werden nach 7 Tagen vom Server gelöscht. Das umgewandelte Projekt ist nur über seinen eigenen zufälligen Link erreichbar.

### In der Kommandozeile

Mit installiertem PyStage können Sie auch auf dem eigenen Computer umwandeln, zum Beispiel für eine ganze Klasse. Exportieren Sie das Scratch-Projekt als .sb3-Datei und führen Sie dann Folgendes aus:

```
python -m pystage.convert.sb3 <SB3-Datei> -l de -d <VERZEICHNIS>
```

| Option | Bedeutung |
|---|---|
| `-l` | Sprache der erzeugten Python-„Scratch-Blöcke“. Im Moment gibt es `en` und `de`. Ohne diese Option wird die sprachneutrale Kern-API verwendet. |
| `-d` | Das Ausgabeverzeichnis, standardmäßig das aktuelle Verzeichnis. |
| `-i` | Gibt die Zwischendarstellung des Codes aus. |
| `-s` | Gibt die project.json des sb3-Projekts aus. |
| `-p` | Gibt den Python-Code aus. |
| `-v` | Ausführliche Ausgabe. |
| `-vv` | Debug-Modus. |

### Was wird umgewandelt

Skripte, eigene Blöcke, Variablen, Listen, Anzeigen und Kommentare eines Projekts werden umgewandelt.

### Was wird nicht unterstützt

Blöcke aus anderen Erweiterungen als Stift (zum Beispiel Musik oder Text zu Sprache) werden nicht unterstützt. Sie erscheinen im Python-Code als Text, der mit `NOT SUPPORTED` beginnt. So können Sie nach diesem Text suchen und diese Stellen von Hand neu schreiben.

Blöcke, die ein Mikrofon brauchen (Lautstärke), sind vorhanden, tun aber nichts.

PyStage ist eine Alpha-Version, deshalb muss ein umgewandeltes Projekt vielleicht noch repariert werden. Wenn Sie ein Projekt finden, das nicht gut umgewandelt wird, [eröffnen Sie bitte ein Issue](https://github.com/pystage/pystage/issues).
