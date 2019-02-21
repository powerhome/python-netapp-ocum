import unittest
from netapp_ocum.objects.svm import NetApp_OCUM_SVM

class NetApp_OCUM_Object_SVM_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/svm.py`."""

    def test_svm_instance(self):
        """ Test creating an instance of `NetApp_OCUM_SVM` """
        svm = NetApp_OCUM_SVM({
            'id': 1
        })
        self.assertIsInstance(svm, NetApp_OCUM_SVM)
