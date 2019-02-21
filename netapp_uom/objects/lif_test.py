import unittest
from netapp_uom.objects.lif import NetApp_UOM_LIF

class NetApp_UOM_Object_LIF_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/lif.py`."""

    def test_lif_instance(self):
        """ Test creating an instance of `NetApp_UOM_LIF` """
        lif = NetApp_UOM_LIF({
            'id': 1
        })
        self.assertIsInstance(lif, NetApp_UOM_LIF)
