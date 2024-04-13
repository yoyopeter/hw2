import pandas as pd
import networkx as nx
from nltk import sent_tokenize, word_tokenize

sentences = sent_tokenize(text)

G = nx.Graph()

keywords = ['Alice', 'Rabbit', 'Queen', 'Hatter'] 

for sentence in sentences:
    words = word_tokenize(sentence)
    found_keywords = [word for word in words if word in keywords]
    for i in range(len(found_keywords)):
        for j in range(i + 1, len(found_keywords)):
            if found_keywords[i] != found_keywords[j]:
                G.add_edge(found_keywords[i], found_keywords[j])

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True)
plt.show()
