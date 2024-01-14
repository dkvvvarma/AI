import sys
class room:
    def __int__ (self):
        self.dirty = False
    def suck(self):
        self.dirty = False

def agentFunction(vaccumpos):
    if vaccumpos=="A" and A.dirty and B.dirty:
        A.suck()
        print("cleaned A")
        print("moving to B")
        vaccumpos == "B"
        B.suck()
        print("cleaned B")
        sys.exit()

    elif vaccumpos=="A" and A.dirty and not B.dirty:  
        A.suck()
        print("cleaned A")
        sys.exit()
    
    elif vaccumpos=="B" and A.dirty and B.dirty:
        B.suck()
        print("cleaned B")
        print("moving to A")
        vaccumpos == "A"
        A.suck()
        print("cleaned A")
        sys.exit()
    
    elif vaccumpos=="B" and not A.dirty and B.dirty:
        B.suck()
        print("cleaned B")
        sys.exit()
    
    elif not A.dirty and not B.dirty:
        print("Both rooms are already")
        sys.exit()

A = room()
B = room()

A.dirty = input("Is room A dirty? Enter True/False: ").lower()=="true"
B.dirty = input("Is room B dirty? Enter True/False: ").lower()=="true"
vaccumpos= input("Is vaccum cleaner present in room A or B :").upper()
print("vaccum cleaner present in room ",vaccumpos)

agentFunction(vaccumpos)