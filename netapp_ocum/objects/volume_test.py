import unittest
from netapp_ocum.objects.volume import NetApp_OCUM_Volume

class NetApp_OCUM_Object_Volume_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/volume.py`."""

    def test_volume_instance(self):
        """ Test creating an instance of `NetApp_OCUM_Volume` """
        volume = NetApp_OCUM_Volume({
            'id': 1
        })
        self.assertIsInstance(volume, NetApp_OCUM_Volume)
