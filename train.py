import gensim
import multiprocessing

#model = gensim.models.Word2Vec(gensim.models.word2vec.LineSentence('train.txt'), min_count = 100, workers = multiprocessing.cpu_count())
#model.save("train.model")

model = gensim.models.Word2Vec.load("train.model")

with open("high_frequency_word.txt", 'r') as wf, open("result.txt", 'w', encoding='utf-8') as wf2:
   # high_frequency_word = wf.readlines()
    high_frequency_word = wf.read().splitlines()
    for word in high_frequency_word:
        wf2.write(word)
        for i in model.most_similar(word):
            res = " {0} {1}".format(i[0], i[1])
            wf2.write(res)
        wf2.write("\n")