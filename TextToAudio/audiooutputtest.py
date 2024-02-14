import elevenlabs
from elevenlabs import generate, play,voices
elevenlabs.set_api_key("490e04cfa04d838602598e1864132169")
import io
from pydub import AudioSegment

voice=voices()
audio=elevenlabs.generate(
    text="awesome",
    voice=voice[3]
)
song=AudioSegment.from_mp3("crime_outro_raw.mp3")
fifteen_seconds = 15 * 1000

outro = song[:fifteen_seconds]
ten_seconds = 10 * 1000
last_5_seconds = song[-5000:]
first_10_seconds = song[:ten_seconds]
end = last_5_seconds - 3
outro=outro-3
#elevenlabs.save(audio, "output/0.mp3")
outro.export("crime_outro.mp3",format="mp3")