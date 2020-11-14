import phonenumbers
from phonenumbers import NumberParseException
import pyautogui
import webbrowser
import time
from datetime import datetime
from datetime import timedelta

class InvalidPhonenumber(Exception):
    pass

class Whatsapp:
    def __init__(self):
        pass
    
    @staticmethod
    def isvalid(phone_no) -> bool:
        '''
        Check if a phone number is valid or not.
        '''

        try:
            ph = phonenumbers.parse(phone_no)
            if not phonenumbers.is_valid_number(ph):
                raise InvalidPhonenumber("Not a valid phone number")
            return True
        except (NumberParseException, InvalidPhonenumber):
            return False

    @staticmethod
    def send(phone_no: str, message: str):
        url = f"https://web.whatsapp.com/send?phone={phone_no}&text={message}"
        webbrowser.open(url)
        time.sleep(5)
        pyautogui.press("enter")
        

    def send_quick_message(self, phone_no: str, message: str) -> None:
        '''
        Send a quick whatsapp message.
        '''
        if not Whatsapp.isvalid(phone_no):
            return print("Invalid Number!")

        Whatsapp.send(phone_no, message)
    
    def send_timed_message(self, phone_no: str, hour: int, minute: int, message: str) -> None:
        now = datetime.now()
        year, month, day = now.year, now.month, now.day
        send_time = datetime(year, month, day, hour, minute)
        time_gap = send_time - now
        wait_time = time_gap.total_seconds()
        if wait_time < 0:
            return print("Can't send messages in past!")
        
        print(f"Sleeping for {wait_time} seconds.")
        time.sleep(wait_time-10)
        Whatsapp.send(phone_no, message)
    
    def send_files(self, file):
        pass    
