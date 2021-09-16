//  Microbit code for a reaction game.
//  Shows a random letter (A or B) for a short length of time.
//  The user must press the corresponding button within that
//  time to score a point.  If they press the wrong button
//  or press too late they lose points.
let score = 0
let hiscore = 0
let letter_showing = ""
let isdead = false
let lives = 3
let max_time_on_screen = 0
let max_pause_before_showing = 0
game_reset()
function on_button_pressed_common(letter_2_check: string) {
    
    if (letter_showing == letter_2_check) {
        letter_showing = ""
        basic.clearScreen()
        music.playTone(462, music.beat(BeatFraction.Whole))
        score = score + 1
        max_time_on_screen = max_time_on_screen / 2
        max_pause_before_showing = max_pause_before_showing / 2
    } else {
        music.playTone(100 + lives * 20, music.beat(BeatFraction.Whole))
        lives = lives - 1
        check_if_dead()
    }
    
}

function game_reset() {
    
    score = 0
    letter_showing = ""
    basic.showIcon(IconNames.Happy)
    music.playMelody("C5 D D F D F F D ", 120)
    lives = 3
    isdead = false
    max_time_on_screen = 4000
    max_pause_before_showing = 2000
}

input.onButtonPressed(Button.AB, function on_ab_pressed() {
    if (isdead) {
        game_reset()
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    on_button_pressed_common("A")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    on_button_pressed_common("B")
})
function check_if_dead() {
    
    if (lives <= 0) {
        //  Yes, we're dead.
        isdead = true
        basic.showIcon(IconNames.Ghost)
        music.playMelody("F3 D3 A2", 60)
        basic.pause(2000)
        basic.showString("Score: " + score)
        if (score > hiscore) {
            hiscore = score
        }
        
        basic.showString("Hi:" + hiscore)
    }
    
}

basic.forever(function on_forever() {
    
    if (!isdead) {
        basic.pause(randint(0, max_pause_before_showing))
        if (Math.randomBoolean()) {
            letter_showing = "A"
            basic.showString("A")
        } else {
            letter_showing = "B"
            basic.showString("B")
        }
        
        basic.pause(randint(0, max_time_on_screen))
        basic.clearScreen()
        letter_showing = ""
    }
    
})
