# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def loadTrainWordsList(name):
    file_path="train/"+name+".txt"
    words_list=[]
    tag_list=[]
    with open(file_path,"r",encoding="utf-8") as f:
        while True:
            line=f.readline()
            if not line:
                break
            else:
                words_list.append(line.strip())
                tag_list.append(name)
    return words_list,tag_list
def loadTestWordsList(name):
    file_path="test/"+name+".txt"
    words_list=[]
    tag_list=[]
    with open(file_path,"r",encoding="utf-8") as f:
        while True:
            line=f.readline()
            if not line:
                break
            else:
                words_list.append(line.strip())
                tag_list.append(name)
    return words_list,tag_list
if __name__ == "__main__":
    data1,tag1=loadTrainWordsList("education")
    data2,tag2=loadTrainWordsList("sports")
    data3,tag3=loadTrainWordsList("technology")
    education_data,education_tag=loadTestWordsList("education")
    sports_data,sports_tag=loadTestWordsList("sports")
    technology_data,technology_tag=loadTestWordsList("technology")
    train_data=data1+data2+data3
    tags_list=tag1+tag2+tag3
    count_vector = CountVectorizer()
    vecot_matrix = count_vector.fit_transform(train_data)
    train_tfidf = TfidfTransformer(use_idf=False).fit_transform(vecot_matrix)
    clf = MultinomialNB().fit(train_tfidf, tags_list)
    education_vector = count_vector.transform(education_data)
    sports_vector = count_vector.transform(sports_data)
    technology_vector = count_vector.transform(technology_data)
    education_tfidf = TfidfTransformer(use_idf=False).fit_transform(education_vector)
    sports_tfidf = TfidfTransformer(use_idf=False).fit_transform(sports_vector)
    technology_tfidf = TfidfTransformer(use_idf=False).fit_transform(technology_vector)
    education_result = clf.predict(education_tfidf)
    sports_result = clf.predict(sports_tfidf)
    technology_result = clf.predict(technology_tfidf)
    print(education_result)
    print(sports_result)
    print(technology_result)
    educationNum=0
    sportsNum=0
    technologyNum=0
    for i in list(education_result):
        if i == "education":
            educationNum+=1
    for i in list(sports_result):
        if i == "sports":
            sportsNum+=1
    for i in list(technology_result):
        if i == "technology":
            technologyNum+=1
    education_success=educationNum/200
    sports_success=sportsNum/200
    technology_success=technologyNum/200
    print("education 成功率:"+str(education_success))
    print("sports 成功率:"+str(sports_success))
    print("technology 成功率:"+str(technology_success))
    