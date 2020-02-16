from difflib import SequenceMatcher

#check similarity between words, don't worry bruv
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#inputs the ingredients and quantities from the users fridge
#the input is the return of the my_split
#this function returns a dictionary with the ingredients in the users fridge
def fridge(item_list):
    dict_of_items={}
    item=input('>')
    quant=int(input('>'))
    while item!='done':#delete done when done. Change to False.
        for i in item_list:
            if i==item:# tell person that we dont have the ingredient
                dict_of_items.update({item: quant})
            elif i!='done':
                for i in item_list:
                    if similar(i,item)>=0.75:
                        item=i
                        dict_of_items.update({item: quant})
        item = input('>')
        if item != 'done':
            quant = int(input('>'))
    return dict_of_items


# gets all the ingredients and puts them in a list by each word
def my_split(text):
    list_of_words=[]
    length=len(text)
    j=0
    word=0
    for i in range(0,length):
        if text[i]==' ':
            word=split_helper(text[j:i])
            list_of_words.append(word)
            j=i+1
    list_of_words.append(split_helper(text[j:]))
    return list_of_words

#this function just takes away the extra commas and periods, this doesn't matter tho
def split_helper(text):
    length = len(text)
    for i in range(0, length):
        if (text[i] == ',' or text[i] == '.')or(text[i] == '!' or text[i] == '?'):
            return text[0:i]
    return text

#Reads Unititled which is the data where all the ingredients are stored
f=open("Untitled.rtf", "r")
if f.mode=="r":
    contents = f.read()
#this is a testing print can delete print and use the rest
print(fridge(my_split(contents)))

