class Animal(object):
    'a class that abstracts an animal'
    def __init__(self, s = 'default', l = 'default'):
        self.species = s
        self.language = l
        
    def setSpecies(self, name):
        'sets the species of the animal'
        self.species = name
        
    def setLanguage(self, lang):
        'sets the language of the animal'
        self.language = lang
        
    def speak(self):
        return 'I am a {} and I {}'.format(self.species, self.language)
    
    def __repr__(self):
        return "Animal('{}', '{}')".format(self.species, self.language)

    def __str__(self):
        return self.speak()

    def __add__(self, other):
        'create a hybrid animal'
        return Animal(self.species+"/"+other.species, self.language+"/"+other.language)

    def __mul__(self,copies):
        clones=[]
        for i in range(copies):
            clones.append(eval(repr(self)))
        return clones

class Bird(Animal):
    'a class that extends Animal for a bird'
    
    def fly(self, n):
        'returns a message about the height of flight'
        return 'I am flying {} feet!'.format(n)
    
    def __init__(self, lang = 'chirp'):
        Animal.__init__(self, 'bird', lang)

    def __repr__(self):
        return "Bird('{}')".format(self.language)

    def __str__(self):
        return Animal.speak(self)
        

class Zoo(object):
    def __init__(self, existing = []):
        self.animals=existing

    def addAnimal(self,animal):
        self.animals.append(animal)

    def speakAll(self):
        for animal in self.animals:
            print(animal.speak())

    def __getitem__(self,index):
        return self.animals[index]

    def __iter__(self):
        return iter(self.animals)
