import pyautogui

screenshot = pyautogui.screenshot()  # robi zrzut ekranu w postaci obrazu "pillow"

# pyautogui.screenshot('example.png') # zapisuje srzut ekranu
# obrazek musi być idealny, na dużym ekranie może to trwać nawet ok 1 sec.
winlogo = pyautogui.locateOnScreen('winlogo.png')  # znajdowanie czegoś na ekranie image recognition
# zwracana jest lokalizacja x, y, width, height

winlogo1 = pyautogui.locateCenterOnScreen('winlogo.png')  # zwraca środek
print(winlogo)
print(winlogo1)
