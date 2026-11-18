---
title: "Programmieren wie in Scratch, mit Python"
description: "PyStage bietet alle Scratch-Blöcke als Python-Methoden an und wandelt Scratch-Projekte in Python um. Programmieren wie in Scratch, mit Python und PyGame."
nav: kids
menu_title: "Startseite"
weight: 1
lead: "Du kennst [Scratch](https://scratch.mit.edu/)? Mit PyStage machst du dieselben Spiele und Animationen, aber mit Python. Jeder Scratch-Block ist ein Python-Befehl. Hast du Lust, es auszuprobieren?"
start:
  text: "Hier starten"
  link: "/start/"
teachers:
  text: "Für Lehrkräfte"
  link: "/teachers/"
translation_of: "_index.md"
source_hash: "293f41c9286abc2d"
---

<div class="cards" role="list">
<div class="card" role="listitem"><h3>1. Installieren</h3><p>Zwei kleine Schritte, dann kann es losgehen.</p><p class="btns"><a class="btn" href="{{< rl "/start/" >}}">Hier starten</a></p></div>
<div class="card" role="listitem"><h3>2. Blöcke finden</h3><p>Sieh dir alle Scratch-Blöcke an und den Python-Befehl, der dasselbe macht.</p><p class="btns"><a class="btn" href="{{< rl "/blocks/" >}}">Blöcke</a></p></div>
<div class="card" role="listitem"><h3>3. Etwas bauen</h3><p>Kleine Projekte, Schritt für Schritt.</p><p class="btns"><a class="btn" href="{{< rl "/projects/" >}}">Projekte</a></p></div>
<div class="card" role="listitem"><h3>Du hast ein Scratch-Projekt?</h3><p>Verwandle es in Python und sieh, wie es funktioniert.</p><p class="btns"><a class="btn" href="{{< rl "/convert/" >}}">Umwandeln</a></p></div>
</div>

## Scratch-Blöcke, als Python geschrieben

Zu jedem Scratch-Block gibt es einen passenden Befehl. Ein Scratch-Skript, das mit einem Hut-Block beginnt („Wenn die grüne Flagge angeklickt wird“), wird in Python zu einer Funktion, die du mit demselben Ereignis verbindest. PyStage aktualisiert den Bildschirm nach jedem Durchlauf einer Schleife und nach Blöcken wie `warte_sekunden`. Dein Code verhält sich deshalb wie ein Scratch-Skript, und du musst keine Spielschleife schreiben.

<figure>
<div class="scrollx" tabindex="0" role="group" aria-label="Abbildung von Scratch zu Python, lässt sich auf kleinen Bildschirmen zur Seite scrollen"><img class="shot" src="{{< asset "/assets/pystage-banner.png" >}}" width="1448" height="529" alt="Links: ein Scratch-Skript mit den Blöcken when flag clicked, go to x y, set size, repeat 8 mit move, change size, next costume und wait, dann say Hello pyStage. Mitte: die Scratch-Katze auf der Bühne, die Hello pyStage sagt. Rechts: dasselbe Programm als PyStage-Python-Code (mit englischen Namen)."></div>
<figcaption>Ein Scratch-Skript (links) und der Python-Code, den der PyStage-Umwandler daraus macht (rechts). Die Abbildung zeigt die englische Version.</figcaption>
</figure>

<div class="tablewrap"><table>
<caption class="visually-hidden">Scratch-Blöcke und die passenden PyStage-Befehle</caption>
<thead><tr><th scope="col">Scratch-Block</th><th scope="col">PyStage (deutsch)</th></tr></thead>
<tbody>
<tr><td>Wenn die grüne Flagge angeklickt wird</td><td><code>figur.wenn_programm_startet(funktion)</code></td></tr>
<tr><td>Wenn Taste <em>d</em> gedrückt wird</td><td><code>figur.wenn_taste_gedrückt_wird("d", funktion)</code></td></tr>
<tr><td>gehe 10er Schritt</td><td><code>figur.gehe_schritte(10)</code></td></tr>
<tr><td>drehe dich nach links um 90 Grad</td><td><code>figur.drehe_dich_nach_links_um_grad(90)</code></td></tr>
<tr><td>ändere x um 10</td><td><code>figur.ändere_x_um(10)</code></td></tr>
<tr><td>warte 1 Sekunden</td><td><code>figur.warte_sekunden(1)</code></td></tr>
<tr><td>sage Hallo!</td><td><code>figur.sage("Hallo!")</code></td></tr>
</tbody></table></div>

## Ein vollständiges Beispiel

Dieses Programm legt eine Bühne und eine Figur an. Die Funktionen sind deine Skripte. Jede verbindest du mit einem Ereignis, genau wie einen Hut-Block in Scratch.

```python {run=true}
from pystage.de import Bühne

bühne = Bühne()
bühne.füge_bühnenbild_hinzu("grid")
zombie = bühne.füge_eine_figur_hinzu()

def los(zombie):
    zombie.sage("Hallo pyStage!")
    for i in range(4):
        zombie.gehe_schritte(10)
        zombie.warte_sekunden(1)
        zombie.denke("Das ist toll!")
        zombie.drehe_dich_nach_links_um_grad(90)
        zombie.warte_sekunden(1)
        zombie.denke("")
    zombie.sage("Bewege mich mit WASD.")

zombie.wenn_programm_startet(los)

def rechts(zombie):
    zombie.ändere_x_um(10)

def links(zombie):
    zombie.ändere_x_um(-10)

def hoch(zombie):
    zombie.ändere_y_um(10)

def runter(zombie):
    zombie.ändere_y_um(-10)

zombie.wenn_taste_gedrückt_wird("d", rechts)
zombie.wenn_taste_gedrückt_wird("a", links)
zombie.wenn_taste_gedrückt_wird("w", hoch)
zombie.wenn_taste_gedrückt_wird("s", runter)

bühne.abspielen()
```

Und so sieht das Ergebnis aus:

<figure>
<img class="shot" src="{{< asset "/assets/demo.gif" >}}" width="484" height="389" alt="Bildschirmaufnahme des Beispiels: Eine Figur auf einem Gitter sagt Hello pyStage, bewegt sich im Quadrat und lässt sich mit den Tasten W, A, S und D bewegen.">
<figcaption>Bildschirmaufnahme des Beispielprogramms (mit englischen Texten).</figcaption>
</figure>

## Warum PyStage?

- Lerne Python „mit Scratch“: Du kennst die Ideen schon, jetzt siehst du den Code dazu.
- Verwandle deine eigenen Scratch-Projekte in echte Python-Programme.
- Die Blöcke gibt es in mehreren Sprachen, das ist ideal für Kinder. Im Moment: Englisch und Deutsch.

<div class="note"><strong>Alpha-Version.</strong> Nicht alles funktioniert schon so, wie es soll. Wenn etwas kaputtgeht, <a href="{{< rl "/contact/" >}}">sag uns bitte Bescheid</a>.</div>

## Kurzes Einführungsvideo

<p><a class="video" href="https://www.youtube.com/watch?v=Bo3kUF9k0Vg"><img src="{{< asset "/assets/video-thumb.jpg" >}}" width="480" height="360" alt="Vorschaubild des Videos: Kurze Einführung in PyStage für die ScratchCon 2021"><span aria-hidden="true">&#9654;</span></a></p>

<p><a href="https://www.youtube.com/watch?v=Bo3kUF9k0Vg">Schau dir unser kurzes Einführungsvideo zu PyStage für die ScratchCon 2021 an</a> (öffnet YouTube, auf Englisch).</p>
