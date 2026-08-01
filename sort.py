
sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

length  = len(words)

print(" the sorted words are:")
for i in range(length):
    print(words[i])
