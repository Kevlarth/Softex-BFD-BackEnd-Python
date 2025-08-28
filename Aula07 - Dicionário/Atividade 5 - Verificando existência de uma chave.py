# Verifique se a chave "telefone" existe no dicionário:
contato: dict = {"nome": "Ana", "email": "ana@email.com"}

verificar: str = "telefone"
chave_encontrada = False

for item in contato:
    if item == verificar:
        chave_encontrada = True
        break 
if chave_encontrada:
    print(f"A chave '{verificar}' existe no dicionário.")

if not chave_encontrada:
    print(f"A chave '{verificar}' não existe no dicionário.")