import cv2
import numpy as np
import pyautogui
import time

def click_on_image(image_path, confidence=0.7, max_attempts=None, delay=0.6):
    pattern = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if pattern.shape[-1] == 4:
        pattern = cv2.cvtColor(pattern, cv2.COLOR_BGRA2BGR)

    attempts = 0

    while max_attempts is None or attempts < max_attempts:
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        if screenshot.shape[-1] == 4:
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

        result = cv2.matchTemplate(screenshot, pattern, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > confidence:
            top_left = max_loc
            bottom_right = (top_left[0] + pattern.shape[1], top_left[1] + pattern.shape[0])
            print(f"Padrão encontrado nas coordenadas: {top_left}, {bottom_right}")

            mid_point = ((top_left[0] + bottom_right[0]) // 2, (top_left[1] + bottom_right[1]) // 2)

            time.sleep(delay)
            pyautogui.click(mid_point[0], mid_point[1])
            print(f"Clicou na imagem {image_path}.")
            return True

        print(f"Padrão não encontrado na tela. Tentando novamente...")
        time.sleep(delay)
        attempts += 1

    print(f"Limite de tentativas atingido para a imagem {image_path}. A imagem não foi encontrada.")
    return False

def wait_for_image(image_path, timeout=None):
    start_time = time.time()

    while timeout is None or time.time() - start_time < timeout:
        if pyautogui.locateOnScreen(image_path, confidence=0.7) is not None:
            return True
        time.sleep(1)

    print(f"Timeout: A imagem {image_path} não foi encontrada.")
    return False

play_image_path = r'img\play.png'
confirmar_image_path = r'img\confirmar.png'
confirmar2_image_path = r'img\confirmar2.png'
encontrar_image_path = r'img\encontrar.png'
aceitar_image_path = r'img\aceitar.png'
pesquisar_image_path = r'img\pesquisar.png'
coop_image_path = r'img\coop.png'
yuumi_image_path = r'img\yuumi.png'

click_on_image(play_image_path)
click_on_image(coop_image_path)
click_on_image(confirmar_image_path)
click_on_image(encontrar_image_path)
click_on_image(aceitar_image_path)

wait_for_image(pesquisar_image_path)

pyautogui.write("yuumi")
click_on_image(yuumi_image_path)
click_on_image(confirmar2_image_path)
