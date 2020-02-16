from word_count import *


def make_dict(file_input):
    #napravi direktorijum od stringa/ ovo ce biti korisno za ubacivvanje recepata u stvar
    recepies={}
    lines= text_to_lines(file_input)
    for i in lines:
        parts_of_lines=my_split(i)
        recepies[parts_of_lines[0]]= set(parts_of_lines[1:]) #ovo cu da stavim da radi sa setovima da bi mogao da vidim
    return recepies

def search_similar_type(list,recepies): #ovi recepti drze teme i to ne hranu i kolicinu
    #ovo je aplikacija koji trazi najslicnije recepte 
    values_of_similarity= []
    foods=[]
    categories= set(my_split(list)) #this gives a set of things that guy inputs
    for j,i in recepies.items():
        intersection_of_sets=categories.intersection(i) #this sees what is the diffrence of two sets
        if len(intersection_of_sets)!=0:
            values_of_similarity.append(len(intersection_of_sets)/len(categories))
        else:
            values_of_similarity.append(0)
        foods.append(j)
    values_of_similarity, foods = zip(*sorted(zip(values_of_similarity, foods))) #ove se sortiraju imena recepata po tome koliko su slicni sa temama
    return values_of_similarity, foods  #returns tuple, x= possible, y= impossible

def search_similar_fridge(fridge, recepies): #unos je lsita sortiranih elemenata recepata po slicnosti po temi, fridge je directory, recepies isto
    values_of_similarity= []
    foods=[]
    for i,j in recepies.items(): #i je ime recepta, j je lista tupla namernica i njiovih kolicina
        k=0
        for n in j:
            x,y=n #x je jednako namernica, y je kolicina namernice
            if x in fridge and y<=fridge[x]:
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
    for i in len(values_of_similarity_fridge):
        if values_of_similarity_fridge[i]==1:
            precentage.append(values_of_similarity_type[i])
            can.append(foods_fridge[i])
        else:
            type_sililarity.append((values_of_similarity_type[i]+values_of_similarity_fridge)/2)
            cant.append(foods_fridge[i])
    precentage, can = zip(*sorted(zip(values_of_similarity, foods)))
    type_sililarity, cant = zip(*sorted(zip(values_of_similarity, foods)))
    
    return can, cant


emotion=open('Emotion.txt', 'r')
if emotion.mode=='r':
    content_emotion=emotion.read()

print(make_dict(content_emotion))


