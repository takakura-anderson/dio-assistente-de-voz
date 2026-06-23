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
```
### 2. Instalar as Dependências
Para o modo com APIs da OpenAI:

```Bash
pip install openai gTTS speechrecognition
Para o modo 100% Local (Ollama + Whisper Local):
```
```Bash
pip install ollama faster-whisper pyttsx3 speechrecognition
```
(Se optar pelo Ollama, certifique-se de baixar o app em ollama.com e rodar o modelo desejado no terminal antes de iniciar: ollama run llama3).

### 3. Configurar Variáveis de Ambiente (Se usar a OpenAI)
Crie um arquivo .env na raiz do projeto e adicione a sua chave privada:

Snippet de código
```OPENAI_API_KEY=sua_chave_secreta_aqui```

Nunca envie seu arquivo .env ou exponha sua chave diretamente no código ao subir alterações para o GitHub!

### 4. Executar o Assistente
```Bash
python main.py
```
🧠 Engenharia de Prompt Aplicada
O grande diferencial deste assistente está no comportamento da inteligência artificial. O modelo está configurado através de instruções internas (System Prompt) para:

Atuar como um professor nativo paciente.

Fornecer uma resposta natural à sua frase para manter o diálogo fluindo.

Apresentar um feedback estruturado no final, corrigindo brevemente eventuais deslizes gramaticais ou sugerindo vocabulários mais naturais.

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
