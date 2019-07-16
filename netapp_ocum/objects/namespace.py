from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Namespace(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp namespace.
    """
    NAME_FROM = ['health', 'namespace', 'label']

    def __init__(self, *args):
        super().__init__(*args)
