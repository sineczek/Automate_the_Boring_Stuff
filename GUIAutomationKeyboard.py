import pyautogui

# dzięki ; możemy w jednej linii odpalić 2 polecenia

pyautogui.click(100, 100);
pyautogui.typewrite('Hello World!\n')  # przesyłanie klawiszy

pyautogui.typewrite('Hello World!\n', interval=0.2)  # z opóźnieniem

pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y', 'right', 'right', '\n'], interval=0.2)

#pyautogui.KEYBOARD_KEYS lista "komend"

pyautogui.press('ENTER') # pojedynczy znak lub komenda

pyautogui.hotkey('ctrl','o') # czyli ctrl + o