---
title: "Scratch-like Python programming"
description: "PyStage offers all Scratch blocks as Python methods and converts Scratch projects to Python. Scratch-like Python programming on PyGame."
nav: kids
menu_title: "Home"
weight: 1
lead: "You know [Scratch](https://scratch.mit.edu/)? With PyStage you can make the same games and animations, but with Python. Every Scratch block is a Python command. Ready to try?"
start:
  text: "Start here"
  link: "/start/"
teachers:
  text: "For teachers"
  link: "/teachers/"
---

<div class="cards" role="list">
<div class="card" role="listitem"><h3>1. Install</h3><p>Two small steps, then you are ready.</p><p class="btns"><a class="btn" href="{{< rl "/start/" >}}">Start here</a></p></div>
<div class="card" role="listitem"><h3>2. Find your blocks</h3><p>See every Scratch block and the Python command that does the same.</p><p class="btns"><a class="btn" href="{{< rl "/blocks/" >}}">Blocks</a></p></div>
<div class="card" role="listitem"><h3>3. Make something</h3><p>Small projects, step by step.</p><p class="btns"><a class="btn" href="{{< rl "/projects/" >}}">Projects</a></p></div>
<div class="card" role="listitem"><h3>Have a Scratch project?</h3><p>Turn it into Python and see how it works.</p><p class="btns"><a class="btn" href="{{< rl "/convert/" >}}">Convert</a></p></div>
</div>

## Scratch blocks, written as Python

Every Scratch block has a matching command. A Scratch script that starts with a hat block ("when green flag clicked") becomes a Python function that you connect to the same event. PyStage updates the screen after every round of a loop and after blocks like `wait`, so your code behaves like a Scratch script. You do not need to write a game loop.

<figure>
<div class="scrollx" tabindex="0" role="group" aria-label="Scratch to Python illustration, scrolls sideways on small screens"><img class="shot" src="{{< asset "/assets/pystage-banner.png" >}}" width="1448" height="529" alt="Left: a Scratch script with the blocks when flag clicked, go to x y, set size, repeat 8 with move, change size, next costume and wait, then say Hello pyStage. Middle: the Scratch cat on a stage saying Hello pyStage. Right: the same program as PyStage Python code."></div>
<figcaption>A Scratch script (left) and the Python code that the PyStage converter makes from it (right).</figcaption>
</figure>

<div class="tablewrap"><table>
<caption class="visually-hidden">Scratch blocks and the matching PyStage commands</caption>
<thead><tr><th scope="col">Scratch block</th><th scope="col">PyStage (English)</th></tr></thead>
<tbody>
<tr><td>when green flag clicked</td><td><code>sprite.when_program_starts(function)</code></td></tr>
<tr><td>when <em>d</em> key pressed</td><td><code>sprite.when_key_pressed("d", function)</code></td></tr>
<tr><td>move 10 steps</td><td><code>sprite.move(10)</code></td></tr>
<tr><td>turn left 90 degrees</td><td><code>sprite.turn_left(90)</code></td></tr>
<tr><td>change x by 10</td><td><code>sprite.change_x_by(10)</code></td></tr>
<tr><td>wait 1 seconds</td><td><code>sprite.wait(1)</code></td></tr>
<tr><td>say Hello</td><td><code>sprite.say("Hello")</code></td></tr>
</tbody></table></div>

## A complete example

This program makes a stage and a sprite. The functions are your scripts. You connect each one to an event, just like a hat block in Scratch.

```python {run=true}
from pystage.en import Stage

stage = Stage()
stage.add_backdrop("grid")
zombie = stage.add_a_sprite()

def doit(zombie):
    zombie.say("Hello pyStage!")
    for i in range(4):
        zombie.move(10)
        zombie.wait(1)
        zombie.think("This is awesome!")
        zombie.turn_left(90)
        zombie.wait(1)
        zombie.think("")
    zombie.say("Move me around with WASD.")

zombie.when_program_starts(doit)

def right(zombie):
    zombie.change_x_by(10)

def left(zombie):
    zombie.change_x_by(-10)

def up(zombie):
    zombie.change_y_by(10)

def down(zombie):
    zombie.change_y_by(-10)

zombie.when_key_pressed("d", right)
zombie.when_key_pressed("a", left)
zombie.when_key_pressed("w", up)
zombie.when_key_pressed("s", down)

stage.play()
```

And here is what you see:

<figure>
<img class="shot" src="{{< asset "/assets/demo.gif" >}}" width="484" height="389" alt="Screen capture of the demo: a sprite on a grid says Hello pyStage, moves in a square and can be moved around with the keys W, A, S and D.">
<figcaption>Screen capture of the demo program.</figcaption>
</figure>

## Why PyStage?

- Learn Python "by Scratch": you already know the ideas, now you see the code.
- Turn your own Scratch projects into real Python programs.
- The blocks come in several languages, which is great for kids. Right now: English and German.

<div class="note"><strong>Alpha version.</strong> Not everything works perfectly yet. If something breaks, please <a href="{{< rl "/contact/" >}}">tell us</a>.</div>

## Quick intro video

<p><a class="video" href="https://www.youtube.com/watch?v=Bo3kUF9k0Vg"><img src="{{< asset "/assets/video-thumb.jpg" >}}" width="480" height="360" alt="Video thumbnail: Quick intro to PyStage for ScratchCon 2021"><span aria-hidden="true">&#9654;</span></a></p>

<p><a href="https://www.youtube.com/watch?v=Bo3kUF9k0Vg">Watch our quick intro to PyStage for ScratchCon 2021</a> (opens YouTube, English).</p>
