from pi_usb_gadget_controller.gadget_device import MouseGadgetDevice
import unittest
from unittest.mock import patch, mock_open, call


class TestMouseGadgetDevice(unittest.TestCase):

    def test_rel_mouse_event(self):
        device_name = "/dev/hidg0"
        open_mock_remote = mock_open()
        with patch("builtins.open", open_mock_remote) as mock_file:
            gadget = MouseGadgetDevice(device_name)
            gadget.handle("rel", "-10|20")
        open_mock_remote.assert_called_once_with(device_name, 'rb+')
        handle = open_mock_remote()
        handle.write.assert_called_once_with(bytes((0x01, 0x0, 0xf6, 0x14, 0x0, 0x0)))

    def test_abs_mouse_event(self):
        device_name = "/dev/hidg0"
        open_mock_remote = mock_open()
        with patch("builtins.open", open_mock_remote) as mock_file:
            gadget = MouseGadgetDevice(device_name)
            gadget.handle("abs", "5|20")
        open_mock_remote.assert_called_once_with(device_name, 'rb+')
        handle = open_mock_remote()
        handle.write.assert_called_once_with(bytes((0x02, 0x0, 0x05, 0x14, 0x0, 0x0)))

    def test_mouse_button_press(self):
        device_name = "/dev/hidg0"
        open_mock_remote = mock_open()
        with patch("builtins.open", open_mock_remote) as mock_file:
            gadget = MouseGadgetDevice(device_name)
            gadget.handle("down", "BTN_RIGHT")
        open_mock_remote.assert_called_once_with(device_name, 'rb+')
        handle = open_mock_remote()
        handle.write.assert_called_once_with(bytes((0x01, 0x02, 0x00, 0x00, 0x0, 0x0)))

    def test_mouse_button_press_two_buttons(self):
        device_name = "/dev/hidg0"
        open_mock_remote = mock_open()
        with patch("builtins.open", open_mock_remote) as mock_file:
            gadget = MouseGadgetDevice(device_name)
            gadget.handle("down", "BTN_RIGHT")
            gadget.handle("down", "BTN_LEFT")

        open_mock_remote.assert_called_with(device_name, 'rb+')
        handle = open_mock_remote()
        handle.write.assert_has_calls([
            call(bytes((0x01, 0x02, 0x00, 0x00, 0x0, 0x0))),
            call(bytes((0x01, 0x03, 0x00, 0x00, 0x0, 0x0)))
        ])

    def test_mouse_click_and_drag(self):
        device_name = "/dev/hidg0"
        open_mock_remote = mock_open()
        with patch("builtins.open", open_mock_remote) as mock_file:
            gadget = MouseGadgetDevice(device_name)
            gadget.handle("down", "BTN_LEFT")
            gadget.handle("rel", "-10|20")
            gadget.handle("up", "BTN_LEFT")

        open_mock_remote.assert_called_with(device_name, 'rb+')
        handle = open_mock_remote()
        handle.write.assert_has_calls([
            call(bytes((0x01, 0x01, 0x00, 0x00, 0x0, 0x0))),
            call(bytes((0x01, 0x01, 0xf6, 0x14, 0x0, 0x0))),
            call(bytes((0x01, 0x00, 0x00, 0x00, 0x0, 0x0)))
        ])


if __name__ == '__main__':
    unittest.main()
