# ==========================================
#    DESAFIO DO CRIADOR DE PERSONAGENS
# ==========================================

# --- NÍVEL 1: Registro na Guilda ---
print("Bem-vindo à Guilda dos Aventureiros!")
nome = input("Qual o nome do herói? ")
classe = input("Qual a sua classe? ")

print("Bem-vindo, " + nome + "! Você foi registrado como um bravo " + classe + "!")
print()

# --- NÍVEL 2: Cálculo de Atributos ---
nivel = int(input("Qual o nível do seu personagem? "))

hp = nivel * 50
mana = nivel * 30

print("Calculando atributos base...")
print()

# --- NÍVEL 3: A Loja de Poções ---
ouro = 100.50
preco_pocao = 12.30

print("Você tem", ouro, "moedas de ouro.")
qtd_pocoes = int(input("Quantas poções de cura (12.30 cada) você quer comprar? "))

# Matemática básica
gasto_total = qtd_pocoes * preco_pocao
ouro = ouro - gasto_total

print()

# --- NÍVEL 4: A Ficha Estilizada ---
borda = "=" * 40
linha = "-" * 40

print(borda)
print("          FICHA DE PERSONAGEM          ")
print(borda)

print("NOME:" , nome , "   |   CLASSE:" , classe)
print("NÍVEL:" , nivel) 

print(linha)
print("ATRIBUTOS COMBATE:")
print("HP Máximo:" , hp , "  |   Mana:" , mana)

print(linha)
print("INVENTÁRIO:")
print("Poções de Cura:" , qtd_pocoes)
print("Ouro Restante:" , ouro , "moedas")

if nivel <= 10:
    print("Você ainda é muito fraco, Vc precisa carregar muitas poções!")
elif nivel >= 11 and nivel <=49:
    print("Você ainda é fraco, carregue algumas poções")
else:
    print("Você é muito forte, n precisa de poções")

print(borda)