class NetApp_OCUM_Settings(object):
    """
    Class object for storing API connection settings.
    """
    def __init__(self, **kwargs):
        self.api_host     = kwargs.get('api_host')
        self.api_user     = kwargs.get('api_user')
        self.api_password = kwargs.get('api_password')
        self.api_port     = kwargs.get('api_port')
        self.verify_ssl   = kwargs.get('verify_ssl')
