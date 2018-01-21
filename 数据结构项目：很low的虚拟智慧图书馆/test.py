from xpinyin import Pinyin
p=Pinyin()
str1='上海'
str2='shanghai'
s1=p.get_pinyin(str1,'')
s2=p.get_pinyin(str2)
print(s1)
print(s2)