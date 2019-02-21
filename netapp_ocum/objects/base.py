class NetApp_OCUM_ObjectBase(object):
    """
    Base class for NetApp objects as returned by the API.
    """
    def __init__(self, json):
        self.json = json

    def get(self, attr_key):
        return self.json.get(attr_key)

    def __iter__(self):
        for k,v in self.json.items():
            yield(k,v)
