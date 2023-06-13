import subprocess
from datetime import datetime, time
import pytz
import smtplib
from email.message import EmailMessage

# Define o fuso horário de Brasília
brasilia_tz = pytz.timezone('America/Sao_Paulo')

# Define o horário de início e término do monitoramento
start_time = time(8, 30)
end_time = time(16, 35)

# Define o IP para pingar
ip_address = '8.8.8.8'

# Variáveis para contar os resultados
successful_pings = 0
failed_pings = 0

# Loop para executar o ping
while True:
    current_time = datetime.now(brasilia_tz).time()
    
    # Verifica se está dentro do intervalo de tempo desejado
    if current_time >= start_time and current_time <= end_time:
        try:
            # Executa o ping
            subprocess.check_output(f"ping -c 1 {ip_address}", shell=True)
            successful_pings += 1
        except subprocess.CalledProcessError:
            failed_pings += 1
    
    # Verifica se o horário atual é após o horário de término
    if current_time > end_time:
        break

# Exibe os resultados
print(f"Testes bem-sucedidos: {successful_pings}")
print(f"Testes mal-sucedidos: {failed_pings}")

# Importar senha
import os
from dotenv import load_dotenv

load_dotenv()

senha = os.environ.get("senha_email")
email = 'seuemail@gmail.com'

msg = EmailMessage()
msg['Subject'] = "Enviando email com o Python"
msg['From'] = 'seuemail@gmail.com'
msg['to'] = 'seuemail@gmail.com'

# Cria o corpo do e-mail
msg.set_content(f'''Testes bem-sucedidos: {successful_pings}\nTestes mal-sucedidos: {failed_pings}''')

# Envia o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email, senha)
    smtp.send_message(msg)

print("E-mail enviado com sucesso!")