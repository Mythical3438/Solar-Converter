#! bin/bash/env python3
# By: Philip Schorr 07.19.2022
# Used to figure out how many solar panels are needed to run a certain device

def welcome_screen():
    print("   _____       __              ______                           __           ")
    print("  / ___/____  / /___ ______   / ____/___  ____ _   _____  _____/ /____  _____")
    print("  \__ \/ __ \/ / __ `/ ___/  / /   / __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/")
    print(" ___/ / /_/ / / /_/ / /     / /___/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    ") 
    print("/____/\____/_/\__,_/_/      \____/\____/_/ /_/|___/\___/_/   \__/\___/_/     ")  
    print("           Figure out your solar panel array's total output!                 ")


def get_watts(volts, amps):
    watts = amps * volts
    print(watts)


def get_amps(volts,watts):
    amps = watts / volts
    print(amps)


def get_volts(amps, watts):
    volts = watts / amps
    print(volts)


def solar_output(panel_size, qty): # panel_size = watts per hour 
    total = panel_size * qty
    print("\n Solar panels maximum output per hour @ 12v:")
    print("\nAmps per hour: ")
    get_amps(12, total)
    print("\nWatts per hour: ")
    print(total)
    print(f"\n For: {qty}x @ {panel_size}watt Solar Panels \n")

if __name__ == "__main__":
    welcome_screen()
    panel_size = int(input("Enter the Watt size of your solar pan? :"))
    qty = int(input("Enter the number of solar panels? :"))
    solar_output(panel_size, qty)