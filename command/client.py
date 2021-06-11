"The Command Pattern Use Case Example. A smart light Switch"
from light import Light
from switch import Switch
from switch_on_command import SwitchOnCommand
from switch_off_command import SwitchOffCommand

LIGHT = Light()

SWITCH_ON = SwitchOnCommand(LIGHT)
SWITCH_OFF = SwitchOffCommand(LIGHT)

SWITCH = Switch()
SWITCH.register("ON", SWITCH_ON)
SWITCH.register("OFF", SWITCH_OFF)

SWITCH.execute("ON")
SWITCH.execute("OFF")
SWITCH.execute("ON")
SWITCH.execute("OFF")

SWITCH.show_history()

SWITCH.replay_last(2)