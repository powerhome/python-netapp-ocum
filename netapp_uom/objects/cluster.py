from netapp_uom.objects.base import NetApp_UOM_ObjectBase

class NetApp_UOM_Cluster(NetApp_UOM_ObjectBase):
    """
    Class representing a single NetApp cluster.
    """
    def __init__(self, object_json):
        super().__init__(object_json)
