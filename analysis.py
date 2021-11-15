import jieba
from csv_to_list import read_csv

jieba.set_dictionary('dict.txt.big')
remove_words = [u'的', u'，', u'和', u'是', u'隨著', u'對於', u'對', u'等', u'能', u'都', u'。', u',', u'、', u'中', u'在', u'了', u'通常', u'如果', u'我們', u'需要']
def countAllWord(strlist):
    cutlist = []
    for i in strlist:
        word = jieba.cut(i, cut_all=False)
        for subword in list(word):
            if subword not in remove_words:
                if len(subword) >= 2:
                    cutlist.append(subword)
    #print(cutlist)
    cut_str = " ".join(cutlist)
    #print(cut_str)
    cutlist2 = list(cut_str.split())
    report = {}
    for i in cutlist2:
        if i in report:
            report[i] = report[i] + 1
        else:
            report[i] = 1
    return report, cut_str



