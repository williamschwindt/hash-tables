import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    words = words.split()
    

# TODO: analyze which words can follow other words
word_dict = {}
for word in words:
    word_dict[word] = []

for i in range(0, len(words) - 2):
    word_dict[words[i]].append(words[i+1])



# TODO: construct 5 random sentences
starting_words = []
for word in word_dict.keys():
    if word[len(word)-1] != '.' or word[len(word)-1] != '?' or word[len(word)-1] != '!' or word[len(word)-1] != '"':
        if word[0].isupper() or word[0] == '"':
            starting_words.append(word)
print(starting_words)

ending_words = []
for word in word_dict.keys():
    if word[len(word)-1] == '.' or word[len(word)-1] == '?' or word[len(word)-1] == '!':
        ending_words.append(word)

def generate_sentence(start):
    is_generating = True
    word = start
    print(word, end=" ")

    while is_generating == True:
        word = random.choice(word_dict[word])
        
        if word in ending_words:
            is_generating = False
            print(word)
        else:
            print(word, end=" ")

generate_sentence(random.choice(starting_words))
generate_sentence(random.choice(starting_words))
generate_sentence(random.choice(starting_words))
generate_sentence(random.choice(starting_words))
generate_sentence(random.choice(starting_words))

    
