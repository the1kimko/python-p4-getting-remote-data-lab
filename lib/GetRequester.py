import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url) #sends a GET request to the URL
        return response.content # returs the response body as raw bytes

    def load_json(self):
        response_body = self.get_response_body() # retrieves the response body as raw bytes
        return json.loads(response_body) # Parses the raw byte content as JSON and returns it