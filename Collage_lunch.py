from word_count import *
from  fridge import *
from readData import *

def make_dict(file_input):
    #napravi direktorijum od stringa/ ovo ce biti korisno za ubacivvanje recepata u stvar
    recepies={}
    lines= text_to_lines(file_input)
    for i in lines:
        parts_of_lines=my_split2(i)
        recepies[parts_of_lines[0]]= set(parts_of_lines[1:]) #ovo cu da stavim da radi sa setovima da bi mogao da vidim
    return recepies


def search_similar_type(list,recepies): #ovi recepti drze teme i to ne hranu i kolicinu
    #ovo je aplikacija koji trazi najslicnije recepte 
    values_of_similarity=[]
    foods=[]
    categories= set(list) #this gives a set of things that guy inputs
    for j,i in recepies.items():
        intersection_of_sets=categories.intersection(i) #this sees what is the diffrence of two sets
        if len(intersection_of_sets)!=0:
            values_of_similarity.append(len(intersection_of_sets)/len(categories))
        else:
            values_of_similarity.append(0)
        foods.append(j)
    return values_of_similarity, foods
    #returns tuple, x= possible, y= impossible



def search_similar_fridge(fridge, recepies): #unos je lsita sortiranih elemenata recepata po slicnosti po temi, fridge je directory, recepies isto
    
    values_of_similarity=[]
    foods=[]
    for i,j in recepies.items(): #i je ime recepta, j je lista tupla namernica i njiovih kolicina
        k=0
        for n in j:
            x,y = n #x je jednako namernica, y je kolicina namernice
            if x in fridge.keys() and y<=fridge[x]:
                k+=1
        values_of_similarity.append(k/len(j))
        foods.append(i)
    return values_of_similarity, foods


def devide_into_can_cant(tuple1, tuple2): #ova funkcija podeli u dva da li moze ili ne moze
    values_of_similarity_fridge, foods_fridge= tuple1 #ASSUMPTION : Moraju type i fridge da budu isto sortirani u fajlovima
    values_of_similarity_type, foods_type= tuple2

    precentage=[] #ovo je kolko sunneke neiste recepti isti
    type_sililarity=[] #ovo je da bi mogao lepo da sortiram ove sto imaju sve 
    can=[]
    cant=[]
    for i in range(len(values_of_similarity_fridge)):
        if values_of_similarity_fridge[i]==1:
            precentage.append(values_of_similarity_type[i])
            can.append(foods_fridge[i])
        else:
            type_sililarity.append((values_of_similarity_type[i]+values_of_similarity_fridge[i])/2)
            cant.append(foods_fridge[i])
    precentage, can = zip(*sorted(zip(precentage, can)))
    type_sililarity, cant = zip(*sorted(zip(type_sililarity, cant)))
    
    return can, cant



#dict_recepies=first() #Dictionary of all recepies and values as a list of tuples
#dict_fridge=fridge(my_split(contents_ingridiatns)) #Dictionary of all ingrediants in the firdge, keys= ingrediants, values= quontint

#type=open('Recepies_type.txt', 'r') #Jovan test file
#if type.mode=='r':
#    content_type=type.read()

#dict_type=make_dict(content_type)

#theam='breakfast,sweet,hot,fat,vegan'


#print(devide_into_can_cant(search_similar_fridge(dict_fridge,dict_recepies), search_similar_type(theam, dict_type)))
