class NetApp_OCUM_ObjectBase(object):
    """
    Base class for NetApp objects as returned by the API.
    """
    def __init__(self, *args):
        self.json = args[0]

    def get(self, attr_key):
        """
        Get a specific key value from the object's JSON
        """
        return self.json.get(attr_key)

    def __iter__(self):
        """
        Iterate over each object attribute.
        """
        for k,v in self.json.items():
            yield(k,v)
