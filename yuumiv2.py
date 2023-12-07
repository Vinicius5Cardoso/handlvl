import pyautogui
import keyboard
import time
import os

def move_mouse_to_center():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.moveTo(center_x, center_y)

def check_for_q1():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    q1_image_path = os.path.join(script_directory, r'img\q1.png')

    try:
        screenshot = pyautogui.screenshot()

        q1_image_location = pyautogui.locateOnScreen(q1_image_path, confidence=0.5,
                                                      region=(0, 0, screenshot.width, screenshot.height))

        return q1_image_location is not None
    except Exception as e:
        print(f"Erro ao verificar a imagem: {e}")
        return False

def press_and_release(keys):
    keyboard.press(keys)
    time.sleep(1)  # Ajuste o tempo de espera conforme necessário
    keyboard.release(keys)

def clicar_na_imagem():
    time.sleep(5)
    imagem_encontrada = False

    while not imagem_encontrada:
        try:
            imagem_pos = pyautogui.locateOnScreen('img/fim.png', confidence=0.8)

            if imagem_pos:
                x, y, _, _ = imagem_pos
                x_centro = x + _ / 2
                y_centro = y + _ / 2

                pyautogui.moveTo(x_centro + 15, y_centro)
                pyautogui.click()
                print("Imagem encontrada e clicada!")
                return True  # Indica que o botão foi clicado
            else:
                print("Imagem não encontrada. Aguardando...")
                time.sleep(1)  
        except pyautogui.ImageNotFoundException:
            print("Imagem não encontrada. Aguardando...")
            time.sleep(1) 

    return False  # Indica que o botão não foi clicado

# Inicializar variável para Anti AFK
w_last_time = time.time()
programa_encerrado = False

# up skill
keyboard.press_and_release("ctrl+q")
time.sleep(2)

while not programa_encerrado:
    if check_for_q1():
        # Ações se o Q1 estiver na tela
        press_and_release("F2")
        move_mouse_to_center()
        time.sleep(1)  # Aguarde o tempo necessário para mover o mouse
        press_and_release("w")
        time.sleep(1)  # Aguarde o tempo necessário para pressionar "W"
        press_and_release("F2")
        programa_encerrado = True  # Sai do loop principal se o botão da imagem foi clicado
    else:
        # Ações se o Q1 não estiver na tela
        press_and_release("e")

    # Anti AFK a cada 2 segundos
    if time.time() - w_last_time >= 2:
        press_and_release("w")
        w_last_time = time.time()
        press_and_release("F2")
        move_mouse_to_center()
        press_and_release("w")

# Restante do código aqui (fora do loop principal)
print("Programa continuando após clicar na imagem.")
