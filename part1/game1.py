def on_gesture_shake():

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
            basic.show_number(0)
        elif hand2 == 2: # Paper
            basic.show_number(2)
        else: # Scissors
            basic.show_number(1)
    elif hand1 == 2: # Paper
        if hand2 == 1: # Rock
            basic.show_number(1)
        elif hand2 == 2: # Paper
            basic.show_number(0)
        else: # Scissors
            basic.show_number(2)
    else: # Scissors
        if hand2 == 1: # Rock
            basic.show_number(2)
        elif hand2 == 2: # Paper
            basic.show_number(1)
        else: # Scissors
            basic.show_number(0)

input.on_gesture(Gesture.SHAKE, on_gesture_shake)
