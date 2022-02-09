import string
#kümenin elemanları aynı olmadığı için girilen cümleleri kümeye ve küçük harfe çevrildi.

sentence = set(input("Enter first sentence please: ").lower())
sentence1 = set(input("Enter second sentence please: ").lower())

newList = ["".join(sorted(list(x for x in sentence.intersection(sentence1) if x not in string.punctuation)))] +\
  ["".join(sorted(list(y for y in sentence - sentence1 if y not in string.punctuation)))] +\
        ["".join(sorted(list(z for z in sentence1 - sentence if z not in string.punctuation)))]

#bu kümelerin elemanları içinde for döngüsü, if komutu ve string.punctuation kullanarak noktalama işaretleri atıldı
#  ve küme listeye çevrildi. Son olarak .join ile virgülle ayrılan kesişim ve küme farkları birleştirildi.
print(newList)