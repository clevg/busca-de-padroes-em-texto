# 🔍 Busca de Padrões em Texto com Comparação de Algoritmos

Este projeto em Python implementa e compara três algoritmos clássicos de busca de padrões em textos:

- **Shift-And (Bitap)** — busca eficiente com operações bit a bit.
- **Força Bruta** — simples, porém com baixa eficiência para textos longos.
- **Índice Invertido** — útil para localizar palavras inteiras rapidamente.

Permite a leitura de **arquivos reais de texto (.txt)** e mede o tempo de execução de cada algoritmo.

---

## 🚀 Como Executar

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/busca-de-padroes-em-texto.git
cd busca-de-padroes-em-texto
```

### 2. Adicione um arquivo `.txt` ao diretório do projeto.

### 3. Execute o programa:

```bash
python busca_texto.py
```

### 4. Informe:
- O **caminho** do arquivo de texto.
- O **padrão** que deseja buscar.

---

## 🧠 Algoritmos Implementados

### 🔹 Shift-And (Bitap)
Algoritmo baseado em operações bit a bit. Muito rápido para padrões curtos. Ideal quando a busca é frequente.

### 🔹 Força Bruta
Compara caractere por caractere. Simples e fácil de entender, mas ineficiente para grandes volumes.

### 🔹 Índice Invertido
Cria uma estrutura que associa cada palavra às suas posições no texto. Ótimo para buscas por palavras inteiras.

---

## 🧪 Exemplo de Uso

```bash
Digite o caminho do arquivo de texto (.txt): exemplo.txt
Digite o padrão a ser buscado: amor

🔍 Shift-And encontrou 12 ocorrências em 0.002134 segundos.
🔍 Força Bruta encontrou 12 ocorrências em 0.003981 segundos.
📚 Índice invertido encontrou 12 ocorrências em 0.000521 segundos.
```

---


## 🛠️ Requisitos

- Python 3.6 ou superior

> Nenhuma biblioteca externa é necessária. O código utiliza apenas bibliotecas nativas.

---

## 💡 Possíveis Extensões

- Suporte à busca por múltiplos padrões
- Comparação com algoritmos como Boyer-Moore ou KMP
- Gráficos de desempenho (usando `matplotlib`)
- Interface gráfica (Tkinter, PyQt)
- Web app com Flask ou Streamlit
