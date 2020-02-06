import spacy
from collections import Counter
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
text = ("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!")
text_doc = nlp(text)
words = [token.text for token in text_doc if not token.is_punct and not token.is_stop]
word_freq = Counter(words)
#top 10 most frequent words
print(word_freq.most_common(10))
#list of unique words
unique_words = [token for(token, freq) in word_freq.items() if freq == 1]
print(unique_words)

nouns = []
adjectives = []
verbs = []

for token in text_doc:
    if token.pos_ == "NOUN":
        nouns.append(token)
    if token.pos_ == "VERB":
        verbs.append(token)
    if token.pos_ == 'ADJ':
        adjectives.append(token)
#total number of nouns, adjectives, verbs
print(f'Nouns: {len(nouns)}, Adjectives: {len(adjectives)}, Verbs: {len(verbs)}')
#showing named entity
displacy.serve(text_doc, style='dep')




