import unittest
from netapp_ocum.objects.lif import NetApp_OCUM_LIF

class NetApp_OCUM_Object_Interface_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/interface.py`."""

    def test_interface_instance(self):
        """ Test creating an instance of `NetApp_OCUM_Interface` """
        lif = NetApp_OCUM_Interface({
            'id': 1
        })
        self.assertIsInstance(lif, NetApp_OCUM_Interface)
