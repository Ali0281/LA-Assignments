import math

import numpy as np

a, b, d = list(map(int, input().split()))
sentences, questions = [], []
for i in range(a):
    sentences.append(input().lower())
for i in range(b):
    questions.append(input().lower())

# find words
words = set()
for sen in sentences:
    words.update(sen.split())
for q in questions:
    # words.update(q.split())
    pass

matrix = np.zeros((len(words), a))
q_save = []

iterable_words = list(words)

for i in range(len(iterable_words)):
    for j in range(a):
        count = sentences[j].split().count(iterable_words[i])
        matrix[i, j] = count

for q in questions:
    temp = np.zeros((1, len(words)))
    for j in range(len(iterable_words)):
        temp[0, j] = q.split().count(iterable_words[j])
    q_save.append(temp)

u, sig, v = np.linalg.svd(matrix)

u = u[:, :d]

temp = np.zeros(matrix.shape)
temp[:a, :a] = np.diag(sig)
sig = temp[:d, :d]

v = v[:d, :]

new_matrix = np.matmul(u, sig)
new_matrix = np.matmul(new_matrix, v)

for i in range(b):
    best_idx = 0
    max_val = -math.inf
    for j in range(a):
        cosine = np.dot(q_save[i], new_matrix[:, j]) / (np.linalg.norm(q_save[i]) * np.linalg.norm(new_matrix[:, j]))
        if cosine > max_val:
            max_val = cosine
            best_idx = j
    print(best_idx)
