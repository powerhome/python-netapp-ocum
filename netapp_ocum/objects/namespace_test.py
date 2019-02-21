import unittest
from netapp_ocum.objects.namespace import NetApp_OCUM_Namespace

class NetApp_OCUM_Object_Namespace_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/namespace.py`."""

    def test_namespace_instance(self):
        """ Test creating an instance of `NetApp_OCUM_Namespace` """
        namespace = NetApp_OCUM_Namespace({
            'id': 1
        })
        self.assertIsInstance(namespace, NetApp_OCUM_Namespace)
