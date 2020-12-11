rounds = 0
score = [0, 0]


def on_gesture_shake():
    global rounds

    basic.show_animation("""
    . . . . . # . . . . . . . . . . . . . # . . . . .
    . . # . . . . . . . . . # . . . . . . . . . # . .
    . # . # . . . # . . . # . # . . . # . . . # . # .
    . . # . . . . . . . . . # . . . . . . . . . # . .
    . . . . . . . . . # . . . . . # . . . . . . . . .
    """, 500)

    basic.clear_screen()
    basic.pause(500)

    rounds += 1
    basic.show_number(rounds)

    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)

    hand1 = randint(1, 3)
    hand2 = randint(1, 3)

    if hand1 == 1: # Rock
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand1 == 2: # Paper
        basic.show_icon(IconNames.SQUARE)
    else: # Scissors
        basic.show_icon(IconNames.SCISSORS)

    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)

    if hand2 == 1: # Rock
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand2 == 2: # Paper
        basic.show_icon(IconNames.SQUARE)
    else: # Scissors
        basic.show_icon(IconNames.SCISSORS)

    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)

    if hand1 == 1: # Rock
        if hand2 == 1: # Rock
            winner = 0
        elif hand2 == 2: # Paper
            winner = 2
        else: # Scissors
            winner = 1
    elif hand1 == 2: # Paper
        if hand2 == 1: # Rock
            winner = 1
        elif hand2 == 2: # Paper
            winner = 0
        else: # Scissors
            winner = 2
    else: # Scissors
        if hand2 == 1: # Rock
            winner = 2
        elif hand2 == 2: # Paper
            winner = 1
        else: # Scissors
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
