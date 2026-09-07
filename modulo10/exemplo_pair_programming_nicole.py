import requests

def obter_cotacoes():
    """
    Busca as cotações do Dólar e Euro em relação ao Real
    utilizando a AwesomeAPI com tratamento de exceções.
    """
    url_api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    
    try:
        # Requisição GET com limite de tempo de 5 segundos
        resposta = requests.get(url_api, timeout=5)
        
        # Lança uma exceção se a resposta HTTP retornar código de erro (4xx ou 5xx)
        resposta.raise_for_status()
        
        # Converte a resposta recebida para dicionário Python
        dados = resposta.json()
        
        # Exibição dos dados obtidos
        print("========================================")
        print("       COTAÇÕES ATUAIS DAS MOEDAS       ")
        print("========================================")
        
        # Iteração pelas moedas retornadas na URL (USD-BRL e EUR-BRL)
        for chave, info in dados.items():
            nome = info["name"]
            cotacao = float(info["bid"])
            print(f"Moeda: {nome}")
            print(f"Valor de Compra: R$ {cotacao:.2f}")
            print("----------------------------------------")

    except requests.exceptions.Timeout:
        print("Erro: A requisição demorou muito para responder (Timeout).")
    except requests.exceptions.HTTPError as erro_http:
        print(f"Erro HTTP ocorrido: {erro_http}")
    except requests.exceptions.RequestException as erro_conexao:
        print(f"Erro de conexão: {erro_conexao}")
    except KeyError:
        print("Erro: Estrutura de dados retornada pela API é diferente do esperado.")

# Execução da função principal
if __name__ == "__main__":
    obter_cotacoes()