import json
import codecs
import jieba #ntlk
import re


def word_divide(filename):
    with codecs.open(filename, 'r', 'utf-8') as file:
        dict = json.load(file)

    with open("train.txt", 'w', encoding='utf-8') as wf:
        for i in range(len(dict)):
            seg_list = jieba.cut(dict[i], cut_all=False, HMM=True)
            wf.write(" ".join(seg_list) + '\n')

def word_count(filename):
    word_lst = []
    stop_lst = []
    word_dict = {}
    with open(filename, 'r', encoding='utf-8') as wf, open("word_count_chinese_2.txt", 'w', encoding='utf-8') as wf2, open("stopwords.dat", "r", encoding='utf-8') as wf3:
        stop_lst = set(wf3.readlines())
        count = 0
        words = wf.read().split(r' ')
        total_len = len(words)
        for word in words:
            word = word.strip()
            if re.match("[\u4e00-\u9fa5]{2,}", word) is not None and word not in stop_lst:
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1

            count += 1
            if count % 100 == 0:
                print("{0}/{1}".format(count, total_len))

        res = sorted(word_dict.items(), key=lambda word_dict: word_dict[1], reverse=True)
        res = [x  for x in res if x[1] > 100]
        res = "\n".join(map(lambda x: "{0} {1}".format(x[0], x[1]), res))
        wf2.write(res)
        # for key in word_dict:
        #     wf2.write(key + ' ' + str(word_dict[key]) + '\n')
   # print(sorted(word_dict.items(), key = lambda word_dict:word_dict[1], reverse = True))
#word_divide("C:/Users/66425/Desktop/data.json")
word_count("train2.txt")