from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Port(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp port.
    """
    NAME_FROM = ['health', 'port', 'label']

    def __init__(self, *args):
        super().__init__(*args)
