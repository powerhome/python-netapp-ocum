import unittest
from netapp_ocum.objects.node import NetApp_OCUM_Node

class NetApp_OCUM_Object_Node_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/node.py`."""

    def test_node_instance(self):
        """ Test creating an instance of `NetApp_OCUM_Node` """
        node = NetApp_OCUM_Node({
            'id': 1
        })
        self.assertIsInstance(node, NetApp_OCUM_Node)
