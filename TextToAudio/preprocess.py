# this file should be preprocessing user input to make sure nothing wrong gets output to audio
# label non-conversational terms in the script
# label different speakers to cut the paragraph into different pieces to generate different
import re
from pydub import AudioSegment
from pydub.playback import play
import elevenlabs
from elevenlabs import voices
import numpy as np
import io
elevenlabs.set_api_key("490e04cfa04d838602598e1864132169")
voice=voices()
def segment_paragraphs(text):
    # Split the text into paragraphs
    paragraphs = text.split("\n\n")
    return paragraphs
#def label_paragraphs(paragraphs):
    labeled_paragraphs = []
    for idx, paragraph in enumerate(paragraphs):
        labeled_paragraphs.append(f"Paragraph {idx + 1}: {paragraph}")
    return labeled_paragraphs


def a(element):
    audio=elevenlabs.generate(
    text=element,
    voice=voice[1])
    return audio
    #elevenlabs.save(audio, "outputaudiotom.mp3")
    #return audio

def b(element):
    audio=elevenlabs.generate(
    text=element,
    voice=voice[4])
    return audio
    #return audio
    #elevenlabs.save(audio, "outputaudioalice.mp3")
def c(element):
    audio=elevenlabs.generate(
    text=element,
    voice=voice[7])
    return audio
    #return audio
    #elevenlabs.save(audio, "outputaudiomusic.mp3")

def generate(paragraphs,ToAudio):
    for index,paragraph in enumerate(paragraphs):
        audio=ToAudio(paragraph)
        elevenlabs.save(audio,"output/clip_"+str(index)+".mp3")
def ToAudio(element):
    if element.startswith("Tom:"):
        element=element[len("Tom:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[1])
        return audio
    elif element.startswith("Alice:"): 
        element=element[len("Alice:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[0])
        return audio
    elif element.startswith("[Intro"):
        element=element[len("[Intro"):].strip()
        with open('crime_intro.mp3', 'rb') as file:
            audio = file.read()
        return audio
def glue(paragraphs):
    concatenated_audio = AudioSegment.silent(duration=0)
    for index,paragraph in enumerate(paragraphs):
        audio = AudioSegment.from_mp3("output/clip_"+str(index)+".mp3")
        concatenated_audio += audio
    return concatenated_audio
    


def main():
    #file_path = "C:\Users\DELL\Documents\GitHub\podcastpage\TextToAudio\test.txt"

    try:
        with open("C:/Users/DELL/Documents/GitHub/podcastpage/TextToAudio/word.txt",'r') as file:
            text = file.read()

        # Segment the text into paragraphs
        paragraphs = segment_paragraphs(text)
        
        paragraphs=paragraphs[:-1]
        print(paragraphs)


        # Print the labeled paragraphs
        generate(paragraphs,ToAudio)
        #glue(audiofiles)
        finalaudio=glue(paragraphs)
        finalaudio.export("outputaudiofinal.mp3",format="mp3")
    
    
            

    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

if __name__ == "__main__":
    main()

