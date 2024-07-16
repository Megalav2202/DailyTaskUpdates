import time
import pygetwindow as gw
import pyautogui
from PIL import ImageGrab

def find_chrome_window():
    chrome_windows = [win for win in gw.getWindowsWithTitle('Google Chrome') if win.visible]
    return chrome_windows[0] if chrome_windows else None

def wait_for_webpage_load():
    time.sleep(5)
def take_website_screenshot(url):
    chrome_window = find_chrome_window()

    if chrome_window:
        chrome_window.activate()
        wait_for_webpage_load()
        left, top, right, bottom = chrome_window.left, chrome_window.top, chrome_window.right, chrome_window.bottom

        chrome_window_width = right - left
        chrome_window_height = bottom - top

        screenshot = ImageGrab.grab(bbox=(left, top, left + chrome_window_width, top + chrome_window_height))

        screenshot.save("web_screenshot.png")

        print("Screenshot saved successfully.")
    else:
        print("No visible Chrome window found.")

if __name__ == "__main__":
    url_to_capture = "https://www.capgemini.com/"  # Replace with the URL you want to capture
    take_website_screenshot(url_to_capture)



import cv2
import easyocr

def is_text_present(ocr_output, expected_text):
    for result in ocr_output:
        text = result[1]
        if expected_text.lower() in text.lower():
            return True
    return False


screenshot_path = 'web_screenshot.png'
screenshot = cv2.imread(screenshot_path)

reader = easyocr.Reader(['en'])
ocr_results = reader.readtext(screenshot)
expected_text = "TURBOCHARGING"
text_found = is_text_present(ocr_results, expected_text)


if text_found:
    print(f"Expected text '{expected_text}' found in the screenshot.")
else:
    print(f"Expected text '{expected_text}' not found in the screenshot.")


