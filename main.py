# Microbit code for a reaction game.
# Shows a random letter (A or B) for a short length of time.
# The user must press the corresponding button within that
# time to score a point.  If they press the wrong button
# or press too late they lose points.

score = 0
hiscore = 0
letter_showing = ""
isdead = False
lives = 3
max_time_on_screen=0
max_pause_before_showing=0

game_reset()

def on_button_pressed_common(letter_2_check):
    global letter_showing, score, lives, max_time_on_screen,max_pause_before_showing
    if letter_showing == letter_2_check:
        letter_showing = ""
        basic.clear_screen()
        music.play_tone(462, music.beat(BeatFraction.WHOLE))
        score = score + 1
        max_time_on_screen = max_time_on_screen / 2
        max_pause_before_showing = max_pause_before_showing / 2
    else:
        music.play_tone(100 + lives * 20, music.beat(BeatFraction.WHOLE))
        lives = lives - 1
        check_if_dead()

def game_reset():
    global score,letter_showing,isdead,lives,max_time_on_screen,max_pause_before_showing
    score = 0
    letter_showing = ""
    basic.show_icon(IconNames.HAPPY)
    music.play_melody("C5 D D F D F F D ", 120)
    lives = 3
    isdead = False
    max_time_on_screen = 4000
    max_pause_before_showing = 2000


def on_ab_pressed():
    if isdead:
        game_reset()
input.on_button_pressed(Button.AB, on_ab_pressed)

def on_button_pressed_a():
   on_button_pressed_common("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
   on_button_pressed_common("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def check_if_dead():
    global lives, isdead, score, hiscore
    if lives <= 0:
        # Yes, we're dead.
        isdead = True
        basic.show_icon(IconNames.GHOST)
        music.play_melody("F3 D3 A2", 60) 
        basic.pause(2000)
        basic.show_string("Score: " + score)
        if score > hiscore:
            hiscore = score
        basic.show_string("Hi:" + hiscore)

def on_forever():
    global letter_showing, isdead, max_pause_before_showing, max_time_on_screen
    if not isdead:
        basic.pause(randint(0, max_pause_before_showing))
        if Math.random_boolean():
            letter_showing = "A"
            basic.show_string("A")
        else:
            letter_showing = "B"
            basic.show_string("B")
        basic.pause(randint(0, max_time_on_screen))
        basic.clear_screen()
        letter_showing = ""

basic.forever(on_forever)