import cv2
import pyautogui
import numpy as np
import time

def clicar_no_centro_da_imagem(imagem_path, imagem_aceitar_path=None):
    while True:
        if imagem_aceitar_path:
            imagem_aceitar = cv2.imread(imagem_aceitar_path)
            imagem_aceitar = cv2.cvtColor(imagem_aceitar, cv2.COLOR_BGR2GRAY)

            # Verificar se a imagem "aceitar" está na tela
            tela_aceitar = pyautogui.screenshot()
            tela_bgr_aceitar = cv2.cvtColor(np.array(tela_aceitar), cv2.COLOR_RGB2BGR)
            tela_gray_aceitar = cv2.cvtColor(tela_bgr_aceitar, cv2.COLOR_BGR2GRAY)
            resultado_aceitar = cv2.matchTemplate(tela_gray_aceitar, imagem_aceitar, cv2.TM_CCOEFF_NORMED)
            _, _, _, max_loc_aceitar = cv2.minMaxLoc(resultado_aceitar)
            x_aceitar, y_aceitar = max_loc_aceitar
            altura_aceitar, largura_aceitar = imagem_aceitar.shape
            centro_x_aceitar = x_aceitar + largura_aceitar // 2
            centro_y_aceitar = y_aceitar + altura_aceitar // 2

            # Se a imagem "aceitar" estiver na tela, clique nela e retorne
            if resultado_aceitar[y_aceitar, x_aceitar] > 0.8:
                pyautogui.click(centro_x_aceitar, centro_y_aceitar)
            else:
                # Se a imagem "aceitar" não for encontrada, aguarde um curto período
                time.sleep(1)
                continue

        # Se a imagem "aceitar" não estiver na tela ou não for fornecida, prossiga com a imagem principal
        imagem = cv2.imread(imagem_path)
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # Verificar se a imagem principal está na tela
        tela = pyautogui.screenshot()
        tela_bgr = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2BGR)
        tela_gray = cv2.cvtColor(tela_bgr, cv2.COLOR_BGR2GRAY)
        resultado = cv2.matchTemplate(tela_gray, imagem, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(resultado)
        x, y = max_loc
        altura, largura = imagem.shape
        centro_x = x + largura // 2
        centro_y = y + altura // 2

        # Se a imagem principal estiver na tela, clique nela e retorne
        if resultado[y, x] > 0.8:
            pyautogui.click(centro_x, centro_y)
            return
        else:
            # Se a imagem principal não for encontrada, aguarde um curto período
            time.sleep(1)

if __name__ == "__main__":
    # Lista de imagens a procurar com suas imagens "aceitar" associadas
    imagens_a_procurar = [
        {"imagem_path": r'img\aceitar.png', "imagem_aceitar_path": None},
        {"imagem_path": r'img\honra.png', "imagem_aceitar_path": r'img\aceitar.png'},
        {"imagem_path": r'img\continuar3.png', "imagem_aceitar_path": r'img\aceitar.png'},
        {"imagem_path": r'img\jogar.png', "imagem_aceitar_path": r'img\aceitar.png'},
        {"imagem_path": r'img\encontrar.png', "imagem_aceitar_path": r'img\aceitar.png'},
        {"imagem_path": r'img\pesquisar.png', "imagem_aceitar_path": r'img\aceitar.png'},
        {"imagem_path": r'img\escrever.png', "imagem_aceitar_path": r'img\aceitar.png'},
        {"imagem_path": r'img\yuumi.png', "imagem_aceitar_path": r'img\aceitar.png'},
        {"imagem_path": r'img\confirmar.png', "imagem_aceitar_path": r'img\aceitar.png'}
    ]

    # Executar a sequência de ações
    for imagem_info in imagens_a_procurar:
        clicar_no_centro_da_imagem(imagem_info["imagem_path"], imagem_info["imagem_aceitar_path"])
