from tkinter import *
import tkinter
 
Start = Tk()
Start.title("Enigma Machine")
Start.geometry("400x360+500+200")
Start.resizable(width=False, height=False)
 
def base():
    """Machine module opening a window with Tk inter to recreate the
    Enigma Machine which was used in WWII by the german army."""
    global PAD1,PAD2,PAD3,text,counter,ecounter,enclist
    Rotors = Frame(bg='dark grey')
    Rotors.pack(side=TOP)
 
    Keyrow1 = Frame(pady=5)
    Keyrow1.pack(side=TOP)
    Keyrow2 = Frame(pady=3)
    Keyrow2.pack(side=TOP)
    Keyrow3 = Frame()
    Keyrow3.pack(side=TOP)
    Keyrow4 = Frame(pady=10)
    Keyrow4.pack(side=TOP)
 
    NONEncryptF = Frame()
    NONEncryptF.pack(side=TOP)
    
    EncryptF = Frame()
    EncryptF.pack(side=TOP)
 
    
    NONEncryptM = "Inputted Text will be written here."
    NONEncryptT = StringVar()
    NONEncryptL = Label(NONEncryptF,width=50,height=4,textvariable=NONEncryptT,bg="black",fg="white")
    NONEncryptL.pack()
    NONEncryptT.set(str(NONEncryptM))
 
    
    EncryptM = "Encrypted Text will be written here."
    EncryptT = StringVar()
    EncryptL = Label(EncryptF,width=50,height=4,textvariable=EncryptT,bg="grey55",fg="black")
    EncryptL.pack()
    EncryptT.set(str(EncryptM))
 
    PAD1=1
    PAD2=1
    PAD3=1
 
    counter = 0
    ecounter = 0
 
    LR1 = ["q","w","e","r","t","z","u","i","o","p"]
    LR2 = ["a","s","d","f","g","h","j","k","l"]
    LR3 = ["y","x","c","v","b","n","m",".",]
    LR4 = ["space"]
 
    text=[]
    enclist = []
 
    def GUI():
        def ROTORMOVER():
            """for each pressed key, we will augment the counter,
            counter moves back to 0 if it reaches 26,
            moving the one to its right"""
            global PAD1,PAD2,PAD3,counter,ecounter
            if PAD3==26:
                PAD3=1
                if PAD2==26:
                    PAD2=1
                    if PAD1==26:
                        PAD1=1
                        PAD2=1
                        PAD3=1
                    else:
                        PAD1+=1
                else:
                    PAD2+=1
            else:
                PAD3+=1
            
            counter+=1
            ecounter+=1
            ROTOR3.set(str(PAD3))
            ROTOR2.set(str(PAD2))
            ROTOR1.set(str(PAD1))
 
        def printer(l):
            """this pastes the normal, inputted text in the Message"""
            global text,NONEncryptM,counter
            ROTORMOVER()
            text+=[l]
            if counter==40:         
                text.append("\n")
                counter=0
            NONEncryptM = "".join(text)
            NONEncryptT.set(str(NONEncryptM))
            
            encrypt()
 
        
        ROTOR1 = StringVar()
        ROTOR2 = StringVar()
        ROTOR3 = StringVar()
        LabelPad1 = Label(Rotors, textvariable = ROTOR1 , bg ="grey")
        ROTOR1.set(str(PAD1))
        LabelPad1.pack(padx=5,pady=10,side=LEFT)
        LabelPad2 = Label(Rotors,textvariable = ROTOR2, bg = "grey")
        ROTOR2.set(str(PAD2))
        LabelPad2.pack(padx=5,pady=10,side=LEFT)
        LabelPad3 = Label(Rotors, textvariable = ROTOR3 , bg ="grey")
        ROTOR3.set(str(PAD3))
        LabelPad3.pack(padx=5,pady=10)
 
        
        for char in LR1:
            Button(Keyrow1,text=char,width=3,pady=5,command=lambda q=char:printer(q)).pack(side=LEFT)
        for char in LR2:
            Button(Keyrow2,text=char,width=3,pady=5,command=lambda q=char:printer(q)).pack(side=LEFT)
        for char in LR3:
            Button(Keyrow3,text=char,width=3,pady=5,command=lambda q=char:printer(q)).pack(side=LEFT)
        Button(Keyrow4,text="Space",width=3,padx=85,pady=5,command=lambda:printer(" ")).pack()
    
    GUI()
 
    def encrypt():
        
        global EncryptM,text,PAD3,PAD2,PAD1,enclist,c,d,e,ENCMESS,x,ecounter,Rotor1,Rotor2,Rotor3,Mirror
        char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
        
        c = PAD3-2
        if c==-1:c=26
        d = PAD2-1
        e = PAD1-1
        ENCMESS=0
 
        
        Rotor1 = [7,13,1,23,6,17,14,10,26,2,5,19,12,18,21,3,25,9,15,24,4,11,20,8,22,16]
        Rotor2 = [19,17,6,3,25,16,7,11,23,4,1,20,9,5,26,22,14,2,18,10,24,15,8,12,21,13]
        Rotor3 = [24,13,9,21,10,5,17,2,12,25,4,11,15,18,7,20,1,14,23,6,16,19,22,3,26,8]
        Mirror = [21,7,17,18,11,3,1,23,15,12,8,25,13,16,9,22,2,26,20,14,6,19,24,4,10,5]
 
        def starter():
            """Converts our last character of the inputted text into a cipher"""
            global ENCMESS,c,text,x,Rotor1
            x = text[len(text)-1]
            for cha in char:
                ENCMESS+=1
                if x==cha: break
 
        def coder(seq,rev,m):
            """Acts as our rotors"""
            global ENCMESS
            if rev==0:ENCMESS+=m
            while ENCMESS>26:ENCMESS-=26
            ENCMESS = seq[ENCMESS-1]
 
        def letters():
            """Converts the ciher back to a letter"""
            global ENCMESS
            ENCMESS = char[ENCMESS-1]
 
        starter()
        coder(Rotor1,0,c)
        coder(Rotor2,0,d)
        coder(Rotor3,0,e)
        coder(Mirror,2,c)
        coder(Rotor3,1,e)
        coder(Rotor2,1,d)
        coder(Rotor1,1,c)
        
        for l in enclist:
            if ecounter==40:
                enclist.append("\n")
                ecounter=0
        
        if x==" ": enclist.append(" ")
        elif x==".":enclist.append(".")
        elif x=="\n":pass
        else:       
            letters()
            enclist.append(ENCMESS)
        EncryptM = "".join(enclist)
        EncryptT.set(str(EncryptM))
 
base()

Start.mainloop()
