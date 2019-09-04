import markovify
import pandas
from random import randint
import string
printable = set(string.ascii_letters)

# ingredients,post_content,summary,title
frame = pandas.read_csv('./scraper/out.csv')

title_model = markovify.Text(' '.join(frame['title'].dropna().values))
# ingredients_train = ' '.join(frame.ingredients.dropna().values).encode('ascii', errors='ignore').decode()
# print(ingredients_train)
# ingredients_model = markovify.Text(ingredients_train)
post_model = markovify.Text(' '.join(frame.post_content.dropna().values))
summary_model = markovify.Text(' '.join(frame.summary.dropna().values))

print('________ TITLE _______')
title = title_model.make_short_sentence(30)
print(title)

print('______ SUMMARY ________')
summary = summary_model.make_sentence()
print(summary)

print('________ POST ________')
post_content = '\n'.join([post_model.make_sentence() for i in range(randint(6, 15))])
print(post_content)

# print('_______ INGREDIENTS _______')
# ingredients = '\n'.join([ingredients_model.make_short_sentence(5) for i in range(randint(4, 10))])
# print(ingredients)