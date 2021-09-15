# Microbit code for a reaction game.
# Shows a random letter (A or B) for a short length of time.
# The user must press the corresponding button within that
# time to score a point.  If they press the wrong button
# or press too late they lose points.

score = 0
letter_showing = ""
isdead = False
lives = 3

def on_button_pressed_common(letter_2_check):
    global letter_showing, score, lives
    if letter_showing == letter_2_check:
        letter_showing = ""
        basic.clear_screen()
        music.play_tone(462, music.beat(BeatFraction.WHOLE))
        score = score + 1
    else:
        music.play_tone(100 + lives * 20, music.beat(BeatFraction.WHOLE))
        lives = lives - 1
        check_if_dead() 

def game_reset():
    global score,letter_showing,isdead,lives
    score = 0
    letter_showing = ""
    lives = 3
    basic.show_icon(IconNames.HAPPY)
    music.play_melody("C5 D D F D F F D ", 120)
    isdead = False

def reset_game():
    if isdead:
        game_reset()
input.on_button_pressed(Button.AB,reset_game)

def on_button_pressed_a():
   on_button_pressed_common("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
   on_button_pressed_common("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def check_if_dead():
    global lives, isdead, score
    if lives <= 0:
        # Yes, we're dead.
        isdead = True
        basic.show_icon(IconNames.GHOST)
        #music.play_melody("C5 A B G A F G E ", 120)
        basic.pause(2000)
        basic.show_number(score)


def on_forever():
    global letter_showing, isdead
    if not isdead:
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
    else:
        pass
        # what should we do when we're dead?

basic.forever(on_forever)
