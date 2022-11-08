import time
import pyperclip
import uuid

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
        self.timestamp = float('-inf')
        pass

    def update_local_state(self):
        self.uid = uuid.uuid4().hex # COPY id
        self.data = pyperclip.paste()
        self.timestamp = float('-inf')

    def update_remote_state(self):
        # todo: get timestamp from cloud
        if cld_timestamp < self.timestamp:
            

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