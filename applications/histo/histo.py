with open('robin.txt') as h:
    words = h.read()

def histo(words):
    ignored_chars = ['"', ':', ';', ',', '.', '-', '+', '=' ,'/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    word_dict = {}

    for i in ignored_chars:
        words = words.replace(i, '')

    words = words.lower().split()

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

def sort(list):
    list.sort(key = lambda x: (-x[1], x[0]))
    return list

histo_dict = histo(words)


histo_list = []
for word in histo_dict.keys():
    histo_list.append((word, histo_dict[word]))

sorted_list = sort(histo_list)

sorted_histo_list = []
for tup in sorted_list:
    sorted_histo_list.append((tup[0], tup[1] * '#'))


print(sorted_histo_list) 
