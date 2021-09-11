import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig

def synthesize_to_speaker():
    speech_config = speechsdk.SpeechConfig(subscription="<paste-your-resource-key>", region="<paste-your-region>")
    speech_config.speech_synthesis_voice_name = "zh-CN-XiaoxiaoNeural"
    audio_config = AudioOutputConfig(use_default_speaker=True, filename="./audio.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    file = open("./text.txt", encoding="UTF-8")
    synthesizer.speak_text_async(file.read())

synthesize_to_speaker()
