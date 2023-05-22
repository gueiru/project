# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:22:01 2023

@author: winni
"""
# ============================================================================= 

# Keras內建IMDb網路電影資料集，匯入imdb
# from keras.datasets import imdb
# # load_data() 
# top_words = 1000
# (X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=top_words)
# 
# # 顯示訓練和測試資料集的形狀
# print("X_train.shape: ", X_train.shape)
# print("Y_train.shape: ", Y_train.shape)
# print("X_test.shape: ", X_test.shape)
# print("Y_test.shape: ", Y_test.shape)
# 
# # 顯示訓練資料集中的第一筆評論內容和標籤
# print(X_train[0])
# print(Y_train[0])
 
# # ======解碼顯示IMDb資料集的評論內容=============================================
# 
# #找出每一筆評論內容最大索引值清單
# max_index = max(max(sequence) for sequence in X_train)
# print("Max Index: ", max_index)
# 
# #先取得單字索引清單
# word_index = imdb.get_word_index()
# we_index = word_index["we"]
# print("'we index:", we_index)
# 
# #反轉單字索引字典成為索引單字字典
# decode_word_map = dict([(value, key) for (key, value) in word_index.items()])
# print(decode_word_map[we_index])
# 
# #get（）函式取得索引資料
# decode_indices = [decode_word_map.get(i-3, "?") for i in X_train[0]]
# print(decode_indices)
# 
# #join()函式將清單連接成以空白字元連接的英文字串 
# decode_review = " ".join(decode_indices)
# print(decode_review)
# 
# =============================================================================

import numpy as np
from keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Embedding

import random
import tensorflow as tf

# 設置 Python 的隨機種子
random.seed(42)
# 設置 NumPy 的隨機種子
np.random.seed(42)
# 設置 TensorFlow 的隨機種子
tf.random.set_seed(42)


# load_data()
top_words = 1000
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=top_words)

# 顯示訓練資料集中的第一筆評論內容和標籤
print(X_train[0])
print(Y_train[0])

max_words = 500
X_train = pad_sequences(X_train, maxlen=max_words)
X_test = pad_sequences(X_test, maxlen=max_words)

print("X_train.shape: ", X_train.shape)
print("X_test.shape: ", X_test.shape)


# 定義模型
model = Sequential()
model.add(Embedding(top_words, 32, input_length=max_words))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(1, activation="sigmoid"))
model.summary()

# 編譯模型
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# 訓練模型
history = model.fit(X_train, Y_train, validation_split=0.2, epochs=5, batch_size=128, verbose=2)

# 評估模型
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

# 預測結果
Y_pred = model.predict(X_test)
Y_pred_classes = (Y_pred >= 0.5).astype(int).flatten()

PositiveDict = {1: '滿意', 0: '不滿意'}
def display_info(i):
    print(X_test[i])
    print('影評真實評價：', PositiveDict[Y_test[i]],
          '預測值：', PositiveDict[Y_pred_classes[i]])

display_info(2)


