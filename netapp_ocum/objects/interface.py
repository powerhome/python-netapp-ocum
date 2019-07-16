from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Interface(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp interface.
    """
    NAME_FROM = ['health', 'lif', 'label']

    def __init__(self, *args):
        super().__init__(*args)
