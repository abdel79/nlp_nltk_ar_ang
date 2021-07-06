import nltk # importing natural language tool kit
nltk.download('wordnet') # lexical database for the English language
nltk.download('stopwords') #English words which does not add much meaning to a sentence
nltk.download('punkt') # divides a text into a list of sentences by using an unsupervised algorithm to build a model for abbreviation words



from nltk.corpus import state_union, stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import state_union, stopwords


data = """Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely
the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from
the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational
numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new
development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the
subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a
way which had not happened before."""


data=data.replace('\n'," ")

stopWords = set(stopwords.words('english'))

words=word_tokenize(data)

wordFiltered=[]

stemmer = PorterStemmer()

lemmatizer = WordNetLemmatizer()

for w in words:
    if w not in stopWords:
        wordFiltered.append(w)

print("{0:20}{1:20}{2:20}".format("word","Stemmer","Lemmatizer"))
for l in wordFiltered:
 print("{0:20}{1:20}{2:20}".format(l,stemmer.stem(l),lemmatizer.lemmatize(l)))

def p():
    try:
        for i in words:
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
         print(str(e))

print("\ntagging")
p()

import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag #process to mark up the words in text format for a particular part of a speech based on its definition and context
from nltk import RegexpParser #RegexpParser uses a set of regular expression patterns to specify the behavior of the parser

text =  """Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely
the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from
the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational
numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new
development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the
subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a
way which had not happened before.""".split ()

print("Après fractionnement :",text)
tokens_tag = pos_tag(text)
print("After Token:",tokens_tag)
grammar= """mychunk:{<NN.?><VBD.?><JJ.?>*<CC>?}"""
chunker = nltk.RegexpParser(grammar)
print("After Regex:",chunker)
output = chunker.parse(tokens_tag)
print("After Chunking",output)
output.draw()