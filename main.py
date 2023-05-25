import random
import Wordle175

#main function to run the program
def main():
    Wordle=Wordle175.ScrabbleDict(5,"scrabble5.txt")
    
    target_n=[] #numbered list for target
    i=1 #variable used to number repeated letters
    atm=0 #number of attempts
    entered=[] #list of valid words entered
    letters=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    target=random.choice(Wordle.getWords(random.choice(letters))) #target word that has to be guessed
    for x in target:
        target_n.append(x.upper())   
    
    looper=1 #variable to control the loop
    Attempts={} #dictionary to store all attempts
    while looper<=6:
        word_n=[] #numbered list of guessed word
        Word=[] #list version of guessed word        
        word=input("Attempt "+str(looper)+": Please enter "+str(Wordle.getWordSize())+"-letter word:")
        word=str(word) #guessed word by player
        RED=[] #list to store RED letter
        GREEN=[] #list to store GREEN letter
        ORANGE=[] #list to store ORANGE letter        
        
        if len(word)>Wordle.getWordSize():
            print(word.upper()+" is too long")
        elif len(word)<Wordle.getWordSize():
            print(word.upper()+" is too short")
        elif word not in Wordle.getWords(word[0]):
            print(word.upper()+" is not a recognized word")
        elif word in entered:
            print(word.upper()+" was already entered")
        else: #statement is triggered when valid guess is entered
            entered.append(word)
            for x in word:
                word_n.append(x.upper())
                Word.append(x.upper())
            for z in [word_n,target_n]: #loop for form list version of guessed word and target to compare them 
                for x in reversed(range(len(z))):
                    i=1
                    temp=z.pop(x)
                    if temp in z:
                        z.insert(x,temp)
                        for y in range(len(z)):
                            if z[y]==temp:
                                z[y]=z[y]+str(i)
                                if z==word_n:
                                    Word[y]=z[y]
                                i+=1
                    else:
                        if len(temp)==1:
                            z.insert(x,temp+str(i))
                        else:
                            z.insert(x,temp)
        
            for x in range(len(word_n)):
                if word_n[x] not in target_n:
                    RED.append(Word[x])
                elif (word_n[x] in target_n) and (x!=target_n.index(word_n[x])):
                    ORANGE.append(Word[x])
                else:
                    GREEN.append(Word[x])
        
            for x in [RED,ORANGE,GREEN]:
                x.sort()
            
            Attempts[word.upper()]=GREEN,ORANGE,RED
            for key,value in Attempts.items():
                print(key,"Green="+str(value[0])+" - "+"Orange="+str(value[1])+" - "+"RED="+str(value[2]))
            atm=looper
            
            if len(GREEN)==Wordle.getWordSize():
                looper=7
            if looper==7:
                print("Found in",atm,"attempts. Well done. The word is "+target.upper())
            if looper==6:
                print("Sorry you lose. The Word is "+target.upper())
            looper+=1
        
    
main()