import unittest
from netapp_uom.objects.base import NetApp_UOM_ObjectBase

class NetApp_UOM_Object_Base_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/base.py`."""

    def test_base_instance(self):
        """ Test creating an instance of `NetApp_UOM_ObjectBase` """
        base_object = NetApp_UOM_ObjectBase({
            'id': 1
        })
        self.assertIsInstance(base_object, NetApp_UOM_ObjectBase)
