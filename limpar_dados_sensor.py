import re

def limpar_dados_sensor(dados):
    return re.sub(r"\s+", " ", re.sub(r"[^\w.:°%-]", " ", dados))

dados = "Temperatura: -5.6°C !!! Umidade: 70%    @@@ Pressão: 999.5hPa ###"
print(limpar_dados_sensor(dados))