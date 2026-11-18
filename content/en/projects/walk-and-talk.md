---
title: "Make the zombie walk and talk"
description: "A first project: a sprite that talks, walks and can be steered with the keyboard."
weight: 1
lead: "A zombie, a stage, a few words. Build it in five small steps."
---

You need PyStage. If you do not have it yet, go to [Start](/start/) first.

In every step you get a whole program. Type it in (do not copy it, typing is the best way to learn) and run it. Then change things and watch what happens.

## Step 1: A zombie on the stage

```python {run=true}
from pystage.en import Stage

stage = Stage()
zombie = stage.add_a_sprite()

stage.play()
```

You see a window with a zombie in the middle. It does nothing yet. Close the window to stop the program.

## Step 2: Let it talk

A script is a function. We connect it to "when program starts", like the green flag in Scratch.

```python {run=true}
from pystage.en import Stage

stage = Stage()
zombie = stage.add_a_sprite()

def start(zombie):
    zombie.say_for_seconds("Hello! I am a zombie.", 2)
    zombie.say("Let's go for a walk.")

zombie.when_program_starts(start)

stage.play()
```

`say_for_seconds` is "say Hello for 2 seconds". After that the zombie says the next thing. Try your own words.

## Step 3: Let it walk

```python {run=true}
from pystage.en import Stage

stage = Stage()
zombie = stage.add_a_sprite()

def start(zombie):
    zombie.say_for_seconds("Hello! I am a zombie.", 2)
    zombie.say("Let's go for a walk.")
    for i in range(20):
        zombie.move(10)
        zombie.wait(0.1)
    zombie.say("Phew, that was far.")

zombie.when_program_starts(start)

stage.play()
```

`for i in range(20):` repeats everything below it 20 times, like "repeat 20" in Scratch. Make the zombie walk further or faster by changing 20, 10 and 0.1.

## Step 4: Steer it with the keyboard

Now you decide where the zombie goes. A second function is connected to the key "space", and two more to the arrow keys.

```python {run=true}
from pystage.en import Stage

stage = Stage()
zombie = stage.add_a_sprite()

def start(zombie):
    zombie.say_for_seconds("Hello! I am a zombie.", 2)
    zombie.say("Use the arrow keys to walk, space to talk.")

def walk_right(zombie):
    zombie.change_x_by(10)

def walk_left(zombie):
    zombie.change_x_by(-10)

def talk(zombie):
    zombie.say_for_seconds("Brains!", 1)

zombie.when_program_starts(start)
zombie.when_key_pressed("right arrow", walk_right)
zombie.when_key_pressed("left arrow", walk_left)
zombie.when_key_pressed("space", talk)

stage.play()
```

## Step 5: Think and turn

Let us make a surprise. When you press the key "t", the zombie thinks, turns around and walks back.

```python {run=true}
from pystage.en import Stage

stage = Stage()
stage.add_backdrop("grid")
zombie = stage.add_a_sprite()

def start(zombie):
    zombie.say_for_seconds("Press t to see a surprise.", 3)

def surprise(zombie):
    zombie.think_for_seconds("Hmm, wrong way.", 2)
    zombie.turn_left(180)
    for i in range(10):
        zombie.move(10)
        zombie.wait(0.1)

zombie.when_program_starts(start)
zombie.when_key_pressed("t", surprise)

stage.play()
```

## Your turn

- Add a second key that makes the zombie go up and down.
- Change what the zombie says.
- Use `zombie.set_size_to(150)` to make the zombie bigger.

More projects will follow. If you made something nice, show us on [Discord](https://discord.gg/MSGrs3UCCz).
