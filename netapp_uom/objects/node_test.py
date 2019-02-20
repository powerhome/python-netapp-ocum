import unittest
from netapp_uom.objects.node import NetApp_UOM_Node

class NetApp_UOM_Object_Node_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/node.py`."""

    def test_node_instance(self):
        """ Test creating an instance of `NetApp_UOM_Node` """
        node = NetApp_UOM_Node({
            'id': 1
        })
        self.assertIsInstance(node, NetApp_UOM_Node)
