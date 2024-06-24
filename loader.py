from firmware_tools import Device, JLinkFlasher, STLinkFlasher

class Loader:
    def __init__(self):
        pass

    def input_device_id(self) -> str:
        device_id = input("Enter device ID (3 or 4 byte hexadecimal): ")
        if len(device_id) not in [6, 8] or not all(c in '0123456789ABCDEFabcdef' for c in device_id):
            raise ValueError("Invalid device ID")
        return device_id

    def choose_subtype(self) -> int:
        subtype = int(input("Enter the subtype (0-255): "))
        if not (0 <= subtype <= 255):
            raise ValueError("Invalid subtype")
        return subtype

    def choose_flasher(self):
        flasher_type = input("Choose flasher (JLink/STLink): ").strip().lower()
        if flasher_type == 'jlink':
            return JLinkFlasher
        elif flasher_type == 'stlink':
            return STLinkFlasher
        else:
            raise ValueError("Invalid flasher type")

    def get_device(self, device_id: str, subtype: int) -> Device:
        # This is a placeholder for the actual device fetching logic
        return Device(family='STM32', name='Device1', add_name='V1')

    def get_firmware(self) -> str:
        # This should return the path to the firmware file
        return input("Enter the path to the firmware file: ")

    def flash_device(self, device: Device, firmware_path: str, flasher):
        # This is a placeholder for the actual flashing logic
        print(f"Flashing {device.name} with firmware from {firmware_path} using {flasher.__name__}")
