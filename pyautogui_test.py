import pyautogui
import keyboard

pyautogui.FAILSAFE = True
pyautogui.sleep(3)

while not keyboard.is_pressed("esc"):
        pyautogui.click(button='left', duration=0.5)

print(pyautogui.confirm(text='Aboba?', title='Abeme?', buttons=['Yesss', "No."]))