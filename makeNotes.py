## Importing required libraries
from fpdf import FPDF
import datetime
import re

# given transcript
transcript = "I have to say that this hotel has the worst customer support ever. It is a shame that people in management positions (who should be more respectful of their customers) are rude and have bad attitudes. They completely ruined my vacations. English is a West Germanic language of the Indo-European language family, originally worst customer support spoken by the inhabitants of early medieval England. It is named after the Angles, one of the ancient Germanic peoples that migrated from called Anglophones Anglia, a peninsula on the Baltic Sea (not to be confused with East Anglia in England), to the area of Great Britain later named after them: England. The closest living relatives of English include Scots, followed by the Low Saxon and Frisian languages. While English is genealogically West Germanic, its vocabulary is also distinctively influenced by Old Norman French and Latin, as well as by Old Norse (a North Germanic language). Speakers of English are called Anglophones  worst customer support."

# important words
#keywords = ['worst customer support', 'bad attitude', 'management position', 'customer', 'people', 'hotel', 'vacation', 'shame', 'relative of english', 'north germanic language','old norman french', 'area of great', 'ancient germanic people', 'early medieval england', 'speaker of english', 'european language family', 'west germanic language', 'called anglophones']
# given link map
LinkMap = {'worst customer support': 'https://www.helpscout.com/blog/bad-customer-service-stories/', 'bad attitude': 'https://en.wikipedia.org/wiki/Bad_Attitude', 'management position': 'https://www.rasmussen.edu/degrees/business/blog/top-management-positions-future-business-leaders/', 'customer': 'https://en.wikipedia.org/wiki/Customer', 'people': 'https://en.wikipedia.org/wiki/People_(magazine)', 'hotel': 'https://www.makemytrip.com/hotels/', 'vacation': 'https://en.wikipedia.org/wiki/Vacation_(2015_film)', 'shame': 'https://en.wikipedia.org/wiki/Shame_(2011_film)', 'relative of english': 'https://en.wikipedia.org/wiki/English_relative_clauses', 'north germanic language': 'https://en.wikipedia.org/wiki/North_Germanic_languages', 'old norman french': 'https://en.wikipedia.org/wiki/Old_Norman', 'area of great': 'https://en.wikipedia.org/wiki/Great_Britain', 'ancient germanic people': 'https://en.wikipedia.org/wiki/Germanic_peoples', 'early medieval england': 'https://en.wikipedia.org/wiki/England_in_the_Middle_Ages', 'speaker of english': 'https://en.wikipedia.org/wiki/English-speaking_world', 'european language family': 'https://en.wikipedia.org/wiki/Indo-European_languages', 'west germanic language': 'https://en.wikipedia.org/wiki/West_Germanic_languages', 'called anglophones': 'https://en.wikipedia.org/wiki/Anglophone_problem'}

def makeSmartNotes(transcript, LinkMap):
  keywords = []
  for key in LinkMap:
    keywords.append(key)
  # getting start and end indices of keywords
  keyword_inds = []
  for keyword in keywords:
    for a in list(re.finditer(keyword, transcript.lower())):
      keyword_inds.append((a.start(), a.end())) 
  keyword_inds.sort()

  ## pdf notes generation
  pdf = FPDF()
  # adding a page
  pdf.add_page()
  pdf.set_font("Arial", size = 18)
  # creating a cell
  pdf.cell(200, 10, txt = "Notes",ln = 1, align = 'C')
  # setting style and font
  pdf.set_font("Arial", size = 12)
  # writing the content to a pdf file
  keyword_list_index =  0 #t
  normal_text_start = 0 # i
  keyword_start =  keyword_inds[keyword_list_index][0] # j
  keyword_end = keyword_inds[keyword_list_index][1] # k

  prev = 0
  while(keyword_start < len(transcript) and keyword_list_index<len(keyword_inds)):
    keyword_start = keyword_inds[keyword_list_index][0]
    keyword_end = keyword_inds[keyword_list_index][1]
    if keyword_start > prev:
      pdf.set_text_color(0, 0, 0)
      pdf.write(5,transcript[normal_text_start:keyword_start])
      pdf.set_text_color(0, 0, 255)
      pdf.write(5, transcript[keyword_start:keyword_end], LinkMap[transcript[keyword_start:keyword_end].lower()])
      pdf.set_text_color(0, 0, 0)
      pdf.write(5,transcript[keyword_end])
      normal_text_start = keyword_end+1
      prev = keyword_end 
    keyword_list_index = keyword_list_index+1

  filename1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
  pdf.output(str(filename1)+".pdf")

makeSmartNotes(transcript, LinkMap)


 
