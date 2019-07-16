from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Node(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp node.
    """
    NAME_FROM = ['health', 'node', 'label']

    def __init__(self, *args):
        super().__init__(*args)
