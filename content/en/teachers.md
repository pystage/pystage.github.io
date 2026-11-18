---
title: "For teachers"
menu_title: "For teachers"
description: "How PyStage bridges Scratch and Python, how to set it up in class, and what to know about the converter."
nav: teachers
weight: 10
lead: "PyStage bridges the gap between Scratch and Python: students keep the ideas they know from Scratch and learn how the same program looks in a text-based language."
---

## What PyStage is

PyStage is a free Python library with a method for every Scratch block, for sprites and for the stage. Scripts that start with a hat block become functions that are connected to the same event. A converter turns Scratch 3 projects into Python code that uses these methods, so students can look at their own projects as text. Graphics and sound run on [PyGame](https://www.pygame.org/news).

The kids' pages of this site ([Start](/start/), [Blocks](/blocks/), [Projects](/projects/)) are written for students aged about 10 and older who know Scratch. [Material](/material/) lists what you can use in class.

## How code behaves like Scratch

Some things work differently than in normal Python programs, because the code behaves like a Scratch script.

### Loops refresh the screen

The screen is refreshed after each iteration of a loop and after blocks that take time, like `wait`. Students do not have to write a game loop.

### Functions are custom blocks

Functions in the same file that you call from your code behave like custom blocks in Scratch, so they can contain loops and `wait` as well.

### Run without screen refresh

Mark a function with `@no_refresh` and it runs at once, like "run without screen refresh" in Scratch. In the example below, the square is drawn immediately.

```python {run=true}
from pystage.en import Sprite, Stage, no_refresh

stage = Stage()
zombie = stage.add_a_sprite()

def jump(zombie: Sprite, height):
    for i in range(10):
        zombie.change_y_by(height / 10)
    for i in range(10):
        zombie.change_y_by(-height / 10)

@no_refresh
def draw_square(zombie: Sprite):
    # Like "run without screen refresh" in Scratch:
    # The square is there at once.
    zombie.pen_down()
    for i in range(4):
        zombie.move(50)
        zombie.turn_left(90)
    zombie.pen_up()

def doit(zombie: Sprite):
    draw_square(zombie)
    while True:
        jump(zombie, 80)
        zombie.wait(1)

zombie.when_program_starts(doit)

stage.play()
```

### Errors are shown

If there is an error in the code, the message is shown in the window and in the terminal.

## Setting it up in class

- **Python:** PyStage needs Python 3.10 or newer, which is free from [python.org](https://www.python.org/downloads/). On Windows, the installer option "Add python.exe to PATH" should be ticked.
- **PyStage:** `pip install pystage` installs PyStage and [pygame-ce](https://pyga.me/). If the classic `pygame` is installed, remove it first (`pip uninstall pygame`). On managed school computers, ask your IT administrator to install it for all users or to allow installing packages with `pip`, or use a virtual environment in the students' home folders.
- **Editor:** any editor works. [Thonny](https://thonny.org/) is a good choice for beginners, because it includes Python and has a simple package manager. Editors with autocompletion help students find the methods.
- **No installation:** nothing runs in the browser. Students need a computer where they may run Python programs.

## Choosing a language for a class

The API exists in several languages: `pystage.en` (English) and `pystage.de` (German, with the block names of German Scratch). Not only the method names change with the language. The values of Scratch's dropdown menus (keys, list positions, special sprites like the mouse pointer, math functions) can be given in the language of the API, and the messages shown in the window follow it as well. Pick one language per class and use it consistently.

## Converting Scratch projects

Students can convert their projects with the [web converter](https://convert.pystage.org); see [Convert](/convert/).

### Privacy

Uploaded projects are deleted from the server after 7 days. The converted project is reachable only through its own random link.

### On the command line

With PyStage installed, you can convert on your own computer, for example for a whole class. Export the Scratch project as an .sb3 file, then run:

```
python -m pystage.convert.sb3 <SB3 File> -l en -d <DIRECTORY>
```

| Option | Meaning |
|---|---|
| `-l` | Language of the generated Python "scratch blocks". At the moment `en` and `de` are available. Without it, the language neutral core API is used. |
| `-d` | The output directory, defaults to the current directory. |
| `-i` | Print the intermediate code representation. |
| `-s` | Print the sb3 project.json. |
| `-p` | Print the Python code. |
| `-v` | Verbose. |
| `-vv` | Debug mode. |

### What is converted

Scripts, custom blocks, variables, lists, monitors and comments of a project are converted.

### What is not supported

Blocks from extensions other than Pen (for example Music or Text to Speech) are not supported. They show up as a text starting with `NOT SUPPORTED` in the Python code, so you can search for that text and rewrite those parts by hand.

Blocks that need a microphone (loudness) are available but do nothing.

PyStage is an alpha version, so a converted project may need some fixes. If you find a project that does not convert well, please [open an issue](https://github.com/pystage/pystage/issues).
