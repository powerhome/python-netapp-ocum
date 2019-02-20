import unittest
from netapp_uom.objects.volume import NetApp_UOM_Volume

class NetApp_UOM_Object_Volume_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/volume.py`."""

    def test_volume_instance(self):
        """ Test creating an instance of `NetApp_UOM_Volume` """
        volume = NetApp_UOM_Volume({
            'id': 1
        })
        self.assertIsInstance(volume, NetApp_UOM_Volume)
