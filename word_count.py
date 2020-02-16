
def text_to_lines(text):
    words=[]
    while text!="":
        try:
            a=text.index("\n")
            words.append(text[:a])
            text = text[a + 1:]
        except ValueError:
            words.append(text)
            text=""
    return words
    
def my_split2(text):
    words=[]
    while text!="":
        try:
            a=text.index(",")
            words.append(text[:a])
            text = text[a + 1:]
        except ValueError:
            words.append(text)
            text=""
    clean(words)
    return words

def clean(words):
    for i in range(len(words)):
        if words[i][-1]=="!" or  words[i][-1]=="." or words[i][-1]=="?" or words[i][-1]== ",":
            words[i]=words[i][:len(words[i])-1]

def count(words):
    my_dict={}
    for i in words:
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i]=1
    return my_dict



