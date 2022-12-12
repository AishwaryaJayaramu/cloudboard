import time
import pyperclip
import uuid
import requests
import datetime


class CopyHandler:
    """
    Handles copy operation
    """

    def __init__(self, client):
        """
        1. Maintain a unique ID for each copy operation
        """
        self.copy_uid = None
        self.data = None
        self.timestamp = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
        pass

    def update_local_state(self):
        self.uid = uuid.uuid4().hex  # COPY id
        self.data = pyperclip.paste()
        self.timestamp = float("-inf")

    def update_remote_state(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYXNkIn0.QBG24x1D26mjFpOCLxOit72m8jt67HYI9dBmpBuBepc"
        list_clipboards_url = "http://127.0.0.1:5000/list_clipboards"
        copy_data_url = "http://127.0.0.1:5000/copy_data"
        query_data = {
            "device_id": token
        }
        copy_data = {
            "device_id": token,
            "copy_data": self.data,
            "timestamp": self.timestamp,
            "is_file": False
        }
        response = requests.get(list_clipboards_url, json=query_data)
        json_response = response.json()
        if response.status_code == 200:
            if len(json_response["clipboards"]) > 0:
                cld_timestamp = response.json()["clipboards"][0]["copied_at"]
                if cld_timestamp < self.timestamp:
                    response = requests.post(copy_data_url, json=copy_data)
                else:
                    pass
            else:
                response = requests.post(copy_data_url, json=copy_data)

    def cloud_copy(self):
        """
        Executes the following steps:
            1. Saves current timestamp
            2. Fetches the timestamp of latest COPY on the server
                - if current time is newer, updates timestamp on server along with client_id
        """
        data = pyperclip.paste()

        pass

    def validate(self):
        """
        Executes the following steps:
            1. Check validity of copy data in case
                - size is too big
                - data is of a type that cannot be sent
            2. In case data is invalid
                - keep local data as is
                - keep server data as is
        """
        pass

    def get_copy_state(self):
        pass

    def send_copy_state(self):
        """
        Executes the following steps:
            1. Listen to server requests for data
            2. Send contents of local clipboard if requested
        """
        pass
