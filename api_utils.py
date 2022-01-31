import requests

from requests.exceptions import HTTPError

class APIConnector:
    def __init__(self, server_address : str, server_port : str, path : str):
        self.server_address = server_address
        self.server_port = server_port
        self.path = path

        self.response_json = {}

        self.base_path = server_address + ":" + server_port + "/" + (path if path[0] != "/" else path[1:])

        if self.base_path[-1] != "/":
            self.base_path += "/"

    def make_request(self, *params):
        param_str = "/".join([str(param) for param in params]) + "/"

        try:
            response = requests.get(self.base_path + param_str)
        except HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as error:
            print(f"Other error occurred: {error}")
        else:
            self.response_json = response.json()

    def get_data(self):
        return self.response_json

def main():
    pass 

if __name__ == "__main__":
    main()