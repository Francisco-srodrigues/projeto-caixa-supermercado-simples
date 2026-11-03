# Autor: Francisco Rodrigues
# Data: 28/10/2026
# Objetivo: Consolidação do estudo de estrutura de repetição com contador e acumulador

Enunciado = """Escreva um programa que funcione como o caixa de um supermercado.
O programa deve pedir para o usuário digitar o preço de um produto.
O programa continuará pedindo o preço do próximo produto até que o usuário digite o valor 0 (zero), que indica que a compra acabou.
No final, o programa deve mostrar o Valor Total da Compra. No final de tudo, mostre a palavra "Pronto!"."""

# Início do programa
import os

# Função para limpar tela
def limpar_tela():
  if os.name == 'nt':
    os.system('cls')  # Windows
  else:
    os.system('clear')  # Linux/macOS


def linha():
    print('='*45)
    
# Declaração de váriáveis    
total = 0.0
quantidade = 0
maior_preco = 0.0

# Loop 
while True:
    print('\t=========================')
    print('\t[ Caixa de Supermercado ]')
    print('\t=========================')
    print('     Desenvolvido por: Valérios TechLabs')
    linha()
    
    # 🛡️ Início da zona de proteção contra erros
    try:
        preco = float(input('Digite o preço do produto (ou 0 para sair): '))
    except ValueError:
        linha()
        print('❌ Erro: Entrada inválida! Digite apenas números.')
        print('👉 Use PONTO (.) para centavos (Ex: 4.50 em vez de 4,50).')
        linha()
        input('Pressione [ENTER] para tentar novamente...')
        limpar_tela()
        continue  # Força o loop a voltar para o começo sem somar nada
    
    if preco == 0:
        break
    # ZONA SEGURA (Só chega aqui quem digitou um preço válido > 0)
    total += preco
    quantidade += 1  # Conta o produto válido!
    
    # Lógica inteligente para descobrir o produto mais caro
    if preco > maior_preco:
        maior_preco = preco
        
    limpar_tela()

# 🧮 Cálculos Finais (Fora do loop)
# Proteção essencial contra o erro de divisão por zero (ZeroDivisionError)
if quantidade > 0:
    media = total / quantidade
else:
    media = 0.0
    
# 📋 Exibição do Relatório Gerencial Estatístico
limpar_tela()
linha()
print('\t📊  RELATÓRIO DA COMPRA - VALÉRIOS TECHLABS')
linha()
print(f'🛒  Total de itens comprados : {quantidade}')
print(f'💵  Valor total da compra     : R$ {total:.2f}')
print(f'📈  Média de preço dos itens : R$ {media:.2f}')
print(f'💎  Produto mais caro        : R$ {maior_preco:.2f}')
linha()
print('Obrigado por utilizar o nosso sistema! Volte sempre.')
linha()
