radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        minibit.stop(mbStopMode.Brake)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (receivedNumber == 2) {
        minibit.mbBias(mbRobotDirection.Right, 0)
        minibit.mbBias(mbRobotDirection.Left, 0)
        minibit.go(mbDirection.Forward, 100)
        basic.clearScreen()
    } else if (receivedNumber == 3) {
        minibit.go(mbDirection.Reverse, 100)
        basic.clearScreen()
    } else if (receivedNumber == 4) {
        minibit.mbBias(mbRobotDirection.Left, 80)
        minibit.go(mbDirection.Forward, 60)
        basic.clearScreen()
    } else if (receivedNumber == 5) {
        minibit.mbBias(mbRobotDirection.Right, 80)
        minibit.go(mbDirection.Forward, 60)
        basic.clearScreen()
    }
})
radio.setGroup(144)
radio.setTransmitPower(7)
minibit.ledBrightness(0)
