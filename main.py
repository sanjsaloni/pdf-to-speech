import os
from gtts import gTTS
from pdf2docx import Converter
import docx


def text_to_speech(text):
    speech = gTTS(text, lang='en')
    speech_file = './assets/speech.mp3'
    speech.save(speech_file)
    os.system(speech_file)


def convert_pdf_to_doc(file, doc):
    pdf_file = os.path.abspath(file)
    # doc = os.path.abspath(doc)
    new_file = os.path.abspath(doc)
    cv = Converter(pdf_file)
    cv.convert(new_file)


def getText(file):
    print("converting into document")
    doc = docx.Document(file)
    fullText = []
    for para in doc.paragraphs:
            fullText.append(para.text)
    return '\n'.join(fullText)


if __name__ == '__main__':
    try:
        file_path = os.path.abspath('./assets/newdoc.docx')
        os.remove(file_path)
    except FileNotFoundError:
        print("There's no such file")
    except PermissionError:
        print("yoy don't have permission to delete the file")
    except OSError as e:
        print(e)
    convert_pdf_to_doc('./assets/book.pdf', './assets/newdoc.docx')
    file = open('./assets/newdoc.docx', 'rb')
    f = file.read()
    text_to_speech(getText('./assets/newdoc.docx'))
