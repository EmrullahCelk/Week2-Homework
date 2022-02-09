import string

sentence = input("Please enter a sentence: ").lower()

sentence = [x for x in sentence if x not in string.punctuation and x != " "]
sentence.sort()
y = []
for x in sentence:
    y.append(sentence.count(x))
print(y)

dict1 = dict()
z = 0
for z in range(0, len(sentence)):
    dict1[sentence[z]] = y[z]

print(dict1.items())