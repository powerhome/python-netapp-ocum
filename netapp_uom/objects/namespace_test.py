import unittest
from netapp_uom.objects.namespace import NetApp_UOM_Namespace

class NetApp_UOM_Object_Namespace_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/namespace.py`."""

    def test_namespace_instance(self):
        """ Test creating an instance of `NetApp_UOM_Namespace` """
        namespace = NetApp_UOM_Namespace({
            'id': 1
        })
        self.assertIsInstance(namespace, NetApp_UOM_Namespace)
