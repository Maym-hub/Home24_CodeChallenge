import string

#create listToString
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  


choice='y'
while choice!='n':
    #create abc
    abc=list(string.ascii_lowercase)

    #Input
    stri=list(str.lower(input("Type in your pangram you want to check: ")))
    print()

    #check for matches
    len_abc=len(abc)
    len_stri=len(stri)

    for n in range(0,len_stri):
        i=0
        while i<len_abc:
            if stri[n] == abc[i]:
                #remove matching letters
                abc.remove(abc[i])
                len_abc=len_abc-1
            i=i+1
    #Check if all letter have matched/removed

    if len(abc)==0:
        print('It is a valid pangram')
    else:
        print('It is no valid pangram')
        print()
        print('the missing letters are: ')
        print(listToString(abc))
    print()
    print('Again?')
    choice=str(input('y for yes, n for no '))
    print()