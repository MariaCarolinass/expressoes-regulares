import re

def validar_senha(senha):
    senhaValidadaLista = []
    senhaValidadaLista.append(verificarTamanho(senha))
    senhaValidadaLista.append(verificarLetraMaiuscula(senha))
    senhaValidadaLista.append(verificarLetraMinuscula(senha))
    senhaValidadaLista.append(verificarNumero(senha))
    return senhaValidadaLista

def verificarTamanho(senha):
    verificador = "NÃO"
    numero = re.search(r"[a-zA-Z\d]{8,}", senha)
    if numero:
        verificador = "OK"
    return verificador

def verificarLetraMaiuscula(senha):
    verificador = "NÃO"
    letraMaiucula = re.search(r"[A-Z]", senha)
    if letraMaiucula:
        verificador = "OK"
    return verificador

def verificarLetraMinuscula(senha):
    verificador = "NÃO"
    letraMinuscula = re.search(r"[a-z]", senha)
    if letraMinuscula:
        verificador = "OK"
    return verificador

def verificarNumero(senha):
    verificador = "NÃO"
    numero = re.search(r"\d+", senha)
    if numero:
        verificador = "OK"
    return verificador

senha = "Senha123456"
senhaValidadaLista = validar_senha(senha)

print(f"Comprimento mínimo de 8 caracteres: {senhaValidadaLista[0]}")
print(f"Pelo menos uma letra maiúscula: {senhaValidadaLista[1]}")
print(f"Pelo menos uma letra minúscula: {senhaValidadaLista[2]}")
print(f"Pelo menos um número: {senhaValidadaLista[3]}")

if "NÃO" in senhaValidadaLista:
    print("Senha fraca!")
else:
    print("Senha forte!")