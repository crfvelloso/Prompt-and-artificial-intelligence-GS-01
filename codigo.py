!sudo apt-get update -y
!sudo apt-get install -y zstd
!curl -fsSL https://ollama.com/install.sh | sh
!pip install ollama -q

import subprocess
import time
import random
import ollama

subprocess.Popen(["ollama", "serve"])
time.sleep(3)

subprocess.run(["ollama", "pull", "llama3.2:1b"])

def gerar_dados_simulados():
    temperatura = random.randint(20, 110)
    energia = random.randint(5, 100)
    status_comunicacao = random.choice(["Estável", "Instável", "Sem Sinal"])
    return temperatura, energia, status_comunicacao

def avaliar_regras_locais(temperatura, energia, comunicacao):
    alertas = []
    if temperatura > 80:
        alertas.append("ALERTA CRÍTICO: Temperatura acima do limite seguro (>80°C).")
    if energia < 20:
        alertas.append("ALERTA: Nível de bateria crítico. Modo de economia ativado.")
    if comunicacao != "Estável":
        alertas.append("AVISO: Sistema de comunicação com anomalias.")
    return alertas

def analisar_com_ia(temperatura, energia, comunicacao, alertas):
    prompt_usuario = f"Temperatura: {temperatura}°C | Energia: {energia}% | Comunicação: {comunicacao} | Alertas locais: {', '.join(alertas) if alertas else 'Nenhum'}."
    
    resposta = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "system",
                "content": "Você é o sistema de controle de uma missão espacial. Analise os dados, confirme os alertas gerados e indique a próxima ação corretiva recomendada."
            },
            {
                "role": "user",
                "content": prompt_usuario
            }
        ]
    )
    return resposta["message"]["content"]

def executar_painel_missao():
    temp, energia, com = gerar_dados_simulados()
    alertas = avaliar_regras_locais(temp, energia, com)
    analise = analisar_com_ia(temp, energia, com, alertas)

    print("=" * 55)
    print("- MISSION CONTROL - STATUS ATUAL -")
    print("=" * 55)
    print(f"Temperatura : {temp}°C")
    print(f"Energia     : {energia}%")
    print(f"Comunicação : {com}")
    print("-" * 55)
    
    print("- ALERTAS E LÓGICA DE DECISÃO -")
    if alertas:
        for alerta in alertas:
            print(f" - {alerta}")
    else:
        print(" - Todos os parâmetros dentro da normalidade.")
        
    print("-" * 55)
    print("- ANÁLISE DA INTELIGÊNCIA ARTIFICIAL:")
    print(analise)
    print("=" * 55)

executar_painel_missao()
