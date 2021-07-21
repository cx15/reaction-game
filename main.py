# Microbit code for a reaction game.
# Shows a random letter (A or B) for a short length of time.
# The user must press the corresponding button within that
# time to score a point.  If they press the wrong button
# or press too late they lose points.
letter_showing = ""

score = 0

lives = 3

isdead = False

def on_button_pressed_a():
    if letter_showing == "A":
        letter_showing = ""
        music.play_tone(462, music.beat(BeatFraction.WHOLE))
        score = score + 1
    else:
        music.play_tone(162, music.beat(BeatFraction.WHOLE))
        lives = lives - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_B():
    if letter_showing == "B":
        music.play_tone(462, music.beat(BeatFraction.WHOLE))
        score = score + 1
    else:
        music.play_tone(162, music.beat(BeatFraction.WHOLE))
        lives = lives - 1
input.on_button_pressed(Button.B, on_button_pressed_B)


def on_forever():
    global letter_showing
    global lives 
    global score 
    basic.pause(randint(0, 2000))
    if Math.random_boolean():
        letter_showing = "A"
        basic.show_string("A")
    else:
        letter_showing = "B"
        basic.show_string("B")
    basic.pause(1000)
    basic.clear_screen()
    letter_showing = ""
    if lives <= 0: 
        basic.show_number(score)

basic.forever(on_forever)

