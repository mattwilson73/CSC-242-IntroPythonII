
class Patient(object):
    'a Patient object'
    def __init__(self,name='', age=0, temp=98.6, heightInFeet=0, heightInInches=1, weight=1):
        'the constuctor'
        
        self.name = name
        self.age = age
        self.temp = temp
        self.heightInFeet = heightInFeet
        self.heightInInches = heightInInches
        self.weight = weight
        

    def getTemp(self):
        'get temp of patient'
        return self.temp

    def setTemp(self, temp):
        'set the temp of the patient'
        self.temp = temp

    def setHeight(self,heightInFeet, heightInInches):
        'set height in feet and inches. Each is an integer parameter'
        self.heightInFeet = heightInFeet
        self.heightInInches = heightInInches
        
    
    def getHeight(self):
        'returns a tuple of height in feet and height in inches'
        return (self.heightInFeet,self.heightInInches)
    
    def setAge(self,age):
        'set the age of patient'
        self.age = age

    def getAge(self):
        'get the age of the patient'
        return self.age
    
    
    def setWeight(self,weight):
        'set the weight of the patient'
        self.weight = weight

    def getWeight(self):
        'get the weight of the patient'
        return self.weight

    def getBMI(self):
        'get numeric bmi value as float'
        totalheight = (self.heightInFeet * 12) + self.heightInInches
        
        self.bmi = float((703 * self.weight) / (totalheight*totalheight))
        return self.bmi

    def getBMIDescription(self):
        'get text BMI description'
        if self.getBMI() < 18.5:
            return 'Underweight'
        
        if self.getBMI() >= 18.5 and self.getBMI() < 25:
            return 'Normal Weight'

        if self.getBMI() >= 25 and self.getBMI() < 30:
            return 'Overweight'
        
        if self.getBMI() >= 30:
            return 'Obese'
        
        
    def tempRange(self):
        'get an indication of a patients temp'
        if self.getTemp() < 97.7:
            return 'Low'
        
        if self.getTemp() >= 97.7 and self.getTemp() <= 99.5:
            return 'Normal'
        
        if self.getTemp() > 99.5:
            return 'High'
        
    def __str__(self):
        'string representation'
        return ('{} is {} years old. The patient is {} and their temp is {}'
                .format(self.name,self.getAge(),self.getBMIDescription(),self.tempRange()))
                

    def __repr__(self):
        'python representation'
        return "Patient('{}',{},{},{},{},{})".format(self.name,self.getAge(),self.getTemp(),
                        self.getHeight()[0],self.getHeight()[1],self.getWeight())
    
    
    
    
    
    
    
def processPatients(filename):
    'load patient info from a file'
    
    
     
    






class Doctor(object):
    'doctor type'
    def __init__(self,name='', hospital=''):
        pass

    def __str__(self):
        pass
    def __repr__(self):
        pass

#implement Specialist here

    
    
