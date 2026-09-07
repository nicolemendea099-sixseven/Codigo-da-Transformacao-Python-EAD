import requests

def consultar_clima():
    # 1. Entrada de dados com validação básica
    cidade = input("Digite o nome da cidade: ").strip()
    if not cidade:
        print("❌ Erro: O nome da cidade não pode estar em branco.")
        return

    # 2. Configurações da API
    chave_api = "2d6690b51aa4015324c330bb1bfa1a7f" 
    
    # --- PASSO A: Buscar Estado e Coordenadas (Geocoding API) ---
    url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={cidade}&limit=1&appid={chave_api}"
    
    estado = ""
    pais = ""
    
    try:
        # timeout=5 evita que a chamada fique travada em conexões lentas
        resposta_geo = requests.get(url_geo, timeout=5)
        if resposta_geo.status_code == 200 and resposta_geo.json():
            dados_geo = resposta_geo.json()[0]
            estado = dados_geo.get("state", "")
            pais = dados_geo.get("country", "")
    except requests.exceptions.RequestException:
        # Se o Geocoding falhar por rede, o programa apenas ignora e tenta buscar o clima direto
        pass

    # --- PASSO B: Buscar Clima Atual ---
    url_api = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"

    print("\nBuscando dados no OpenWeatherMap...")
    
    try:
        # 3. Requisição HTTP GET com timeout
        resposta = requests.get(url_api, timeout=5)
        
        # Dispara exceção para status HTTP 4xx ou 5xx
        resposta.raise_for_status()

        # 4. Processamento dos dados JSON
        dados_clima = resposta.json()

        nome_cidade = dados_clima["name"]
        temperatura = dados_clima["main"]["temp"]
        sensacao_termica = dados_clima["main"]["feels_like"]
        descricao_clima = dados_clima["weather"][0]["description"]
        umidade = dados_clima["main"]["humidity"]

        # Formatação do local
        if estado:
            localizacao = f"{nome_cidade} - {estado}, {pais}"
        elif pais:
            localizacao = f"{nome_cidade}, {pais}"
        else:
            localizacao = nome_cidade

        # Exibição dos dados organizados (Atividade 2)
        print("\n" + "=" * 40)
        print(f"🌍 Clima atual em: {localizacao}")
        print("=" * 40)
        print(f"🌤️  Condição: {descricao_clima.capitalize()}")
        print(f"🌡️  Temperatura: {temperatura}°C")
        print(f"🔥 Sensação Térmica: {sensacao_termica}°C")
        print(f"💧 Umidade: {umidade}%")
        print("=" * 40)

    # --- PASSO C: Tratamento de Erros e Exceções (Atividade 3) ---
    except requests.exceptions.Timeout:
        print("\n⏳ Erro: A requisição excedeu o tempo limite. Verifique sua conexão com a internet.")
    except requests.exceptions.ConnectionError:
        print("\n🌐 Erro: Falha de conexão de rede. Não foi possível alcançar o servidor.")
    except requests.exceptions.HTTPError:
        if resposta.status_code == 401:
            print("\n❌ Erro 401: Chave de API não autorizada.")
        elif resposta.status_code == 404:
            print(f"\n❌ Erro 404: Cidade '{cidade}' não encontrada.")
        else:
            print(f"\n⚠️ Falha na requisição. Código HTTP: {resposta.status_code}")
    except KeyError:
        print("\n❌ Erro: A estrutura de resposta da API mudou ou faltam dados no JSON.")
    except Exception as erro:
        print(f"\n❌ Erro inesperado: {erro}")

# Execução do programa
if __name__ == "__main__":
    consultar_clima()