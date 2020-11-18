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
    def __isvalid(phone_no) -> bool:
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
    def __send(phone_no: str, message: str):
        url = f"https://web.whatsapp.com/send?phone={phone_no}&text={message}"
        webbrowser.open(url)
        time.sleep(10)
        pyautogui.press("enter")

    @staticmethod
    def send_quick_message(phone_no: str, message: str) -> None:
        '''
        Send a quick whatsapp message.
        '''
        if not Whatsapp.__isvalid(phone_no):
            return print("Invalid Number!")

        Whatsapp.__send(phone_no, message)

    @staticmethod
    def send_scheduled_message(phone_no: str, hour: int, minute: int, message: str) -> None:
        '''
        Send a scheduled whatsapp message
        '''
        if not Whatsapp.__isvalid(phone_no):
            return print("Invalid Number!")

        now = datetime.now()
        year, month, day = now.year, now.month, now.day
        send_time = datetime(year, month, day, hour, minute)
        time_gap = send_time - now
        wait_time = time_gap.total_seconds()
        if wait_time < 10:
            return print("Can't send messages in past!")

        print(f"Message will be sent after {wait_time} seconds")
        time.sleep(wait_time-10)
        Whatsapp.__send(phone_no, message)

    def send_files(self, file):
        pass


if __name__ == "__main__":
    number = 'phone_no'
    msg = 'happy birthday'
    Whatsapp.send_quick_message(number, msg)
    Whatsapp.send_scheduled_message(number, 10, 22, msg)
