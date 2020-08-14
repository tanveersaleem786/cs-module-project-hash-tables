def word_count(s):
    # Your code here
    d = {}
    ignor_characters = ['"', ':', ';', ',' , '.', '-', '+', '=',  '/',  '\\',  '|', '[', ']', '{',  '}',  '(',  ')',  '*', '^',  '&']
    word = ""
    # for char in s:
    for i in range(0, len(s)):
        if s[i].isspace() or i == len(s) - 1: 
            if i == len(s) - 1 and s[i] not in ignor_characters:
                word += s[i]
            if word.strip():
                word = word.lower()
                d[word] = 1 if d.get(word) is None else d[word] + 1
                word = ''
        else: 
            if s[i] not in ignor_characters:    
                word += s[i]
    return d

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))