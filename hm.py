from playsound import playsound
import random


death=["\n\n\n\n\n\n","\n\n\n\n\n\n=========","\n|\n|\n|\n|\n|\n=========","\n|-----\n|\n|\n|\n|\n=========","\n|-----\n|\n|    O\n|\n|\n=========","\n|-----\n|\n|    O\n|   /|\ \n|\n=========","\n|-----\n|\n|    O\n|   /|\ \n|   / \ \n=========","\n|-----\n|    |\n|    O\n|   /|\ \n|   / \ \n========="]
data=""
choice=input("1.Animals 2.Fruits 3.Countries \n")
if (choice=="1"):
    data="C:\\Users\\DUMP3R\\Desktop\\Youtube\\Python\\hangman\\animal.txt"
    typp="ANIMAL"
elif (choice=="2"):
    data="C:\\Users\\DUMP3R\\Desktop\\Youtube\\Python\\hangman\\fruit.txt"
    typp="FRUIT"
elif (choice=="3"):
    data="C:\\Users\\DUMP3R\\Desktop\\Youtube\\Python\\hangman\\country.txt"
    typp="COUNTRY"
else: print("Choose 1 of 3")

if data!="":
    with open(data, 'r') as f:
        lines = f.readlines()
        keyword = random.choice(lines) if lines else None #chosen keyword
        keyword=keyword.replace("\n","")
        
        
        win=0
        missed=0
        counter=0
        i=0
        sword=""
        
        l=len(keyword)
        while(i<l-1):
            sword = sword+"-"
            i=i+1
        
        space=keyword.find(" ")
        space=space+1
        if (space>0):
            bsub=sword[:space-1]
            esub=sword[space:]
            sword=bsub+" "+esub
            l=l-1
        print(typp+" name from "+str(l)+" letters")
        print(sword)
        while (win==0) and (missed<7):
            j=0
            let=input("enter a letter: ")
            occ=keyword.upper().count(let.upper())
            if (occ==0):
                missed=missed+1
                print(sword)
                print(death[missed])
                

            elif(occ==1):
                index=keyword.upper().find(let.upper())
                bbsub=sword[:index]
                eesub=sword[index+1:]
                sword=bbsub+let+eesub
                print(sword)
                print(death[missed])
            else:
                index=0
                aux=keyword
                while(index>=0):
                    index=aux.upper().find(let.upper())
                    if(index>=0):
                        bbsub=sword[:index]
                        eesub=sword[index+1:]
                        sword=bbsub+let+eesub
                        b2sub=aux[:index]
                        e2sub=aux[index+1:]
                        aux=b2sub+"*"+e2sub
                print(sword)
                print(death[missed])
            
            print(sword.upper()==keyword.upper())
            if(sword.upper()==keyword.upper()):
                win=1            
    if (win==1):
        print("--\., YOU WIN ,./--")
        playsound("C:\\Users\\DUMP3R\\Desktop\\Youtube\\Python\\hangman\\win.mp3")
    else:
        print(":( YOU LOSE ):")
        print("the word is : "+ keyword)
        playsound("C:\\Users\\DUMP3R\\Desktop\\Youtube\\Python\\hangman\\hang.mp3")
