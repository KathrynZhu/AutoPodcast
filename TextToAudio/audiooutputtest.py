import elevenlabs
#elevenlabs.set_api_key("my-api-key")
voice = elevenlabs.Voice(
    voice_id = "ZQe5CZNOzWyzPSCn5a3c",
    settings = elevenlabs.VoiceSettings(
        stability = 1,
        similarity_boost = 0.75
    )
)
audio=elevenlabs.generate(
    text="Hi,this is a message",
    voice=voice
)
#elevenlabs.play(audio)
elevenlabs.save(audio, "outputaudio3.mp3")