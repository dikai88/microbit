let light2 = 0
basic.forever(function () {
    if (ModuleWorld_Digital.Button(ModuleWorld_Digital.mwDigitalNum.P0P1, ModuleWorld_Digital.enButton.Press)) {
        basic.pause(100)
        while (ModuleWorld_Digital.Button(ModuleWorld_Digital.mwDigitalNum.P0P1, ModuleWorld_Digital.enButton.Press)) {
            basic.pause(1)
        }
        light2 += 1
        if (light2 > 1) {
            light2 = 0
        }
    }
    if (light2 == 0) {
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.OFF)
    } else {
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.Red)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.Yellow)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.Green)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.Pinkish)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.Cyan)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.Blue)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.White)
        basic.pause(500)
    }
})
