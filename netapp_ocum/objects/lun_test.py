import unittest
from netapp_ocum.objects.lun import NetApp_OCUM_LUN

class NetApp_OCUM_Object_LUN_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/lun.py`."""

    def test_lun_instance(self):
        """ Test creating an instance of `NetApp_OCUM_LUN` """
        lun = NetApp_OCUM_LUN({
            'id': 1
        })
        self.assertIsInstance(lun, NetApp_OCUM_LUN)
