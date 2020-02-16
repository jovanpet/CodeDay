#reads the data and makes into a dictionary, easy to read
def data(contents):
    food=''
    ing=''
    diction={} #{}
    list=[]
    length = len(contents)
    j=0
    for i in range(0,length):
        if contents[i]==',':
            food=contents[j:i]
            break
    contents=contents[i+1:]
    length = len(contents)
    for i in range(0, length):
        if contents[i]==' ':
            ing=split_helper(contents[j:i])
            j=i+1
            list.append(ing)
    list.append(split_helper(contents[j:]))
    return food, list

#the function seperates the words between ':'
def split_helper(text):
    length = len(text)
    for i in range(0, length):
        if (text[i] == ':'):
            return (text[0:i],int(text[i+1:]))
    #return text

# don't know i did this but this acts like MAIN it reads data by lines
def first():
    list_of_foods={}
    with open("Recepies.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    for i in lines:
        x,y=data(i)
        list_of_foods.update({x:y})
    return list_of_foods



