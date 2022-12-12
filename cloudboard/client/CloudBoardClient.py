from threading import Thread
from CopyHandler import CopyHandler
from PasteHandler import PasteHandler
import pyperclip
import keyboard

copyhandler = CopyHandler(None)
pastehandler = PasteHandler()

host = "34.102.116.94"
port = "5000"

class CopyDaemon(Thread):
    def run(self):
        while True:
            d = pyperclip.waitForNewPaste()
            if d:
                copyhandler.update_local_state()
                copyhandler.update_remote_state()

class PasteDaemon(Thread):
    def run(self):
        keyboard.add_hotkey('esc', lambda: keyboard.write(pastehandler.cloud_paste(copyhandler.timestamp)))
        keyboard.wait()

if __name__=="__main__":
    copydaemon = CopyDaemon(host, port)
    pastedaemon = PasteDaemon(host, port)

    copydaemon.start()
    pastedaemon.start()
