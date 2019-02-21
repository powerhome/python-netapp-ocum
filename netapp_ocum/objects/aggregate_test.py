import unittest
from netapp_ocum.objects.aggregate import NetApp_OCUM_Aggregate

class NetApp_OCUM_Object_Aggregate_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/aggregate.py`."""

    def test_aggregate_instance(self):
        """ Test creating an instance of `NetApp_OCUM_Aggregate` """
        aggregate = NetApp_OCUM_Aggregate({
            'id': 1
        })
        self.assertIsInstance(aggregate, NetApp_OCUM_Aggregate)
