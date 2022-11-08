import time
import pyperclip
import uuid

class CloudBoardClient:
    """
    Handles copy operation
    """
    def __init__(self):
        """
        1. Maintain a unique ID for each client
        2. Maintain a unique ID for each client device
        3. Maintain a unique ID for each copy operation
        """
        self.client_uid = None
        self.device_uid = None
        self.copy_uid = None
        self.copy_data = None
        self.copy_timestamp = float('-inf')
        self.up_to_date = False
        pass

    def update_local_state(self):
        data = pyperclip.paste()
        if self.validate(data):
            self.copy_uid = uuid.uuid4().hex # COPY id
            self.copy_data = data
            self.copy_timestamp = time.time()

    def update_remote_state(self):
        # todo: get timestamp from cloud
        if cloud_timestamp < self.timestamp:
            # todo: send local data, timestamp and uid
            

    def cloud_copy(self):
        """
        Executes the following steps:
            1. Saves current timestamp
            2. Fetches the timestamp of latest COPY on the server
                - if current time is newer, updates timestamp on server along with client_id            
        """
        self.update_local_state()
        self.update_remote_state()
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