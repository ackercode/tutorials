import pyautogui as spam
import time

limite_msg = input("Enter n de msgs: ")
msg = input("Coloque a msg: ")

i = 0

time.sleep(5)

while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")

i+=1
