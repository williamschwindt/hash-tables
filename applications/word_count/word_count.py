def word_count(s):
    ignored_chars = ['"', ':', ';', ',', '.', '-', '+', '=' ,'/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    word_dict = {}

    for i in ignored_chars:
        s = s.replace(i, '')
    
    word_list = s.lower().split()

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))