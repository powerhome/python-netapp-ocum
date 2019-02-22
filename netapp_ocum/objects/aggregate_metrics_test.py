import unittest
from netapp_ocum.objects.aggregate_metrics import NetApp_OCUM_AggregateMetrics

class NetApp_OCUM_Object_AggregateMetrics_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/aggregate_metrics.py`."""

    def test_volume_metrics_instance(self):
        """ Test creating an instance of `NetApp_OCUM_AggregateMetrics` """
        volume = NetApp_OCUM_AggregateMetrics({
            'id': 1
        })
        self.assertIsInstance(volume, NetApp_OCUM_AggregateMetrics)
