def no_dups(s):
    word_dict = {}
    word_list = s.split()

    for word in word_list:
        if word in word_dict:
            continue
        else:
            word_dict[word] = 1
    
    new_list = [x for x in word_dict]

    return ' '.join(new_list)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))