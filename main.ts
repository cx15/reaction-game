//  Microbit code for a reaction game.
//  Shows a random letter (A or B) for a short length of time.
//  The user must press the corresponding button within that
//  time to score a point.  If they press the wrong button
//  or press too late they lose points.
let letter_showing = ""
let score = 0
let lives = 3
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let score: number;
    let lives: number;
    if (letter_showing == "A") {
        music.playTone(462, music.beat(BeatFraction.Whole))
        score = score + 1
    } else {
        music.playTone(162, music.beat(BeatFraction.Whole))
        lives = lives - 1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_B() {
    let score: number;
    let lives: number;
    if (letter_showing == "B") {
        music.playTone(462, music.beat(BeatFraction.Whole))
        score = score + 1
    } else {
        music.playTone(162, music.beat(BeatFraction.Whole))
        lives = lives - 1
    }
    
})
basic.forever(function on_forever() {
    
    
    
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
    if (lives == 0) {
        basic.showNumber(score)
    }
    
})
