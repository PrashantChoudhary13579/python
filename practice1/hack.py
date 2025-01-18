

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

dataset = open("D:\python\practice1\hacker_text_updated.txt")
def create_word_cloud(string):
    maskArray = np.array(Image.opne("hacker.jpeg"))
    cloud = WordCloud(background_color = "white",max_words= 200, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("hacker_wordcloud.png")
dataset = dataset.lower()
create_word_cloud(dataset)