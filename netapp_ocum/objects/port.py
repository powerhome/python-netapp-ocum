from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Port(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp port.
    """
    def __init__(self, *args):
        super().__init__(*args)
