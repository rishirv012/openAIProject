import openai

openai.api_key = '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'
audio_file = open("output.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript['text'])
