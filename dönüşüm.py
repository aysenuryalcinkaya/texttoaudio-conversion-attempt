import xml.etree.ElementTree as ET
from moviepy.editor import VideoFileClip, concatenate_videoclips
import pyttsx3

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    texts = []
    for text_elem in root.iter('Text'):
        start_time = float(text_elem.attrib['start'])
        end_time = float(text_elem.attrib['end'])
        text = text_elem.text.strip()
        texts.append((start_time, end_time, text))
    return texts

def text_to_speech(text, output_file):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Okuma hızını ayarlayabilirsiniz
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    engine.stop()

def generate_video(xml_file, output_file):
    texts = parse_xml(xml_file)
    clips = []

    for i, (start_time, end_time, text) in enumerate(texts):
        print(text)  # Ekrana yazdırma
        clip_file = f'temp_clip_{i}.mp3'
        text_to_speech(text, clip_file)
        clip = VideoFileClip(clip_file)
        clips.append(clip)

    if clips:
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(output_file, codec='libx264')

if __name__ == '__main__':
    xml_file = 'metin.xml'
    output_file = 'output.mp4'

    generate_video(xml_file, output_file)
