import unittest
from netapp_ocum.objects.cluster import NetApp_OCUM_Cluster

class NetApp_OCUM_Object_Cluster_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/cluster.py`."""

    def test_cluster_instance(self):
        """ Test creating an instance of `NetApp_OCUM_Cluster` """
        cluster = NetApp_OCUM_Cluster({
            'id': 1
        })
        self.assertIsInstance(cluster, NetApp_OCUM_Cluster)
