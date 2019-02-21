import requests

class NetApp_OCUM_HTTP(object):
    """
    Class object for handling HTTP requests/responses for the OCUM.
    """
    def __init__(self, settings):
        self.settings = settings

    def GET(self, path, params={}):
        """
        Make a GET request to the OCUM API method with an optional filter.
        """
        request_url = 'https://{0}:{1}/rest/{2}'.format(
            self.settings.api_host,
            self.settings.api_port,
            path
        )

        # Make the API request
        response = requests.get(request_url,
            auth    = (self.settings.api_user, self.settings.api_password),
            verify  = self.settings.verify_ssl,
            headers = self.settings.headers,
            params  = params
        )

        # Request failed
        if not int(response.status_code) == 200:
            raise Exception('Failed to GET {0}: {1}'.format(request_url, response.json()))
        return response.json()
