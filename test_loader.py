import pytest

from firmware_tools import Device, JLinkFlasher, STLinkFlasher
from loader import Loader


@pytest.fixture
def loader():
    return Loader()


@pytest.fixture
def mock_input(monkeypatch):
    inputs = []

    def mock_input(prompt):
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)
    return inputs


def test_get_device(loader):
    # Mocked device to test with
    device = Device(
        family='STM32', name='Device1',
        add_name='V1', processor="STM32F4",
    )
    assert isinstance(device, Device)


def test_get_firmware(loader, monkeypatch):
    # Mock the method to return a specific firmware path
    monkeypatch.setattr(
        loader, "get_firmware",
        lambda: "/path/to/firmware.hex",
    )
    firmware_path = loader.get_firmware()
    assert firmware_path == "/path/to/firmware.hex"


def test_input_device_id_valid(mock_input, loader):
    mock_input.extend(['A1B2C3'])
    device_id = loader.input_device_id()
    assert device_id == 'A1B2C3'


def test_input_device_id_invalid(mock_input, loader):
    mock_input.extend(['XYZ'])
    with pytest.raises(ValueError, match="Invalid device ID"):
        loader.input_device_id()


def test_choose_subtype_valid(mock_input, loader):
    mock_input.extend(['100'])
    subtype = loader.choose_subtype()
    assert subtype == 100


def test_choose_subtype_invalid(mock_input, loader):
    mock_input.extend(['300'])
    with pytest.raises(ValueError, match="Invalid subtype"):
        loader.choose_subtype()


@pytest.mark.parametrize(
    "flasher_input,expected_class", [
        ('jlink', JLinkFlasher),
        ('stlink', STLinkFlasher),
    ],
)
def test_choose_flasher_valid(mock_input, loader, flasher_input, expected_class):
    mock_input.extend([flasher_input])
    flasher = loader.choose_flasher()
    assert flasher == expected_class


def test_choose_flasher_invalid(mock_input, loader):
    mock_input.extend(['invalid'])
    with pytest.raises(ValueError, match="Invalid flasher type"):
        loader.choose_flasher()
