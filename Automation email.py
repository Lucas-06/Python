import pandas as pd
import datetime 
import yfinance as yf
from matplotlib import pyplot as plt
import mplcyberpunk
import smtplib
import os
from email.message import EmailMessage

ativos = ["^BVSP", "BRL=X"]

hoje = datetime.datetime.now()

um_ano_atras = hoje - datetime.timedelta(days= 365)

dados_mercado = yf.download(ativos, um_ano_atras, hoje)

dados_fechamento = dados_mercado['Adj Close']
dados_fechamento.columns = ['Dolar', 'Ibovespa']

dados_fechamento = dados_fechamento.dropna()

dados_media_semanal = dados_fechamento.resample("W").mean()

### continuar posteriormente

##print(dados_fechamento)

dados_fechamento_mensal = dados_fechamento.resample("M").last()

##print(dados_fechamento_mensal)

###Passo 3

dados_fechamento_anual = dados_fechamento.resample("Y").last()

##print(dados_fechamento_anual)

###Passo 4

retorno_no_ano = dados_fechamento_anual.pct_change().dropna()
retorno_no_mes = dados_fechamento_mensal.pct_change().dropna()
retorno_no_dia = dados_fechamento.pct_change().dropna() 

####Passo 5

retorno_dia_dolar = retorno_no_dia.iloc[-1, 0]
retorno_dia_ibovespa = retorno_no_dia.iloc[-1, 1]

retorno_mes_dolar = retorno_no_mes.iloc[-1, 0]
retorno_mes_ibovespa = retorno_no_mes.iloc[-1, 1]

retorno_ano_dolar = retorno_no_ano.iloc[-1, 0]
retorno_ano_ibovespa = retorno_no_ano.iloc[-1, 1]

####Fazer função aqui####

retorno_dia_dolar = round (retorno_dia_dolar * 100, 2)
retorno_dia_ibovespa = round(retorno_dia_ibovespa * 100, 2)

retorno_mes_dolar = round (retorno_mes_dolar * 100, 2)
retorno_mes_ibovespa = round (retorno_mes_ibovespa * 100, 2)

retorno_ano_dolar = round (retorno_ano_dolar * 100, 2)
retorno_ano_ibovespa = round (retorno_ano_ibovespa * 100, 2)

##print(retorno_ano_dolar)

##print(retorno_ano_ibovespa)

###Passo 6 Ibovespa

plt.style.use("cyberpunk")

dados_fechamento.plot(y = 'Ibovespa', use_index = True, legend = False)

plt.title("Ibovespa")

plt.show()

##grafico dolar

plt.style.use("cyberpunk")

dados_fechamento.plot(y = 'Dolar', use_index = True, legend = False)

plt.title("Dolar")

plt.show()

##Grafico semanal



###

from dotenv import load_dotenv

senha = os.environ.get("senha")
email = 'araujolucas908@gmail.com'

msg = EmailMessage()
msg['Subject'] = "Enviando email com o Python"
msg['From'] = 'araujolucas908@gmail.com'
msg['to'] = 'lucas.praujo@gmail.com'

msg.set_content(f'''Prezado, segue o relatorio diário:
                
Bolsa:

No ano o Ibovespa está tendo uma rentabilidade de {retorno_ano_ibovespa}%,
enquanto no mês a rentabilidade é de {retorno_mes_ibovespa}%

No último dia útil, o fechamento do Ibovespa foi de {retorno_dia_ibovespa}%. 

Dólar:

No ano o Dólar está tendo uma rentabilidade de {retorno_ano_dolar}%,
enquanto no mês a rentabilidade é de {retorno_mes_dolar}%.

Abs,

ANAL. de Dados do Valdo de Neves..
''')

###Enviar email com arquivos de imagem 
'''''
with open('Figure_1.png', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='application', subtype='png', filename='Figure_1.png')


with open('Figure_2.png', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='application', subtype='png', filename='Figure_2.png')    
'''''
###Enviando o email

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email, senha)
    smtp.send_message(msg)    

