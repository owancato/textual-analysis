import pandas as pd
from matplotlib import pyplot as plt

from analysis import countAllWord
from csv_to_list import read_csv
import nltk
from wordcloud import WordCloud
from PIL import Image
import numpy as np

data = read_csv()
report, cutstr = countAllWord(data)
output = sorted(report.items(), key=lambda x:x[1], reverse=True)
print(output)
output_DF = pd.DataFrame(columns=["關鍵字", "出現字數"], data=output)
output_DF.to_csv('output.csv', encoding='utf_8_sig')

x, y = np.ogrid[:300, :300]
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

font = 'SourceHanSansTW-Regular.otf'

my_wordcloud = WordCloud(background_color='white',font_path=font, mask=mask).generate(cutstr)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()