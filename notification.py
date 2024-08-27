'''
Script to send Desktop Notifications
'''


import time
from plyer import notification




if __name__=="__main__":

    while True:
        notification.notify(
            title="ALERT!!",
            message="TAKE A BREAK PLEASE",
            timeout=30
        )
        time.sleep(3600)