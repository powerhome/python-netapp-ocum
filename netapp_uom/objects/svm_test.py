import unittest
from netapp_uom.objects.svm import NetApp_UOM_SVM

class NetApp_UOM_Object_SVM_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/svm.py`."""

    def test_svm_instance(self):
        """ Test creating an instance of `NetApp_UOM_SVM` """
        svm = NetApp_UOM_SVM({
            'id': 1
        })
        self.assertIsInstance(svm, NetApp_UOM_SVM)
