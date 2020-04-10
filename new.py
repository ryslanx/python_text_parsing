import string
file = open('mbox-short.txt')
letters_freq = dict()
for line in file:
        line = line.translate(str.maketrans('', '', string.punctuation + '1234567890'))
        line = line.lower()
        words = line.split()
        for word in words:
            for letter in word:
                letters_freq[letter] = letters_freq.get(letter, 0) + 1
new_list = sorted([(k, v) for k, v in letters_freq.items()])
for k, v in new_list:
    print(v, k)
print(len(letters_freq))





new_list = list()
#print(domains)
#print(week_days)
#print(emails)
#print(bigkey, bigvalue)


