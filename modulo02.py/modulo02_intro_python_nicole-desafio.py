import time
from datetime import datetime

# Cores para deixar o terminal estilizado (Códigos ANSI)
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
RESET = "\033[0m"

print(f"{AZUL}==========================================")
print("     🚀 SISTEMA INTERATIVO PYTHON 🚀      ")
print(f"=========================================={RESET}\n")

# Entrada do usuário
nome = input(f"{AMARELO}👉 Qual é o seu nome? {RESET}")

# Captura do horário atual
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
hora_numero = agora.hour

# Define a saudação dinamicamente
if 5 <= hora_numero < 12:
    saudacao = "Bom dia ☀️"
elif 12 <= hora_numero < 18:
    saudacao = "Boa tarde 🌤️"
else:
    saudacao = "Boa noite 🌙"

# Efeito visual de carregamento no terminal
print(f"\n{AZUL}Conectando ao sistema", end="", flush=True)
for _ in range(3):
    time.sleep(0.4)
    print(".", end="", flush=True)

# Exibição final estilizada
print(f"\n\n{VERDE}✨ {saudacao}, {nome}!{RESET}")
print(f"{VERDE}⏰ Horário atual: {hora_atual}{RESET}\n")