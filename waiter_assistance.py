import spacy
from spacy import displacy
from spacy.symbols import NOUN, NUM

from nltk import Tree
from speech_processing import stt, tts


def tok_format(tok):
    return "_".join([tok.orth_, tok.tag_])


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return (Tree(tok_format(node),
                     [to_nltk_tree(child) for child in node.children]))
    else:
        return tok_format(node)


intro_speech = 'Hello and welcome to our bar. We offer hot, and cold drinks'
tts(intro_speech)

hot_menu_options = 'Your options for hot drinks are'
tts(hot_menu_options)

hot_drinks = ['tea', 'cappuccino', 'green tea', 'latte']
for h_drink in hot_drinks:
    tts(h_drink)

cold_menu_options = 'for the cold drinks, we have'
tts(cold_menu_options)

cold_drinks = ['scotch', 'beer', 'lemon juice', 'water', 'ice tea']

for c_drink in cold_drinks:
    tts(c_drink)

order_req = 'So what you want to order?'
tts(order_req)

response = stt(verbose=0)

# python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')
doc = nlp(response)

[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]

nouns = []
for possible_subject in doc:
    # Instead of Noun, we use NUM for numbers
    if possible_subject.pos == NOUN:
        nouns.append(possible_subject.text)

for noun in nouns:
    print(noun)

alcohol = ['scotch', 'beer']

non_alcohol = ['lemon juice', 'water', 'ice tea',
               'tea', 'cappuccino', 'green tea', 'latte']

noun = nouns[0]

if(noun in alcohol):
    tts('How old are you?')
    you_said = stt(verbose=0)
    doc = nlp(you_said)
    nums = []
    for possible_subject in doc:
        if possible_subject.pos == NUM:
            nums.append(possible_subject.text)
    if(int(nums[0]) < 21):
        tts('I am afraid, I cannot sell you a alcohol, next customer please')
    else:
        tts('free drink for your alcoholic ass sir, bye.')
elif(noun in non_alcohol):
    tts('You have just earned yourself a free drink, Enjoy your day, bye.')
else:
    tts('I am sorry we do not offer {} here'.format(noun))
