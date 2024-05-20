#Data pre processing
import re as rex
import string
import time

import emoji
import pandas as pd
import spacy
from autocorrect import Speller
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
puchuation = string.punctuation
slang = {'AFAIK': 'As Far As I Know',
         'AFK': 'Away From Keyboard',
         'ASAP': 'As Soon As Possible',
         'ATK': 'At The Keyboard',
         'ATM': 'At The Moment',
         'A3': 'Anytime, Anywhere, Anyplace',
         'BAK': 'Back At Keyboard',
         'BBL': 'Be Back Later',
         'BBS': 'Be Back Soon',
         'BFN': 'Bye For Now',
         'B4N': 'Bye For Now',
         'BRB': 'Be Right Back',
         'BRT': 'Be Right There',
         'BTW': 'By The Way',
         'B4': 'Before',
         'B4N': 'Bye For Now',
         'CU': 'See You',
         'CUL8R': 'See You Later',
         'CYA': 'See You',
         'FAQ': 'Frequently Asked Questions',
         'FC': 'Fingers Crossed',
         'FWIW': 'For What It`s Worth',
         'FYI': 'For Your Information',
         'GAL': 'Get A Life',
         'GG': 'Good Game',
         'GN': 'Good Night',
         'GMTA': 'Great Minds Think Alike',
         'GR8': 'Great!',
         'G9': 'Genius',
         'IC': 'I See',
         'ICQ': 'I Seek you (also a chat program)',
         'ILU': 'ILU: I Love You',
         'IMHO': 'In My Honest/Humble Opinion',
         'IMO': 'In My Opinion',
         'IOW': 'In Other Words',
         'IRL': 'In Real Life',
         'KISS': 'Keep It Simple, Stupid',
         'LDR': 'Long Distance Relationship',
         'LMAO': 'Laugh My A.. Off',
         'LOL': 'Laughing Out Loud',
         'LTNS': 'Long Time No See',
         'L8R': 'Later',
         'MTE': 'My Thoughts Exactly',
         'M8': 'Mate',
         'NRN': 'No Reply Necessary',
         'OIC': 'Oh I See',
         'PITA': 'Pain In The A.',
         'PRT': 'Party',
         'PRW': 'Parents Are Watching',
         'QPSA?': 'Que Pasa?',
         'ROFL': 'Rolling On The Floor Laughing',
         'ROFLOL': 'Rolling On The Floor Laughing Out Loud',
         'ROTFLMAO': 'Rolling On The Floor Laughing My A.. Off',
         'SK8': 'Skate',
         'ASL': 'Age, Sex, Location',
         'THX': 'Thank You',
         'TTFN': 'Ta-Ta For Now!',
         'TTYL': 'Talk To You Later',
         'U': 'You',
         'U2': 'You Too',
         'U4E': 'Yours For Ever',
         'WB': 'Welcome Back',
         'WTF': 'What The F...',
         'WTG': 'Way To Go!',
         'WUF': 'Where Are You From?',
         'W8': 'Wait...',
         '7K': 'Sick:-D Laugher',
         'TFW': 'That feeling when',
         'MFW': 'My face when',
         'MRW': 'My reaction when',
         'IFYP': 'I feel your pain',
         'LOL': 'Laughing out loud',
         'TNTL': 'Trying not to laugh',
         'JK': 'Just kidding',
         'IDC': 'I don`t care',
         'ILY': 'I love you',
         'IMU': 'I miss you',
         'ADIH': 'Another day in hell',
         'IDC': 'I don`t care',
         'ZZZ': 'Sleeping, bored, tired',
         'WYWH': 'Wish you were here',
         'BAE': 'Before anyone else',
         'FIMH': 'Forever in my heart',
         'BSAAW': 'Big smile and a wink',
         'BWL': 'Bursting with laughter',
         'LMAO': 'Laughing my a** off',
         'BFF': ' Best friends forever',
         'CSL': 'Can`t stop laughing'}


#replace sohort language
def replace_short(text):
    new_txt = []
    for w in text.split():
        if w.upper() in slang:
            new_txt.append(slang[w.upper()])
        else:
            new_txt.append(w)
    return ''.join(new_txt)


def remove_html_tag(text):
    reg = rex.compile('<.*?>')
    return reg.sub(r'', text)


def remove_urls(str_val):
    reg = rex.compile(r'http?://\S+|www\.\S+')
    return reg.sub(r'', str_val)


def remove_punc(str_val):
    return str_val.translate(str.maketrans('', '', puchuation))  #faster
    # return ''.join([c for c in text if c not in exclude])#slower


#spelling correction
def spell_correct(text):
    spell = Speller(lang='en')
    return spell(text)


print(spell_correct('ar'))

dfstart = pd.read_json('../startups_demo.json', lines=True)
#make lower all strings
dfstart['description'] = dfstart['description'].str.lower()

#remove html tags
dfstart['description'] = dfstart['description'].apply(remove_html_tag)

#remove urls
dfstart['description'] = dfstart['description'].apply(remove_urls)
start = time.time()
#remove punctuation
dfstart['description'] = dfstart['description'].apply(remove_punc)

#replace short text by full text
dfstart['description'] = dfstart['description'].apply(replace_short)

#replace emoji with relevent text
# dfstart['description'] = emoji.demojize(dfstart['description'])

print(len(dfstart['description'].unique()))

text = "game is on 🔥 🔥"
text = emoji.demojize(text, delimiters=("", ""))  # 'game is on fire fire' emogis to text

# split/tokenize words
print(word_tokenize('asdsa ssss! dsdsad %89 sadasd? and !'))
# split/tokenize sentences
print(sent_tokenize('asdsa ssss! dsdsad %89 sadasd? and !'))

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

'''Stemming of string to covert word to it's common form grammatically like gender, noun, case, voice, mood, 
tense aspect etc, even it's not valid word in language'''

# the stemmer requires a language parameter
snow_stemmer = SnowballStemmer(language='english')

# list of tokenized words
words = ['cared', 'university', 'fairly', 'easily', 'singing',
         'sings', 'sung', 'singer', 'sportingly']

# stem's of each word
stem_words = []
for w in words:
    x = snow_stemmer.stem(w)
    stem_words.append(x)

# print stemming results
for e1, e2 in zip(words, stem_words):
    print(e1 + ' ----> ' + e2)

'''lemmatization is unlike stemming of string, The goal of lemmatization is to reduce a word to its root form, 
also called a lemma. For example, the verb "running" would be identified as "run." Lemmatization studies the 
morphological, or structural, and contextual analysis of words.'''

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               """
sentences = sent_tokenize(paragraph)

lemmatizer = WordNetLemmatizer()
# Lemmatization
print("Word", "Lemma")
for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    for word in words :
        if word not in puchuation:
            print(f"{word} :- {lemmatizer.lemmatize(word)}")
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    # print(words)
    sentences[i] = ' '.join(words)

# print(sentences)