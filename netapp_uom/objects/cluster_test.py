import unittest
from netapp_uom.objects.cluster import NetApp_UOM_Cluster

class NetApp_UOM_Object_Cluster_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/cluster.py`."""

    def test_cluster_instance(self):
        """ Test creating an instance of `NetApp_UOM_Cluster` """
        cluster = NetApp_UOM_Cluster({
            'id': 1
        })
        self.assertIsInstance(cluster, NetApp_UOM_Cluster)
