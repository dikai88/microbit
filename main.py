light2 = 1

def on_forever():
    global light2
    if ModuleWorld_Digital.button(ModuleWorld_Digital.mwDigitalNum.P0P1,
        ModuleWorld_Digital.enButton.PRESS):
        basic.pause(100)
        while ModuleWorld_Digital.button(ModuleWorld_Digital.mwDigitalNum.P0P1,
            ModuleWorld_Digital.enButton.PRESS):
            basic.pause(1)
        light2 += 1
        if light2 > 1:
            light2 = 0
    if light2 == 0:
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.OFF)
    else:
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.RED)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.YELLOW)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.GREEN)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.CYAN)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.BLUE)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.PINKISH)
        basic.pause(500)
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.WHITE)
        basic.pause(500)
basic.forever(on_forever)
