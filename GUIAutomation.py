import pyautogui

"""
0x0 to lewy góry róg
"""

print(pyautogui.size())  # zwraca rozdzielczość ekranu (ciekawe co przy 2) TODO: jutro sprawdzić

width, height = pyautogui.size()  # przydzielenie do zmiennych

print(pyautogui.position())  # lokalizacja kursora aktualna

"""
pyautogui.moveTo(10, 10) # "teleport" kursoro
pyautogui.moveTo(1000, 500, duration=1.5) # powolniejszy ruch

pyautogui.moveRel(200,0) # rusz kursor o 200px w prawo
pyautogui.moveRel(200,-400) # - aby w górę"""

pyautogui.click(1415, 14)  # kliknij w napis Help (PyCharm na połowie ekranu)

pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()

# pyautogui.displayMousePosition() # tylko w terminalu do zbierania lokalizacji


# gdyby coś nawaliło myszka na 0x0 aby przerwać
