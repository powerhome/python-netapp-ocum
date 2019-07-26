from netapp_ocum.objects.base import NetApp_OCUM_ObjectBase

class NetApp_OCUM_SVM(NetApp_OCUM_ObjectBase):
    """
    Class representing a single NetApp SVM (storage virtual machine).
    """
    NAME_FROM = ['health', 'svm', 'label']

    def __init__(self, *args):
        super().__init__(*args)
