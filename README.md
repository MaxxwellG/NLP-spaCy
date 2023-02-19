# NLP-spaCy
an Express solution for installing and working  spaCy ,  a python library for NLP(Natural Prcessing Language) 


#  Projec Name
NLP-spaCy

# A brief description of the project
This project is just an  express presentation of the Python Natural Language Processing library spaCy giving an idea of what spaCy can do .

 ## Installation

 - Clone  the repository
 
 git clone https://github.com/MaxxwellG/NLP-spaCy.git

 -Install the required packages by running in the command prompt or twerminal and run :

pip install -r requirements.txt

or go to the root of the repository directory and run the pip  command to automatically  create the requirements.txt file:

pip freeze > requirements.txt

# Usage
This project can be use to get started with spaCy  and play around  with some examples with key concepts like 
tokenisation , lemamatisation, word frequency in a text etc...

# ------------ Working with spaCy-------

# Before we proceed with the basics of spaCy,
pip install spacy

# spaCy is an open-source natural language processing library that is designed to be fast and efficient.
# spaCy provides a wide range of functionalities for various natural language processing tasks such as tokenization, named entity recognition, dependency parsing, and more.
# Here's a simple example of how we can use spaCy to perform basic natural language processing tasks such as tokenization, part-of-speech tagging, and dependency parsing.

# import spacy(ony after installing spacy)
import spacy

# Downnload the simple English model
python3 -m spacy download en_core_web_sm

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
 

 # Contributing 
 Contributions are welcome!

 # License
 Distributed under the GNU license. see 'LICENSE'  for more information.
