import pyautogui
import time

try:
    print("Certifique-se de que a janela do Roblox esteja ativa e em foco.")
    print("Pressione Ctrl + C para parar o script.")
    
    while True:
        pyautogui.press('e')  # Simula o pressionamento da tecla "E"
        time.sleep(1)         # Espera 1 segundo
except KeyboardInterrupt:
    print("\nScript finalizado pelo usuário.")
