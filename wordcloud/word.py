import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud,STOPWORDS

a=str(input("Enter the name of which you want to make cloud: "))
title=wikipedia.search(a)[0]
page=wikipedia.page(title)
text=page.content
print(text)
bg=np.array(Image.open("black.png"))
unwated_words=set(STOPWORDS)
wordclo=WordCloud(background_color="black",max_words=400,mask=bg,stopwords=unwated_words)
wordclo.generate(text)
wordclo.to_file("sample.png")

