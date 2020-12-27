rounds = 0
score = [0, 0]


def on_gesture_shake():
    global rounds

    basic.show_animation("""
    # . # . # . . . . . # . # . # . . . . . # . # . #
    . # # # . . . # . . . # # # . . . # . . . # # # .
    # # . # # . # . # . # # . # # . # . # . # # . # #
    . # # # . . . # . . . # # # . . . # . . . # # # .
    # . # . # . . . . . # . # . # . . . . . # . # . #
    """, 700)

    basic.clear_screen()
    basic.pause(500)

    rounds += 1
    basic.show_number(rounds)

    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)

    hand1 = randint(1, 3)
    hand2 = randint(1, 3)

    if hand1 == 1: # Santa
        basic.show_leds("""
            . . . # #
            . . # . #
            . # # # .
            # # # # #
            . . . . .
        """)
    elif hand1 == 2: # Tree
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
        """)
    else: # Reindeer
        basic.show_leds("""
            # . . . #
            . # . # .
            # # . # #
            . # # # .
            . # # # .
        """)

    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)

    if hand2 == 1: # Santa
        basic.show_leds("""
            . . . # #
            . . # . #
            . # # # .
            # # # # #
            . . . . .
        """)
    elif hand2 == 2: # Tree
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
        """)
    else: # Reindeer
        basic.show_leds("""
            # . . . #
            . # . # .
            # # . # #
            . # # # .
            . # # # .
        """)

    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)

    if hand1 == 1: # Santa
        if hand2 == 1: # Santa
            winner = 0
        elif hand2 == 2: # Tree
            winner = 2
        else: # Reindeer
            winner = 1
    elif hand1 == 2: # Tree
        if hand2 == 1: # Santa
            winner = 1
        elif hand2 == 2: # Tree
            winner = 0
        else: # Reindeer
            winner = 2
    else: # Reindeer
        if hand2 == 1: # Santa
            winner = 2
        elif hand2 == 2: # Tree
            winner = 1
        else: # Reindeer
            winner = 0

    basic.show_number(winner)

    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)

    if winner == 1:
        score[0] += 1
    elif winner == 2:
        score[1] += 1

    basic.show_string(str(score[0]) + "-" + str(score[1]))

input.on_gesture(Gesture.SHAKE, on_gesture_shake)
