---
title: "Start"
menu_title: "Start"
description: "Install Python and PyStage and run your first program, step by step."
nav: kids
weight: 2
lead: "Install Python and PyStage, then run your first program. It takes about ten minutes."
---

## What you need

You need a computer with Windows, macOS or Linux. Ask a grown-up to help you if you are not allowed to install programs.

## Step 1: Install Python

Python is the programming language. Go to [python.org/downloads](https://www.python.org/downloads/), click the big yellow button and run the file you get.

On Windows, tick the box **Add python.exe to PATH** on the first screen of the installer. This is important.

You need Python 3.10 or newer.

## Step 2: Install PyStage

Open a terminal. On Windows, search for "Command Prompt" in the start menu. On macOS, open the app "Terminal". Then type this and press Enter:

```
pip install pystage
```

Wait until it says that it is done. If your computer says that it does not know `pip`, try `python -m pip install pystage` instead.

## Step 3: Get an editor

You write your program in a text file. An editor makes this easy. [Thonny](https://thonny.org/) is made for beginners and comes with its own Python. If you use Thonny, you can also install PyStage inside it: click on *Tools*, then *Manage packages*, search for `pystage` and click *Install*.

## Step 4: Your first program

Type this into your editor and save it as `first.py`. Then run it: in Thonny, click the green play button. In a terminal, type `python first.py`.

```python {run=true}
from pystage.en import Sprite, Stage

stage = Stage()
zombie = stage.add_a_sprite()

def doit(zombie: Sprite):
    for i in range(4):
        zombie.move(10)
        zombie.turn_left(90)
        zombie.wait(1)

zombie.when_program_starts(doit)

stage.play()
```

A window opens. The zombie walks in a small square. Well done, you have made your first PyStage program!

### What does the program say?

- `from pystage.en import Sprite, Stage` gets the parts you need.
- `stage = Stage()` makes the stage, the place where everything happens.
- `zombie = stage.add_a_sprite()` puts a sprite on the stage. You can give it any name.
- `def doit(zombie):` is your script. Everything that is pushed to the right belongs to it.
- `for i in range(4):` is like "repeat 4" in Scratch.
- `zombie.when_program_starts(doit)` is the hat block "when green flag clicked".
- `stage.play()` opens the window. Keep it as the last line.

## Something went wrong?

- If you see `No module named pystage`, run `pip install pystage` again. Make sure that you use the same Python in your editor.
- If you installed the old `pygame` before, remove it with `pip uninstall pygame`, then run `pip install pystage` again.
- Ask for help on [Discord](https://discord.gg/MSGrs3UCCz).

## What next?

- Make the zombie walk and talk: [Projects](/projects/walk-and-talk/).
- Look up blocks: [Blocks](/blocks/).
- Turn a Scratch project into Python: [Convert](/convert/).
