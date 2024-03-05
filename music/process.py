import io
from pydub import AudioSegment
intro=AudioSegment.from_mp3("music/crime_outro.mp3")



intro=intro-8
intro.export("music/crime_outro.mp3",format="mp3")