from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Event(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp event.
    """
    def __init__(self, *args):
        super().__init__(*args)
