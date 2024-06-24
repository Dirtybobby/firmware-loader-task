from __future__ import annotations

from itertools import zip_longest

from firmware_tools import Device, JLinkFlasher, STLinkFlasher


class Loader:
    def __init__(self) -> None:
        pass

    @staticmethod
    def show_devices_list(devices: list[Device]) -> None:
        half_length = (len(devices) + 1) // 2
        numerated = list(enumerate(devices))
        zipper = zip_longest(
            numerated[:half_length], numerated[half_length:], fillvalue=[
                None, None,
            ],
        )
        color_ending = '\033[0m'
        for (i1, dev_1), (i2, dev_2) in zipper:
            l_col_text = (
                f"{dev_1.family.value}{i1:3}."
                f" {dev_1.name + dev_1.add_name:50}{color_ending}"
            )
            if dev_2:
                r_col_text = (
                    f"{dev_2.family.value}{i2:3}."
                    f" {dev_2.name}{dev_2.add_name}{color_ending}"
                )
            else:
                r_col_text = ""
            print(f'{l_col_text}{r_col_text}')
        print()

    def get_device(self):
        pass

    def get_firmware(self):
        # TODO firmware file always have extension .hex and name in format ->
        #  [device_name][version][region][id_address][subtype][id_type].hex
        #  [DoorProtect][5.5.55.5][EU][0x0077AA][0][3B].hex example in firmware_for_test
        #  you can create you owm files for tests
        pass

    def input_device_id(self):
        # TODO device id can only be 3 or 4 byte, and it`s hexadecimal
        pass

    def color_to_flash(self):
        pass

    def choose_subtype(self):
        # TODO subtype only digital in range 0 - 255
        pass

    def choose_flasher(self) -> type[JLinkFlasher] | type[STLinkFlasher]:
        pass
