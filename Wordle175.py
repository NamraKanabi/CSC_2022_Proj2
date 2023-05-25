#defining class ScrabbleDict
class ScrabbleDict:
    """
    class ScabbleDict: accepts a filename and performs several functions on it
                       Sorts the read file into a dictionary (with definitions if provided)
    Parameter: filename(str), size(int)
    Return: None
    """
    def __init__(self,size,filename): #accepts a filename and sorts that file into a dictionary
        self.size= size
        opener= open(filename,"r")
        reader= opener.read()
        opener.close()
        lister= reader.split("\n")
        self.dictn={}
        self.test=[]
        for x in lister:
            i=0
            temp=""
            temp2=""
            for y in x.split():
                if i==0 and len(y)==size:
                    temp=y
                    self.dictn[temp]=""
                if i!=0 and len(temp)==size:
                    temp2=temp2+y+" "
                    t=temp2.rstrip()
                    self.dictn[temp]=t
                i+=1
    
    #function check checks whether a word is in dictionary or not
    def check(self,word):
        """
        function check: checks whether a word is in dictionary or not
        Parameter: word(str)
        Return: True(if word in dictionary) or False(if word is not in dictionary)
        """
        if word in self.dictn.keys():
            return True
        else:
            return False
    
    #function getSize returns the size of the dictionary
    def getSize(self):
        """
        function getSize: checks the size of dictionary
        Parameter: None
        Return: size of dictionary(int)
        """
        return len(self.dictn)
    
    #function getWords returns a list words from dictionary with specified letter
    def getWords(self,letter):
        """
        function getWords: creats a list of words from dictionary with specified letter
        Parameter: letter(str)
        Return: words(list)
        """
        words=[]
        for x in self.dictn.keys():
            if x[0]==letter:
                words.append(x)
        words.sort()
        return words
    
    #function getWordSize returns size of the words in dictionary
    def getWordSize(self):
        """
        function getWordSize : returns size of the words in dictionary
        Parameter: None
        Return: size of words in dictionary (int)
        """
        return self.size
    
    #function getMaskedWords returns list of words according to the template entered
    def getMaskedWords(self,template):
        """
        function getMaskedWords: returns list of words according to the template entered
        Parameter: template(str)
        Return: MaskedWords(list)
        """
        temp_list=list(template)
        MaskedWords=[]
        for key in self.dictn.keys():
            checker=True
            for index in range(len(key)):
                if temp_list[index].isalpha():
                    if temp_list[index]!=key[index]:
                        checker=False
            if checker:
                MaskedWords.append(key)
        return MaskedWords
    
    #function getConstrainedWords returns list of words according to the template and letters
    def getConstrainedWords(self,template,letters):
        """
        function getConstrainedWords: returns list of words according to the template and letters
        Parameter: template(str) and letters(str)
        Return: ConstrainedWords(list)
        """
        temp_list=list(template)
        MaskedWords=[]
        ConstrainedWords=[]
        positions=[]
        for key in self.dictn.keys():
            checker=True
            for index in range(len(key)):
                if temp_list[index].isalpha():
                    if temp_list[index]!=key[index]:
                        checker=False
            if checker:
                MaskedWords.append(key)
        for x in range(len(temp_list)):
            if not temp_list[x].isalpha():
                positions.append(x)
        for word in MaskedWords:
            lister=[]
            checker=True
            for x in positions:
                lister.append(word[x])
            if all(x in lister for x in letters):
                ConstrainedWords.append(word)
        return ConstrainedWords

if __name__ == "__main__":
    test= ScrabbleDict(5,"scrabble5.txt") #defining object test to test out the class
    print(test.check("aahed")) #testing function check
    print(test.getSize()) #testing function getSize
    print(test.getWords("a")) #testing function getWords
    print(test.getWordSize()) #testing function getWordSize
    print("hints:",test.getMaskedWords("a*a*a")) #testing function getMaskedWords
    print("Constrained hints:",test.getConstrainedWords("a*a*a",["b","c"])) #testing function getConstrainedWords
