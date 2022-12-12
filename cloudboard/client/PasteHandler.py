import pyperclip
import uuid
import requests

class PasteHandler:
    """
    Handles paste operation.
    """
    def __init__(self):
        # self.uid = uuid.uuid4().hex # client_id
        pass

    def cloud_paste(self, local_copy_timestamp):
        print("I am here")
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiZGV2aWNlIDEifQ.kKOl0Y5L9H7DjNYr6zAdizhtsReUd50C8WvpYHlobSI"
        list_clipboards_url = "http://127.0.0.1:5000/list_clipboards"
        paste_data_url = "http://127.0.0.1:5000/paste_data"
        query_data = {
            "device_id": token
        }
        response = requests.get(list_clipboards_url, json=query_data)
        json_response = response.json()
        paste_response = None
        if response.status_code == 200:
            if len(json_response["clipboards"]) > 0:
                cld_timestamp = response.json()["clipboards"][0]["copied_at"]
                if cld_timestamp >= local_copy_timestamp:
                    paste_response = requests.get(paste_data_url, json=query_data)
                else:
                    pass
            else:
                paste_response = requests.get(paste_data_url, json=query_data)
            json_paste_response = paste_response.json()
        if paste_response and "copied_text" in json_paste_response:
            return(json_paste_response["copied_text"])
        

    def get_copy_state(self):
        pass