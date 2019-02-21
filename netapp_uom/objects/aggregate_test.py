import unittest
from netapp_uom.objects.aggregate import NetApp_UOM_Aggregate

class NetApp_UOM_Object_Aggregate_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/aggregate.py`."""

    def test_aggregate_instance(self):
        """ Test creating an instance of `NetApp_UOM_Aggregate` """
        aggregate = NetApp_UOM_Aggregate({
            'id': 1
        })
        self.assertIsInstance(aggregate, NetApp_UOM_Aggregate)
