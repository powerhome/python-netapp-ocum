from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_Relationship(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp Volume Protection Relationship.
    """
    def __init__(self, *args):
        super().__init__(*args)
