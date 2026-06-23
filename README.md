# dio-assistente-de-voz
Adaptação do "Assistente de Voz Multi-Idiomas Com Whisper e ChatGPT" da DIO para versão OpenSource e aplicado a conversação em língua estrangeira, como o Inglês.
# 🎙️ Assistente de Voz Inteligente para Prática de Idiomas

[cite_start]Este projeto é um assistente de voz interativo desenvolvido em Python, focado no aprendizado e na prática de conversação de idiomas estrangeiros[cite: 13, 14, 75]. [cite_start]Ele captura sua fala pelo microfone, transcreve o áudio, processa uma resposta inteligente (agindo como um professor nativo paciente) e dita a resposta de volta para você[cite: 15, 27].

[cite_start]O sistema combina três pilares principais[cite: 24, 75]:
1. [cite_start]**Speech-to-Text (Voz para Texto):** Reconhecimento de fala robusto com suporte a sotaques[cite: 13, 75, 77].
2. [cite_start]**Processamento de Linguagem Natural (IA):** Geração de respostas e correções gramaticais personalizadas[cite: 15].
3. [cite_start]**Text-to-Speech (Texto para Voz):** Sintetização da resposta da IA em áudio[cite: 15, 75].

---

## 🛠️ Modos de Execução

[cite_start]Você pode rodar este projeto de duas maneiras: utilizando APIs em nuvem (OpenAI) ou de forma 100% local e gratuita (Open-Source)[cite: 60, 62].

### Opção A: Utilizando APIs (Nuvem)
[cite_start]Configuração padrão utilizando os serviços da OpenAI e Google[cite: 2, 80].
* [cite_start]**Transcrição:** API do Whisper (OpenAI) [cite: 2]
* [cite_start]**Cérebro:** API do ChatGPT (GPT-4o-Mini) [cite: 46]
* [cite_start]**Voz:** Google Text-to-Speech (gTTS) [cite: 2, 80]

> [cite_start]⚠️ *Nota: Requer uma chave de API da OpenAI com saldo ativo[cite: 48, 50].*

### Opção B: 100% Local e Gratuita (Open-Source)
[cite_start]Caso queira rodar o projeto sem custos e de forma totalmente privada e offline[cite: 64, 69]:
* [cite_start]**Transcrição:** `faster-whisper` (Rodando localmente na CPU/GPU) [cite: 67]
* [cite_start]**Cérebro:** `Ollama` (Modelos Llama3 ou Qwen2.5 instalados na sua máquina) [cite: 61, 63]
* [cite_start]**Voz:** `pyttsx3` ou `MeloTTS` (Sintetização offline rápida) [cite: 69]

---

## 🚀 Como Instalar e Rodar

### Prerequisites

* Python 3.8 ou superior instalado.
* [cite_start]Requisito de Hardware (Caso use o modo Local): Mínimo de 8GB a 16GB de RAM[cite: 73].

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
cd NOME-DO-REPOSITORIO
