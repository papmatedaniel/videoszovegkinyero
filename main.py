import pyautogui
import time
import webbrowser

# Nyisd meg a Google Képkeresőt a böngészőben
webbrowser.open('https://images.google.com/')

# Várj, amíg a böngésző megnyílik
time.sleep(5)

# Kattints a kamera ikonra a képkeresőn
camera_icon_position = pyautogui.locateOnScreen('/workspaces/videoszovegkinyero/camera_icon.png')
if camera_icon_position:
    pyautogui.click(camera_icon_position)
else:
    print("camera_icon.png not found")

# Várj egy kicsit a feltöltés ablak megnyitásához
time.sleep(2)

# Kattints a 'Kép feltöltése' fülre
upload_tab_position = pyautogui.locateOnScreen('/workspaces/videoszovegkinyero/upload_tab.png')
if upload_tab_position:
    pyautogui.click(upload_tab_position)
else:
    print("upload_tab.png not found")

# Várj egy kicsit a feltöltés gomb megnyitásához
time.sleep(2)

# Írd be a fájl útvonalát és nyomd meg az Entert
pyautogui.write('/workspaces/videoszovegkinyero/image.png')
pyautogui.press('enter')

# Várj, amíg a kép feltöltődik és a keresési eredmények megjelennek
time.sleep(5)

# Kattints a 'Szöveg kivonása' (Text) opcióra a képkeresési eredmények között
text_option_position = pyautogui.locateOnScreen('/workspaces/videoszovegkinyero/text_option.png')
if text_option_position:
    pyautogui.click(text_option_position)
else:
    print("text_option.png not found")

# Várj egy kicsit a szöveg kivonásához
time.sleep(2)

# Kattints a 'Szöveg másolása' opcióra
copy_text_position = pyautogui.locateOnScreen('/workspaces/videoszovegkinyero/copy_text.png')
if copy_text_position:
    pyautogui.click(copy_text_position)
else:
    print("copy_text.png not found")

# A szöveg most már a vágólapon van, beilleszthető egy fájlba vagy további feldolgozásra
