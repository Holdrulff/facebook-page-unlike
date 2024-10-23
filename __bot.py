import pyautogui
import time
import os

pyautogui.PAUSE = 0.5
counter = 9503

def screenshot(counter):
    
    # Verifica se o diretório 'data' existe, senão cria
    if not os.path.exists(".\\data"):
        os.makedirs(".\\data")
    
    # Captura o screenshot
    screenshot = pyautogui.screenshot()
    
    # Define o caminho e nome do arquivo
    filename = f".\\data\\dummy{counter}.png"
    print(filename)
    
    # Salva o screenshot no arquivo
    screenshot.save(filename)
 

pyautogui.hotkey("alt", "tab")
pyautogui.press("f5")
time.sleep(3)



while True:
    pyautogui.moveTo(503, 1005, 1)#move para a página 
    pyautogui.click()
    time.sleep(5)#carregando a página
    try:
        img = pyautogui.locateOnScreen("botao_curtir.png", confidence=0.8) #localiza botão de curtir
        x, y = pyautogui.center(img) 
        pyautogui.moveTo(x, y) #move o cursor para o botão de cutir
        screenshot(counter)
        pyautogui.click()
        pyautogui.moveTo(1160, 815)#descurtir
        pyautogui.click()
        pyautogui.moveTo(1060, 885)#atualizar
        pyautogui.click()
        pyautogui.hotkey("ctrl", "w")#fecha aba
        pyautogui.press("f5")#atualiza página
        time.sleep(3)#espera
    except: 
        print("error: button not found")
        screenshot(counter)
        exit(1)
    counter = counter+1