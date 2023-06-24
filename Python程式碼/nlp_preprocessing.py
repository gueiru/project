import jieba
import csv

comment_list = []
keyword_list = []

with open('comment.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    header = next(reader)
    target_column_index = header.index('Comment')
    for row in reader:
        comment = row[target_column_index]
        comment = comment.replace(":", "")
        comment_list.append(comment)
        
'''for comment in comment_list:
    text = jieba.cut(comment)
    for word in text:
        keyword_list.append(word)
'''

with open('keyword_preprocessing.csv', 'w', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    for comment in comment_list:
        text = jieba.cut(comment)
        word_list = list(text)
        writer.writerow(word_list)

print("-----end-----")
