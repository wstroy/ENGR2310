# Import packages
# ===============
import rcpy
from rcpy.button import mode, pause
from rcpy.led import red, green


# Turns on the red or green LEDs depending on which button is pressed
# ===================================================================
def PushLights():
    # Get rcpy running
    rcpy.set_state(rcpy.RUNNING)

    # Welcome message
    print("=" * 65)
    print("Welcome to PressyLights!")
    print("Press <PAUSE> to turn on the red light, or <MODE> to turn on the green light.")
    print("Press both <PAUSE> and <MODE> to exit.")
    print("-" * 65)

    # Main loop
    while not (mode.is_pressed() and pause.is_pressed()):

        if pause.is_pressed():
            red.on()
            green.off()

        elif mode.is_pressed():
            red.off()
            green.on()

    # Exit message
    print("Bye Beaglebone!")
    print("=" * 65)
    red.off()
    green.off()


# Main execution
# ==============
if __name__ == "__main__":
    PushLights()