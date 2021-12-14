radio.set_group(144)
radio.set_transmit_power(7)
minibit.led_brightness(0)


def on_received_number(receivedNumber):
    if receivedNumber == 1:
        minibit.stop(mbStopMode.BRAKE)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
        """)
    elif receivedNumber == 2:
        minibit.mb_bias(mbRobotDirection.RIGHT, 0)
        minibit.mb_bias(mbRobotDirection.LEFT, 0)
        minibit.go(mbDirection.FORWARD, 100)
        basic.clear_screen()
    elif receivedNumber == 3:
        minibit.go(mbDirection.REVERSE, 100)
        basic.clear_screen()
    elif receivedNumber == 4:
        minibit.mb_bias(mbRobotDirection.LEFT, 80)
        minibit.go(mbDirection.FORWARD, 60)
        basic.clear_screen()
    elif receivedNumber == 5:
        minibit.mb_bias(mbRobotDirection.RIGHT, 80)
        minibit.go(mbDirection.FORWARD, 60)
        basic.clear_screen()
    elif receivedNumber == 6:
        minibit.rotate(mbRobotDirection.LEFT, 60)
        basic.clear_screen()
    elif receivedNumber == 7:
        minibit.rotate(mbRobotDirection.RIGHT, 60)
        basic.clear_screen()
radio.on_received_number(on_received_number)
