#no collaborators were used in this assignment.



def numVowelsInFile(fileName):
    """Reads content of fileName and prints a count of all vowels in content"""
    
    
    try:
        
        file = open(fileName,'r')
        content = file.read()
        file.close()
    
        voweldict = {'a':0,'e':0,'i':0,'o':0,'u':0}
        
        content = content.lower()
        
        for char in content:
            if char in voweldict:
                voweldict[char] += 1
                    
        for key in voweldict:
            print("{} found: {}".format(key,voweldict[key]))
            
    except FileNotFoundError:
        print("No file found with that name.")
        
    except IOError:
        print("No file found with that name.")
        



def mergeFiles(file1,file2,newFile):
    """Takes the content of file1 and file 2 and writes their content to newFile."""
    
    try:
        
        file = open(file1,'r')
        file1content = file.read()
        file.close()
        
        file = open(file2,'r')
        file2content = file.read()
        file.close()
        
        print(file1content)
        print(file2content)
        
        mergefile = open(newFile,'w')
        print(file1content,file = mergefile)
        print(file2content,file = mergefile)
        mergefile.close()
        
    except FileNotFoundError:
        print("One of the two files could not be found")
        
    except IOError:
        print("One of the two files could not be found")
        
        


numVowelsInFile('Sample1.txt')

mergeFiles('1.txt','2.txt','out.txt')