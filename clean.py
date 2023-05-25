#function reader to read the file word5dict.txt
def reader(): 
    """
    function reader: reads the file word5Dict
    Parameters: None
    Return: string version of read file
    """
    opener=open("word5Dict.txt","r")
    reader=opener.read()
    opener.close()
    return reader

#function to sort the file and write it onto a file scrabble5.txt
def cleaner(file):
    """
    function cleaner: sorts the string in a organized way and
                      writes it onto a text file scrabble5.txt
    Parameters: file that is supposed to be organized
    Return: None
    """
    s=file.split("#")
    opener=open("scrabble5.txt","w")
    for x in s:
        opener.write(x+"\n")

#main function to run the program
def main():
    file=reader()
    cleaner(file)

main()