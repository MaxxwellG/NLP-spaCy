import spacy
 # ===== PYTHON Natural Processing Language (NLP) libraryb spaCy ============

# spaCy is an Industrial-Strength Python natural language processing library.
# spaCy is designed to help you do real work — to build real products, or gather real insights.
# The library respects your time, and tries to avoid wasting it.
# It's easy to install, and its API is simple and productive(https://spacy.io/usage/spacy-101)

 # --------- Installation of spaCY-------

# Before we proceed with the basics of spaCy,
# we first need to install spaCy. We can install spaCy using pip,
# a package installer for Python. We can execute the following command to install spaCy:

# pip install spacy

# In this example, we are downloading the en_core_web_sm model, which is a small English language model that includes vocabulary, syntax, and entities.

# ------------ Working with spaCy-------

# spaCy is an open-source natural language processing library that is designed to be fast and efficient.
# spaCy provides a wide range of functionalities for various natural language processing tasks such as tokenization, named entity recognition, dependency parsing, and more.
# Here's a simple example of how we can use spaCy to perform basic natural language processing tasks such as tokenization, part-of-speech tagging, and dependency parsing.

# import spacy(ony after installing spacy)
import spacy

# load the english model
nlp = spacy.load('en_core_web_sm')


text = "spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython. The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."

# Tokenisation

# Tokenisation is a foundational step in many NLP tasks. Tokenising text is the
# process of splitting a piece of text into words, symbols, punctuation, spaces,(https://realpython.com/natural-language-processing-spacy-python/)
# and other elements, thereby creating “tokens”. A naive way to do this is to
# simply split the string on white space:

doc = nlp(text)

doc.text.split()

output = ['spaCy', 'is', 'an', 'open-source', 'software', 'library', 'for', 'advanced', 'natural', 'language', 'processing,', 'written', 'in', 'the', 'programming', 'languages',
          'Python', 'and', 'Cython.', 'The', 'library', 'is', 'published', 'under', 'the', 'MIT', 'license', 'and', 'its', 'main', 'developers', 'are', 'Matthew', 'Honnibal', 'and',
          'Ines', 'Montani,', 'the', 'founders', 'of', 'the', 'software', 'company', 'Explosion.']

# On the surface, this looks fine. But, note that a) it disregards the punctuation and
# Put differently, it is naive, it fails to recognise elements of the text that help
# us (and a machine) to understand its structure and meaning. Let’s see how spaCy handles this:
[token.orth_ for token in doc]

output = ['spaCy', 'is', 'an', 'open', '-', 'source', 'software', 'library', 'for', 'advanced', 'natural', 'language',
          'processing', ',', '\n', 'written', 'in', 'the', 'programming', 'languages', 'Python', 'and', 'Cython', '.', '\n', 'The', 'library', 'is', 'published', 'under', 'the', 'MIT', 'license', 'and',
          'its', 'main', 'developers', 'are', 'Matthew', 'Honnibal', 'and', 'Ines', 'Montani', ',', '\n', 'the', 'founders', 'of', 'the', 'software', 'company', 'Explosion', '.']

# Here we access the each token’s .orth_ method, which returns a string representation
# of the token rather than a spaCy token object, this might not always be desirable,
# but worth noting. SpaCy recognises punctuation and is able to split these punctuation
# tokens from word tokens. Many of spaCy’s token methods offer both string and integer
# representations of processed text – methods with an underscore suffix return strings,
# methods without an underscore suffix return integers. For example:
# (hyerion bootcamp  Task37, example.py)
print([(token, token.orth_, token.orth) for token in doc])

