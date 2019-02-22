import unittest
from netapp_ocum.objects.volume_metrics import NetApp_OCUM_VolumeMetrics

class NetApp_OCUM_Object_VolumeMetrics_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/volume_metrics.py`."""

    def test_volume_metrics_instance(self):
        """ Test creating an instance of `NetApp_OCUM_VolumeMetrics` """
        volume = NetApp_OCUM_VolumeMetrics({
            'id': 1
        })
        self.assertIsInstance(volume, NetApp_OCUM_VolumeMetrics)
