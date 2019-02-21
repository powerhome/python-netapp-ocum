import unittest
from netapp_ocum.objects.port import NetApp_OCUM_Port

class NetApp_OCUM_Object_Port_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/port.py`."""

    def test_port_instance(self):
        """ Test creating an instance of `NetApp_OCUM_Port` """
        port = NetApp_OCUM_Port({
            'id': 1
        })
        self.assertIsInstance(port, NetApp_OCUM_Port)
