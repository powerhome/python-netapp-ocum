import unittest
from netapp_uom.objects.lun import NetApp_UOM_LUN

class NetApp_UOM_Object_LUN_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/lun.py`."""

    def test_lun_instance(self):
        """ Test creating an instance of `NetApp_UOM_LUN` """
        lun = NetApp_UOM_LUN({
            'id': 1
        })
        self.assertIsInstance(lun, NetApp_UOM_LUN)