'''
[(spaCy, 'spaCy', 6772933960739496234), (is, 'is', 3411606890003347522), (an, 'an', 15099054000809333061), (open, 'open', 8092125317261700160), (-, '-', 9153284864653046197), (source, 'source', 9032917268300750242), (software, 'software', 8212201967714533330), (library, 'library', 1785747669126016609), (for, 'for', 16037325823156266367), (advanced, 'advanced', 3943929226210916060), (natural, 'natural', 3743574233330547430), (language, 'language', 8740476009882919263), (processing, 'processing', 10935198773122488114), (,, ',', 2593208677638477497), (
, '\n', 962983613142996970), (written, 'written', 15025889640951653632), (in, 'in', 3002984154512732771), (the, 'the', 7425985699627899538), (programming, 'programming', 17860067660221736314), (languages, 'languages', 16338895541063414738), (Python, 'Python', 15328717830860514303), (and, 'and', 2283656566040971221), (Cython, 'Cython', 1240263822940474778), (., '.', 12646065887601541794), (
, '\n', 962983613142996970), (The, 'The', 5059648917813135842), (library, 'library', 1785747669126016609), (is, 'is', 3411606890003347522), (published, 'published', 6032455370920491303), (under, 'under', 11091676426636450224), (the, 'the', 7425985699627899538), (MIT, 'MIT', 14376736078981358651), (license, 'license', 9536024028233391360), (and, 'and', 2283656566040971221), (its, 'its', 12513610393978129441), (main, 'main', 11645434534719424374), (developers, 'developers', 2480558665256297208), (are, 'are', 5012629990875267006), (Matthew, 'Matthew', 17272523751765076137), (Honnibal, 'Honnibal', 14421789472383257804), (and, 'and', 2283656566040971221), (Ines, 'Ines', 2670756221512064827), (Montani, 'Montani', 13007990771093603325), (,, ',', 2593208677638477497), (
, '\n', 962983613142996970), (the, 'the', 7425985699627899538), (founders, 'founders', 16713696713169059598), (of, 'of', 886050111519832510), (the, 'the', 7425985699627899538), (software, 'software', 8212201967714533330), (company, 'company', 6905553075311563409), (Explosion, 'Explosion', 4396889584336059458), (., '.', 12646065887601541794)]

'''
# print token  and 
# If you want to avoid returning tokens that are punctuations or white space, spaCy
# provides convienient methods for this
# .is_punct indicates whether the token is a punctuation symbol or not.
# .is_space indicates whether the token is a space symbol or not.

print([token.orth_ for token in doc if not token.is_punct | token.is_space])
'''
['spaCy', 'is', 'an', 'open', 'source', 'software', 'library', 'for', 'advanced', 'natural', 'language',
'processing', 'written', 'in', 'the', 'programming', 'languages', 'Python', 'and', 'Cython', 'The', 'library',
'is', 'published', 'under', 'the', 'MIT', 'license', 'and', 'its', 'main', 'developers', 'are', 'Matthew', 'Honnibal', 'and', 'Ines', 'Montani', 'the', 'founders', 'of', 'the', 'software', 'company', 'Explosion']
'''

# Let's identify stop words. We imported the word list above, so it's just a
# matter of iterating through the tokens stored in the Doc object and performing
# a comparison:
# .is_stop indicates whether the token is a stop word or not

for word in doc:
    if word.is_stop == True:
        print(word)
'''
is
an
for
in
the
and
The
is
under
the
and
its
are
and
the
of
the
'''


# Lemmatisation

# A related task to tokenisation is lemmatisation. Lemmatisation is the process
# of reducing a word to its base form, its mother word if you like. Different
# uses of a word often have the same root meaning. For example, practice, practised
# and practising all essentially refer to the same thing. It is often desirable
# to standardise words with similar meaning to their base form. With spaCy we can
# access each word’s base form with a token’s .lemma_ method:

sing = "sang singing sing"
nlp_practice = nlp(sing)
print([word.lemma_ for word in nlp_practice])

''' ['sing', 'sing', 'sing'] '''
# we can also print the token and it lemma this way:
for token in doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
        

# In this example, you check to see if the original word is different from the lemma, and if it is, you print both the original word and its lemma.

