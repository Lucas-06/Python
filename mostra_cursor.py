import pyautogui

# Aguarde o usuário clicar em alguma coisa
input("Clique em algo em outra tela e pressione Enter...")

# Obtenha as coordenadas do cursor do mouse
x, y = pyautogui.position()

# Exiba as coordenadas
print(f"Coordenadas do cursor: X = {x}, Y = {y}")
