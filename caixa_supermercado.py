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
    
    
total = 0.0

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
    total += preco
    limpar_tela()
    
# Resultado
linha()
print(f'Total a pagar: R$ {total:.2f} reais')
print('Pronto!')
