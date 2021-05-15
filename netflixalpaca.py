import pandas, re
from collections import Counter

nvh = pandas.read_csv("NetflixViewingHistory.csv")

words = []

for index, show in nvh.iterrows():
    showwords = show["Title"].split(' ')
    for word in showwords:
        clean = re.sub(r'\W+', '', word)
        words.append(clean.lower())

for key, value in Counter(words).most_common():
    print('{} {}'.format(key, value))