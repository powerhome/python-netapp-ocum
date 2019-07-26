from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Cluster(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp cluster.
    """
    NAME_FROM = ['health', 'cluster', 'label']

    def __init__(self, *args):
        super().__init__(*args)
