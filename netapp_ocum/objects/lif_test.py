import unittest
from netapp_ocum.objects.lif import NetApp_OCUM_LIF

class NetApp_OCUM_Object_LIF_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/lif.py`."""

    def test_lif_instance(self):
        """ Test creating an instance of `NetApp_OCUM_LIF` """
        lif = NetApp_OCUM_LIF({
            'id': 1
        })
        self.assertIsInstance(lif, NetApp_OCUM_LIF)