'''
               spaCy : spacy
                  is : be
             written : write
           languages : language
                 The : the
                  is : be
           published : publish
          developers : developer
                 are : be
            founders : founder

'''

# Word Frequency

# You can now convert a given text into tokens and perform statistical analysis on it. This analysis can give you various insights, 
# such as common words or unique words in the text:(https://realpython.com/natural-language-processing-spacy-python/)

# import Counter  module to count occurrence from collections library
from collections import Counter

words = [token.text for token in doc if not token.is_stop and not token.is_punct]

print(Counter(words).most_common(5))

'''[('\n', 3), ('software', 2), ('library', 2), ('spaCy', 1), ('open', 1)]

'''

# Why is this useful? An immediate use case is in machine learning, specifically
# text classification. Lemmatising the text prior to, for example, creating a
# “bag-of-words” avoids word duplication and, therefore, allows for the model to
# build a clearer picture of patterns of word usage across multiple documents.


# Entity recognition

# Entity recognition is the process of classifying named entities found in a text
# into pre-defined categories, such as persons, places, organisations, dates,
# etc. spaCy uses a statistical model to classify a broad range of entities,
# including persons, events, works-of-art and nationalities / religions (see the
# documentation for the full list https://spacy.io/docs/usage/entity-recognition).

# For example, let’s take the first two sentences from Priyanka Chopra's wikipedia
# entry. We will parse this text, then access the identified entities using the
# Doc object’s .ents method. With this method called on the Doc we can access
# additional Token methods, specifically .label_ and .label:

print([(i, i.label_, i.label) for i in doc.ents])

'''['(Cython, 'PERSON', 380), (MIT, 'ORG', 383), (Matthew Honnibal, 'PERSON', 380), (Ines Montani, 'PERSON', 380)]
'''

# Part-of-Speech Tagging
#Part of speech or POS is a grammatical role that explains how a particular word is used in a sentence. There are typically eight parts of speech:

# 1-  Noun
# 2-  Pronoun
# 3-  Adjective
# 4-  Verb
# 5-  Adverb
# 6-  Preposition
# 7-  Conjunction
# 8-  Interjection

# Part-of-speech tagging is the process of assigning a POS tag to each token depending on its usage in the sentence. POS tags are useful for assigning a syntactic category like noun or verb to each word.

# Print the tokens and their part-of-speech tags

for token in doc:
    print(f"{str(token.text):>20} : {token.pos_}")
    
'''spaCy      : INTJ
is         : AUX
an         : DET
open       : ADJ
-          : PUNCT
source     : NOUN
software   : NOUN
library    : NOUN
for        : ADP
advanced   : ADJ
natural    : ADJ
language   : NOUN
processing : NOUN
,          : PUNCT

          : SPACE
written    : VERB
in         : ADP
the        : DET
programming : NOUN
languages  : NOUN
Python     : PROPN
and        : CCONJ
Cython     : PROPN
.          : PUNCT

          : SPACE
The        : DET
library    : NOUN
is         : AUX
published  : VERB
under      : ADP
the        : DET
MIT        : PROPN
license    : NOUN
and        : CCONJ
its        : PRON
main       : ADJ
developers : NOUN
are        : AUX
Matthew    : PROPN
Honnibal   : PROPN
and        : CCONJ
Ines       : PROPN
Montani    : PROPN
,          : PUNCT

          : SPACE
the        : DET
founders   : NOUN
of         : ADP
the        : DET
software   : NOUN
company    : NOUN
Explosion  : PROPN
.          : PUNCT
 
'''

# In the above code, we first loaded the en_core_web_sm language model using the spacy.load() function. We then defined a text that we want to process. We then processed the text using the language model and obtained a doc object.

# We then printed the tokens in the text and their part-of-speech tags using a for loop. We also printed the dependency parse of the text, which shows the relationships between the words in the text. We printed the head of each token, its dependency label, its part-of-speech tag, and its children.

