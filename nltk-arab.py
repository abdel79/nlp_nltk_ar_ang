import nltk # importing natural language tool kit
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger') # used for tagging words with their parts of speech
nltk.download('wordnet')
from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import sent_tokenize 
text1 ="""ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي وهي بدايات الجبر، ومن المهم فهم كيف كانت هذه
الفكرة الجديدة مهمة، فقد كانت خطوة نورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر کان نظرية موحدة تتيح الأعداد الكسرية
والأعداد اللا كسرية، والمقادير الهندسية وغيرها، أن تتعامل على أنها أجسام جبرية، وأعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان
موجودا من قبل، وقم وسيلة للتنمية في هذا الموضوع مستقبلا. وجانب آخر مهم لإدخال أفكار الجبر وهو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث
من قبل """

tokens = nltk.word_tokenize(text) # A tokenizer that divides a string into substrings by splitting on the specified string (defined in subclasses).


print("After Split:",tokens)
sent=sent_tokenize(text)
print("After sentence token:",sent)
grammar ="""mychunk:{<NN.?><VBD.?><JJ.?>*<CC>?}"""
chunker =nltk.RegexpParser(grammar)
output = chunker.parse(tokens_tag)
print(output)

import nltk
stm=[]
for i in tokens: 
  stemm = nltk.stem.PorterStemmer()
  stm.append(stemm.stem(i))
stm