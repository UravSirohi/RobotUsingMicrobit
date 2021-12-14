def on_received_number(receivedNumber):
    receivedNumber = receivedNumber / password
    if receivedNumber == 1:
        minibit.stop(mbStopMode.BRAKE)
    elif receivedNumber == 2:
        minibit.mb_bias(mbRobotDirection.RIGHT, 0)
        minibit.mb_bias(mbRobotDirection.LEFT, 0)
        minibit.go(mbDirection.FORWARD, 100)
    elif receivedNumber == 3:
        minibit.go(mbDirection.REVERSE, 100)
    elif receivedNumber == 4:
        minibit.mb_bias(mbRobotDirection.LEFT, 80)
        minibit.go(mbDirection.FORWARD, 60)
    elif receivedNumber == 5:
        minibit.mb_bias(mbRobotDirection.RIGHT, 80)
        minibit.go(mbDirection.FORWARD, 60)
    else:
        basic.show_icon(IconNames.ANGRY)
radio.on_received_number(on_received_number)
 
def on_received_value(name, value):
    if name == "" + str(password):
        password == value
    else:
        basic.show_icon(IconNames.ANGRY)
radio.on_received_value(on_received_value)
 
password = 0
radio.set_group(144)
radio.set_transmit_power(7)
minibit.led_brightness(0)
password = 399
 
