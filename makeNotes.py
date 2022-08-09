## Importing required libraries
import speech_recognition as sr
from fpdf import FPDF
import datetime



# function to convert audio to text
def audio_to_text(audio):

    r = sr.Recognizer()
    voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
        pravi_speaks('Sorry, I could not get that')
        return -1
    except sr.RequestError:
        pravi_speaks('Sorry, my speech service is down, try again later.')
        return 0
    return voice_data


# given transcript
transcipt = "I have to say that this hotel has the worst customer support ever. It is a shame that people in management positions (who should be more respectful of their customers) are rude and have bad attitudes. They completely ruined my vacations. English is a West Germanic language of the Indo-European language family, originally spoken by the inhabitants of early medieval England. It is named after the Angles, one of the ancient Germanic peoples that migrated from Anglia, a peninsula on the Baltic Sea (not to be confused with East Anglia in England), to the area of Great Britain later named after them: England. The closest living relatives of English include Scots, followed by the Low Saxon and Frisian languages. While English is genealogically West Germanic, its vocabulary is also distinctively influenced by Old Norman French and Latin, as well as by Old Norse (a North Germanic language). Speakers of English are called Anglophones."

# given link map
LinkMap = {'worst customer support': 'https://www.helpscout.com/blog/bad-customer-service-stories/', 'bad attitude': 'https://en.wikipedia.org/wiki/Bad_Attitude', 'management position': 'https://www.rasmussen.edu/degrees/business/blog/top-management-positions-future-business-leaders/', 'customer': 'https://en.wikipedia.org/wiki/Customer', 'people': 'https://en.wikipedia.org/wiki/People_(magazine)', 'hotel': 'https://www.makemytrip.com/hotels/', 'vacation': 'https://en.wikipedia.org/wiki/Vacation_(2015_film)', 'shame': 'https://en.wikipedia.org/wiki/Shame_(2011_film)', 'relative of english': 'https://en.wikipedia.org/wiki/English_relative_clauses', 'north germanic language': 'https://en.wikipedia.org/wiki/North_Germanic_languages', 'old norman french': 'https://en.wikipedia.org/wiki/Old_Norman', 'area of great': 'https://en.wikipedia.org/wiki/Great_Britain', 'ancient germanic people': 'https://en.wikipedia.org/wiki/Germanic_peoples', 'early medieval england': 'https://en.wikipedia.org/wiki/England_in_the_Middle_Ages', 'speaker of english': 'https://en.wikipedia.org/wiki/English-speaking_world', 'european language family': 'https://en.wikipedia.org/wiki/Indo-European_languages', 'west germanic language': 'https://en.wikipedia.org/wiki/West_Germanic_languages', 'called anglophones': 'https://en.wikipedia.org/wiki/Anglophone_problem'}

# funciton to make pdf notes
def makePdfNotes(txt, LinkMap):
    # saving FPDF() class into a variable pdf
    pdf = FPDF()
    # adding a page
    pdf.add_page()
    pdf.set_font("Arial", size = 18)
    # creating a cell
    pdf.cell(200, 10, txt = "Notes",ln = 1, align = 'C')
    # setting style and font
    pdf.set_font("Arial", size = 12)
    
    # writing the content to a pdf file
    pdf.write(5,transcipt)
    pdf.write(5,"\n")
    pdf.write(5,"\n\nImportant Links:\n")
    # Then put a blue underlined link
    pdf.set_text_color(0, 0, 255)
    #pdf.set_font('', 'U')
    k = 1
    for key in LinkMap:
        pdf.write(5, str(k)+"."+key, LinkMap[key])
        pdf.write(5,"\n")
        k = k+1
    filename1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    pdf.output(str(filename1)+".pdf")

# function call
makePdfNotes(transcipt, LinkMap)

 
