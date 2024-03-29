# -*- coding: utf-8 -*-
"""news sentiment analysis from reddit

Automatically generated by Colaboratory.

"""

pip install praw

from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
nltk.download('vader_lexicon')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

import praw

import praw

reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret_id',
                     user_agent='your_user_name')

headlines = set()
for submission in reddit.domain('cnbc.com').new(limit=None):
    headlines.add(submission.title)
    display.clear_output()
    print(len(headlines))

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:10000], width=100)
##result100 will derive the last 100 data does'nt matter how many days has it been since it was posted on the reddit domain

df = pd.DataFrame.from_records(results)
df.head()

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()

df2 = df[['headline', 'label']]
df2.to_csv('reddit_headlines_labels.csv', mode='a', encoding='utf-8', index=False)

print("Positive headlines:\n")
pprint(list(df[df['label'] == 1].headline)[:200], width=200)

print("\nNegative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:200], width=200)

print(df.label.value_counts())

print(df.label.value_counts(normalize=True) * 100)

fig, ax = plt.subplots(figsize=(8, 8))

counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

plt.show()

