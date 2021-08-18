//  Microbit code for a reaction game.
//  Shows a random letter (A or B) for a short length of time.
//  The user must press the corresponding button within that
//  time to score a point.  If they press the wrong button
//  or press too late they lose points.
let score = 0
let letter_showing = ""
let lives = 0
let isdead = false
lives = 3
function on_button_pressed_common(letter_2_check: string) {
    
    if (letter_showing == letter_2_check) {
        letter_showing = ""
        basic.clearScreen()
        music.playTone(462, music.beat(BeatFraction.Whole))
        score = score + 1
    } else {
        music.playTone(100 + lives * 20, music.beat(BeatFraction.Whole))
        lives = lives - 1
        check_if_dead()
    }
    
}

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
        // music.play_melody("C5 A B G A F G E ", 120)
        basic.pause(2000)
        basic.showNumber(score)
    }
    
}

//  what should we do when we're dead?
basic.forever(function on_forever() {
    
    if (!isdead) {
        basic.pause(randint(0, 2000))
        if (Math.randomBoolean()) {
            letter_showing = "A"
            basic.showString("A")
        } else {
            letter_showing = "B"
            basic.showString("B")
        }
        
        basic.pause(1000)
        basic.clearScreen()
        letter_showing = ""
    } else {
        
    }
    
})
