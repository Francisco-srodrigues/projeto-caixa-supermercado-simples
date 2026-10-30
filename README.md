# 🛒 Caixa de Supermercado - Valérios TechLabs

Um sistema de terminal modular, robusto e intuitivo que simula o funcionamento do caixa de um supermercado. Desenvolvido em Python como parte da consolidação de estudos avançados sobre estruturas de repetição, acumuladores e tratamento de exceções.

## 🚀 Funcionalidades

*   **Interface Limpa e Inteligente:** Atualização dinâmica da tela a cada produto inserido para evitar a poluição visual do terminal.
*   **Design Profissional:** Cabeçalhos centralizados, linhas modulares de separação e formatação automática para moeda padrão (`R$ 0.00`).
*   **Blindagem contra Erros (Resiliência):** Tratamento completo de entradas inválidas via `try/except`. O sistema impede travamentos caso o usuário digite letras ou utilize vírgula ( `,` ) em vez de ponto ( `.` ) para os centavos.
*   **Multiplataforma:** Identificação automática do Sistema Operacional para garantir a limpeza de tela tanto no Windows quanto no Linux/macOS.

## 🛠️ Tecnologias e Conceitos Aplicados

*   **Linguagem:** Python 3
*   **Loop Infinito Controlado:** Estrutura `while True` com saídas estratégicas via `break`.
*   **Fluxo Avançado de Repetição:** Uso do comando `continue` para reiniciar o ciclo imediatamente após a detecção de erros.
*   **Manipulação do Sistema Operacional:** Biblioteca integrada `os` para execução de comandos do sistema de baixo nível (`cls` / `clear`).
*   **Modularização:** Funções limpas e reutilizáveis (`limpar_tela()`, `linha()`).

## 📋 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe o arquivo do código fonte.
3. Abra o seu terminal ou prompt de comando na pasta do arquivo e execute:
   ```bash
   python caixa_supermercado.py
   ```
4. Digite os preços dos produtos. Para finalizar a compra e emitir o total, digite `0`.

---
**Desenvolvido com dedicação por Francisco Rodrigues 💻**
