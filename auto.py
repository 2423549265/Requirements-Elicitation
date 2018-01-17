import json
import codecs
import jieba #ntlk
import re


def word_divide(filename):
    with codecs.open(filename, 'r', 'utf-8') as file:
        dict = json.load(file)

    with open("hfrw.txt", encoding="utf-8") as f:
        hfws = [line.split()[0] for line in f.readlines()]

    hfws = set(hfws)

    with open("train2.txt", 'w', encoding='utf-8') as wf:
        for i in range(len(dict)):
            seg_list = set((jieba.cut(dict[i], cut_all=False, HMM=True)))
            if len(seg_list.intersection(hfws)) > 5:
                wf.write(" ".join(list(seg_list)) + '\n')


word_divide("C:/Users/66425/Desktop/data.json")