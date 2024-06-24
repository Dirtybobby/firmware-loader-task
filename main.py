from __future__ import annotations

import logging
import signal
import sys
from inspect import FrameInfo


def main():
    steps = [
        ("Step 1: Enter device ID", input_device_id),
        ("Step 2: Choose subtype", choose_subtype),
        ("Step 3: Choose flasher", choose_flasher),
    ]

    for step_description, step_function in steps:
        success = False
        while not success:
            try:
                print(step_description)
                step_function()
                success = True
            except Exception as e:
                logging.error(f"Error during {step_description}: {e}")
                print(f"An error occurred: {e}. Please try again.")


def input_device_id():
    device_id = input("Enter device ID (3 or 4 byte hexadecimal): ")
    if len(device_id) not in [6, 8] or not all(c in '0123456789ABCDEFabcdef' for c in device_id):
        raise ValueError("Invalid device ID")


def choose_subtype():
    subtype = int(input("Enter the subtype (0-255): "))
    if not (0 <= subtype <= 255):
        raise ValueError("Invalid subtype")


def choose_flasher():
    flasher_type = input("Choose flasher (JLink/STLink): ").strip().lower()
    if flasher_type not in ['jlink', 'stlink']:
        raise ValueError("Invalid flasher type")


def sigint_handler(sig: int, frame: FrameInfo.frame):
    sys.tracebacklimit = 0
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    logging.basicConfig(
        filemode="a+", format='%(asctime)s %(levelname)s %(message)s',
        level=logging.INFO,
    )
    main()
