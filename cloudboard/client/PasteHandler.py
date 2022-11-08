import pyperclip
import uuid

class PasteHandler:
    """
    Handles paste operation.
    """
    def __init__(self):
        self.uid = uuid.uuid4().hex # client_id
        pass

    def cloud_paste(self):
        """
        Executes the following steps:
            1. Check timestamp of latest local COPY operation
            2. Fetch the timestamp of latest COPY on the server
                - if local COPY is the newest COPY:
                    + paste from local clipboard
                - else:
                    + fetch the latest COPY data from the server
                    + update the local clipboard with the data
                    + update the local timestamp
        """
        pass

    def get_copy_state(self):
        pass