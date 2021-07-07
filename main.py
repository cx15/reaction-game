


basic.forever(A_or_B)
def A_or_B():
    basic.pause(randint(0, 2000))
    if Math.random_boolean():    
        basic.show_string("A")
    else:
        basic.show_string("B")
    basic.pause(1000)
    basic.clear_screen()



