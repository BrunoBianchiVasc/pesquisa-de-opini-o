# 📋 Pesquisa de Opinião - TudoWeb

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)

Programa em Python que simula uma pesquisa de satisfação no atendimento ao cliente da empresa TudoWeb.

## 🎯 Objetivo

Coletar, por meio de estrutura de repetição, a opinião de clientes sobre o atendimento prestado e exibir ao final quantas respostas foram "EXCELENTE" e quantas foram "RUIM".

## ⚙️ O que o programa faz

- Coleta nome, idade e opinião sobre o atendimento de cada entrevistado
- Opções de resposta:
  - `1` - EXCELENTE
  - `2` - BOM
  - `3` - RUIM
- Repete a coleta para todos os entrevistados (loop `for`)
- Usa `match/case` para verificar a opinião digitada e contar as respostas
- Ao final, exibe:
  - Quantidade de respostas EXCELENTE
  - Quantidade de respostas RUIM

## ▶️ Como rodar

```bash
python pesquisa_opiniao.py
```

O programa vai pedir os dados de cada entrevistado, um por vez.

## 🔢 Sobre a quantidade de entrevistados

No código, a variável `NUM_ENTREVISTADOS` controla quantas pessoas serão entrevistadas e já está ajustada para a versão final da atividade:

```python
NUM_ENTREVISTADOS = 50
```

Para testar o programa mais rápido, basta reduzir esse valor (ex: `10`) durante os testes.

## 📌 Requisitos

- Python 3.10 ou superior (necessário para o `match/case`)
