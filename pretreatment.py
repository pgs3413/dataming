# -*- coding:utf-8 -*-
import re
import jieba.posseg
import numpy as np
def getStopWord():
    stop_words=[]
    with open("stopwords.txt","r",encoding="utf-8") as f:
        while True:
            line=f.readline()
            if not line :
                break
            else:
                stop_words.append(line.strip())
    return stop_words

def cut_words(path):
    file_path=path+".txt"
    news_list=[]
    stop_words=getStopWord()
    with open(file_path,"r",encoding="utf-8") as f:
        while True:
            line=f.readline()
            if not line:
                break
            else:
                news_list.append(line.strip())
    for news in news_list:    
        new=re.sub("[@·《》、.%，。？“”（）：(\u3000)(\xa0)！… ；▼]|[a-zA-Z0-9]|['月''日''年']", "", news)
        words = jieba.posseg.cut(new)
        words_list=[]
        for word in words:
            if len(word.word)>1 and word.flag=="n" and word.word not in stop_words:
                words_list.append(word.word)
        if len(words_list)>10:        
            with open(path+"_clean.txt","a",encoding="utf-8") as f:
                for w in words_list:
                    f.write(w+" ")
                f.write("\n")

def mixWords(path):
    #打乱顺序
    words_list=[]
    file_path=path+"_clean.txt"
    new_path=path+"_clean2.txt"
    with open(file_path,"r",encoding="utf-8") as f:    
        while True:
            line=f.readline()
            if not line:
                break
            else:
                words_list.append(line)
    for i in range(2000):
        a=np.random.randint(0,1300)
        b=np.random.randint(0,1300)
        temp=words_list[a]
        words_list[a]=words_list[b]
        words_list[b]=temp
    with open(new_path,"a",encoding="utf-8") as f:
        for w in words_list:
            f.write(w.strip()+"\n")


if __name__ == "__main__":
    # cut_words("education")
    # print("education finish")
    # cut_words("sports")
    # print("sports finish")
    # cut_words("technology")
    # print("technology finish")
    mixWords("education")
    print("education finish")
    mixWords("sports")
    print("sports finish")
    mixWords("technology")
    print("technology finish")
