<div align="center">

  <h1>🐍 Atividades Pessoais — Python</h1>

  <p>
    <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge" alt="Status"/>
    <img src="https://img.shields.io/badge/Projetos-3-brightgreen?style=for-the-badge" alt="Projetos"/>
  </p>

  <p>Repositório com projetos pessoais desenvolvidos em Python para estudo e prática. Cada arquivo representa uma ideia diferente — de jogos a ferramentas de análise.</p>

</div>

---

## 📁 Projetos

---

### 🃏 1. Análise de Jogos de Poker — `analise_jogos_poker.py`

> **Assistente inteligente para Texas Hold'em no terminal**

Um advisor completo de poker rodando no terminal. Você informa as suas cartas na mão e a fase atual do jogo (Pre-Flop, Flop, Turn ou River), e o programa analisa a força da sua mão e te diz a melhor jogada: **Raise**, **Call**, **Check**, **Bet** ou **Fold**.

**Como funciona:**
- No **Pre-Flop**, avalia os dois cards da mão usando um sistema de score próprio (considera pares, suited, conectores, altura das cartas) e estima a equidade percentual.
- No **Flop**, **Turn** e **River**, recebe as cartas comunitárias e usa a biblioteca `texasholdem` para calcular o rank real da mão (de 1 a 7462), convertendo isso em um percentual de força.
- Para cada fase, exibe a recomendação de jogada com uma explicação estratégica.

**Tecnologias:** `texasholdem`, `os`

**Como usar:**

````
Ranks: 2 3 4 5 6 7 8 9 T J Q K A
Naipes: h=♥ d=♦ c=♣ s=♠
Exemplo: As Kh (Ás de espadas + Rei de copas)
````

<div align="center">
  <img src="ignore/image.png" alt="Advisor de Poker" width="300"/>

</div>

---

### 💱 2. Conversor de Moedas — `conversor_de_moedas.py`

> **Conversor de câmbio em tempo real via API**

Um conversor de moedas que busca a cotação atual diretamente da internet e realiza a conversão na hora. Suporta quatro moedas e usa a [AwesomeAPI](https://economia.awesomeapi.com.br/) para obter as taxas de câmbio em tempo real.

**Moedas suportadas:**
| Símbolo | Moeda   |
|---------|---------|
| R$      | Real    |
| $       | Dólar   |
| €       | Euro    |
| £       | Libra   |

**Como funciona:**
1. O usuário escolhe a moeda de origem e a de destino.
2. O programa monta o par (ex: `BRL-USD`) e faz uma requisição GET à API.
3. O valor atual da cotação (`bid`) é retornado e multiplicado pelo valor inserido.
4. O resultado final é exibido formatado com 2 casas decimais.

**Tecnologias:** `requests`, `os`, `sys`

**Exemplo de saída:**
````
A conversão do(a) Real para o(a) Dólar é: $5.73
Multiplicado por R$100, é igual á: $ 573.00
````

<div align="center">
  <img src="ignore/image-1.png" alt="Conversor de Moedas" width="300"/>
</div>

---

### 🎲 3. Jogo de Adivinhação — `jogo_de_advinhação.py`

> **Clássico jogo de adivinhar o número com dificuldades configuráveis**

Um jogo de terminal onde o computador sorteia um número aleatório e o jogador deve adivinhar qual é, recebendo dicas se o número é maior ou menor a cada tentativa. Conta as tentativas e mostra no final quantos chutes foram necessários.

**Modos de dificuldade:**
| #  | Dificuldade  | Intervalo       |
|----|--------------|-----------------|
| 1  | Fácil        | 1 a 10          |
| 2  | Médio        | 1 a 100         |
| 3  | Difícil      | 1 a 1.000       |
| 4  | Personalizado| Você define o teto |
| 5  | Sair         | —               |

**Como funciona:**
- O número é gerado com `random.randint()`.
- A cada tentativa errada, o jogo informa se o número secreto é **maior** ou **menor**.
- Ao acertar, exibe a quantidade de tentativas usadas.

**Tecnologias:** `random`, `os`, `sys`


<div align="center">
  <img src="ignore/image-2.png" alt="Demo do Jogo de Adivinhação" width="300"/>
  <p><i>🖼️ Substitua pela imagem real do programa rodando</i></p>
</div>

---

## 🚀 Como executar os projetos

**Pré-requisitos:** Python 3.14 instalado.

```bash
# Clone o repositório
git clone https://github.com/Eduardo-Nicolete37/Atividades_Pessoais_Python.git
cd Atividades_Pessoais_Python

# Para o conversor de moedas (precisa da lib requests):
pip install requests

# Para a análise de poker (precisa da lib texasholdem):
pip install texasholdem

# Rode qualquer arquivo:
python analise_jogos_poker.py
python conversor_de_moedas.py
python jogo_de_advinhação.py
```

---

## 🛠️ Tecnologias utilizadas

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/requests-Library-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/texasholdem-Library-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/random-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/AwesomeAPI-Exchange%20Rates-green?style=flat-square"/>
</p>

---

## 👤 Autor

**Eduardo Nicolete**

[![GitHub](https://img.shields.io/badge/GitHub-Eduardo--Nicolete37-181717?style=flat-square&logo=github)](https://github.com/Eduardo-Nicolete37)

---

<div align="center">
  <sub>Feito com 🐍 e dedicação para aprender Python na prática.</sub>
</div>