import unittest
from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Object_Base_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/base.py`."""

    def test_base_instance(self):
        """ Test creating an instance of `NetApp_OCUM_ObjectBase` """
        base_object = NetApp_OCUM_ObjectBase({
            'id': 1
        })
        self.assertIsInstance(base_object, NetApp_OCUM_ObjectBase)
