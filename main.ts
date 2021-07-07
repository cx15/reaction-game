basic.forever(function A_or_B() {
    basic.pause(randint(0, 2000))
    if (Math.randomBoolean()) {
        basic.showString("A")
    } else {
        basic.showString("B")
    }
    
    basic.pause(1000)
    basic.clearScreen()
})
