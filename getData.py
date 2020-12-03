#爬取sports technology education finance entertainment 各3000篇
#sports https://sports.qq.com/l/others/newsroll.htm
 
from requests import *
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
}
sports
url="https://sports.qq.com/l/others/newsroll.htm";
page_text=get(url,headers=headers).text
tree=etree.HTML(page_text)
a_list=tree.xpath("/html/body/div[4]/div[3]/div[1]/ul/li/a")
for a in a_list:
    print(a.xpath("@href")[0])
for i in range(2,51):
    url="https://sports.qq.com/l/others/newsroll_"+str(i)+".htm";
    page_text=get(url,headers=headers).text
    tree=etree.HTML(page_text)
    a_list=tree.xpath("/html/body/div[4]/div[3]/div[1]/ul/li/a")
    with open("sportsurl.txt","a") as f:
        for a in a_list:
            f.write(a.xpath("@href")[0]+"\n")


with open("sportsurl.txt","r") as f:
    for i in range(2500):
        url=""
        url=f.readline().strip()
        page_text=get(url,headers=headers).text
        tree=etree.HTML(page_text)
        text_list=tree.xpath('//*[@id="Cnt-Main-Article-QQ"]/p/text()')
        with open("sports.txt","a",encoding="utf-8") as f2:
            for text in text_list:
                f2.write(text)
            f2.write("\n")
print("sports爬取完毕")
#           
# technology
# url="http://tech.163.com/special//blockchain_2018/";
# page_text=get(url,headers=headers).text
# tree=etree.HTML(page_text)
# a_list=tree.xpath('//*[@id="news-flow-content"]/li/div/h3/a')
# with open("technologyurl.txt","a") as f:
#     for a in a_list:
#         f.write(a.xpath("@href")[0]+"\n")
# for i in range(2,9):
#     url="http://tech.163.com/special//blockchain_2018_0"+str(i)+"/";
#     page_text=get(url,headers=headers).text
#     tree=etree.HTML(page_text)
#     a_list=tree.xpath('//*[@id="news-flow-content"]/li/div/h3/a')
#     with open("technologyurl.txt","a") as f:
#         for a in a_list:
#             f.write(a.xpath("@href")[0]+"\n")
# for i in range(10,11):
#     url="http://tech.163.com/special//blockchain_2018_"+str(i)+"/";
#     page_text=get(url,headers=headers).text
#     tree=etree.HTML(page_text)
#     a_list=tree.xpath('//*[@id="news-flow-content"]/li/div/h3/a')
#     with open("technologyurl.txt","a") as f:
#         for a in a_list:
#             f.write(a.xpath("@href")[0]+"\n")

# with open("technologyurl.txt","r") as f:
#     for i in range(1620):
#         url=""
#         url=f.readline().strip()
#         if i>900:
#             page_text=get(url,headers=headers).text
#             tree=etree.HTML(page_text)
#             text_list=tree.xpath('//*[@id="endText"]/p/text()')
#             with open("technology.txt","a",encoding="utf-8") as f2:
#                 for text in text_list:
#                     f2.write(text.strip())
#                 f2.write("\n")
# print("technology爬取完毕")

#education
# http://edu.people.com.cn/n1/2020/1123/c367001-31941217.html
# url="http://edu.people.com.cn/GB/226718/index.html";
# page_text=get(url,headers=headers).text
# tree=etree.HTML(page_text)
# a_list=tree.xpath('/html/body/div[6]/div[1]/div[2]/ul/li/a')
# with open("educationurl.txt","a") as f:
#     for a in a_list:
#         f.write("http://edu.people.com.cn"+a.xpath("@href")[0]+"\n")
# for i in range(2,8):
#     url="http://edu.people.com.cn/GB/226718/index"+str(i)+".html";
#     page_text=get(url,headers=headers).text
#     tree=etree.HTML(page_text)
#     a_list=tree.xpath('/html/body/div[6]/div[1]/div[2]/ul/li/a')
#     with open("educationurl.txt","a") as f:
#         for a in a_list:
#             f.write("http://edu.people.com.cn"+a.xpath("@href")[0]+"\n")

# with open("educationurl.txt","r") as f:
#     for i in range(1580):
#         url=""
#         url=f.readline().strip()
#         page_text=get(url,headers=headers).text.encode("iso-8859-1").decode("GBK")
#         tree=etree.HTML(page_text)
#         text_list=tree.xpath('//p/text()')
#         with open("education.txt","a",encoding="utf-8") as f2:
#             for text in text_list:
#                 f2.write(text.strip())
#             f2.write("\n")
# print("education爬取完毕")

#打乱顺序
# import numpy as np
# str=[]
# with open("sports.txt","r") as f:    
#     for i in range(1636):
#         str.append(f.readline())
# for i in range(1000):
#     a=np.random.randint(0,2000)
#     b=np.random.randint(0,1000)

