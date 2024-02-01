import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui


#abrir o whatsapp Web
webbrowser.open('https://web.whatsapp.com/')
sleep(15)


workbook = openpyxl.load_workbook('listaNomes.xlsx')
pagina_clientes = workbook['Planilha1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    #mensagem personalizada
    mensagem= (f'Olá {nome} seu boleto irá vencer dia {vencimento.strftime('%d/%m/%Y')}. Qualquer dúvida favor entrar em contato com financeiro.')
   
   
    try:
        link_mensagem = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem)
        sleep(15)
        seta = pyautogui.locateCenterOnScreen('enviarpct.png')
        sleep(7)
        pyautogui.click(seta[0],seta[1])
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possível enviar a mensagem para {nome}.')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}')



