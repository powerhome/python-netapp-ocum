from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_LUN(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp LUN.
    """
    NAME_FROM = ['health', 'lun', 'label']

    def __init__(self, *args):
        super().__init__(*args)
