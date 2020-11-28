import csv
import matplotlib.pyplot as plt


vals = []
labels = []


with open('Boys.csv', "r") as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        temp = row[1][-1]
        if temp in ['а', 'я', 'ь']:
            temp = row[1][-2:]
        if temp not in labels:
            labels.append(temp)
            vals.append(1)
        else:
            vals[labels.index(temp)] += 1

fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
plt.bar(labels, vals,  align='edge', width=0.3)
for i in range(len(vals)):
    plt.text(labels[i], vals[i], float(vals[i]), horizontalalignment='center', verticalalignment='bottom')
plt.title(label='Мальчики')
plt.show()

vals1 = []
labels1 = []


with open('Girls.csv', "r") as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        temp = row[1][-1]
        if temp in ['а', 'я', 'ь']:
            temp = row[1][-2:]
        if temp not in labels1:
            labels1.append(temp)
            vals1.append(1)
        else:
            vals1[labels1.index(temp)] += 1


fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
plt.bar(labels1, vals1,  align='edge', width=0.3)
for i in range(len(vals1)):
    plt.text(labels1[i], vals1[i], float(vals1[i]), horizontalalignment='center', verticalalignment='bottom')
plt.title(label='Девочки')
plt.show()


dict = {}
for i in range(len(labels)):
    dict[labels[i]] = 'male'
for i in range(len(labels1)):
    if labels1[i] not in labels:
        dict[labels1[i]] = 'female'
    else:
        if vals1[i] > vals[labels.index(labels1[i])]:
            dict[labels1[i]] = 'female'


def app(word):
    if word[-1] in ['а', 'я', 'ь']:
        if dict[word[-2:]] == 'male':
            return print('Уважаемый ' + word)
        else:
            return print('Уважаемая ' + word)
    else:
        if dict[word[-1]] == 'male':
            return print('Уважаемый ' + word)
        else:
            return print('Уважаемая ' + word)

while True:
    app(input())
