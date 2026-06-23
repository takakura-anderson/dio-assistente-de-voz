import ollama
from faster_whisper import WhisperModel
import speech_recognition as sr
import pyttsx3  # Para voz offline rápida, ou mantenha o gTTS se tiver internet

# 1. Inicializa o Whisper Local (usando o modelo 'base' ou 'tiny' para ser rápido)
# Se tiver placa de vídeo NVIDIA, mude device="cpu" para device="cuda"
modelo_transcricao = WhisperModel("base", device="cpu", compute_type="int8")

# 2. Inicializa o sintetizador de voz local
engine_voz = pyttsx3.init()

def ouvir_usuario():
    # Código padrão para gravar o áudio do microfone e salvar em um arquivo temporario 'audio.wav'
    print("Ouvindo...")
    # (Imagine aqui o bloco de código que captura o áudio do microfone)
    
    # Transcreve localmente com Whisper
    segments, _ = modelo_transcricao.transcribe("audio.wav", language="en")
    texto = "".join([segment.text for segment in segments])
    return texto

def conversar_com_ollama(texto_usuario):
    # Envia o texto para o modelo rodando no seu Ollama local
    response = ollama.chat(
        model="llama3",  # Certifique-se de ter dado 'ollama run llama3' no terminal antes
        messages=[
            {
                "role": "system",
                "content": "You are a patient English teacher. Reply naturally and briefly correct any grammar mistakes."
            },
            {
                "role": "user",
                "content": texto_usuario
            }
        ]
    )
    return response['message']['content']

def falar(texto_resposta):
    # Dita a resposta localmente
    engine_voz.say(texto_resposta)
    engine_voz.runAndWait()

# Fluxo Principal
# texto = ouvir_usuario()
# resposta = conversar_com_ollama(texto)
# falar(resposta)