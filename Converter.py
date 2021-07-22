''' Welcome to Converter. This module as at the time of development consists of three classes to make temperature, weight, and some currency conversion easy when coding in python. '''


#Temperature Converter.
class Convert_temperature():
    #initialize the attributes of the class.
    #set the initial value of the attributes to 0 so that you can instantiate an object of the class without passing any parameters.
    def __init__(self, celsius=0, fahrenheit=0, kelvin=0):
        #define the attributes.
        self.celsius = celsius
        self.fahrenheit = fahrenheit
        self.kelvin = kelvin
        
    #1a. defining its methods. Firstly, Celsius to Fahrenheit. 
    def celTofah(self, celsius):
        self.fahrenheit = (celsius * 1.8) + 32
        self.fahrenheit = round(self.fahrenheit, 3)
        print(self.fahrenheit,'°F')
    
    #1b. Fahrenheit to Celsius.
    def fahTocel(self, fahrenheit):
        self.celsius = (fahrenheit - 32) / 1.8
        self.celsius = round(self.celsius, 3)
        print(self.celsius,'°C')
    
    #2a. Celsius to Kelvin.
    def celTokel(self, celsius):
        self.kelvin = celsius + 273.15
        self.kelvin = round(self.kelvin, 3)
        print(self.kelvin,'°K')
    
    #2b. Kelvin to Celsius.
    def kelTocel(self, kelvin):
        self.celsius = kelvin - 273.15
        self.celsius = round(self.celsius, 3)
        print(self.celsius,'°C')
    
    #3a. Fahrenheit to Kelvin.
    def fahTokel(self, fahrenheit):
        self.kelvin = ((fahrenheit - 32) / 1.8) + 273.15
        self.kelvin = round(self.kelvin, 3)
        print(self.kelvin,'°K')
    
    #3b. Kelvin to Fahrenheit.
    def kelTofah(self, kelvin):
        self.fahrenheit = ((kelvin - 273.15) * 1.8) + 32
        self.fahrenheit = round(self.fahrenheit, 3)
        print(self.fahrenheit,'°F')
        

#Weight Converter.
class Convert_weight():
    def __init__(self, gram=0, kilogram=0, pounds=0):
        self.gram = gram
        self.kilogram = kilogram
        self.pounds = pounds
        
    def gramTokg(self, gram):
        self.kilogram = gram / 1000
        self.kilogram = round(self.kilogram, 3)
        return self.kilogram
    
    def kgTogram(self, kilogram):
        self.gram = kilogram * 1000
        self.gram = round(self.gram, 3)
        return self.gram
    
    def poundsTokg(self, pounds):
        self.kilogram = pounds * 0.45359
        self.kilogram = round(self.kilogram, 3)
        return self.kilogram
    
    def kgTopounds(self, kilogram):
        self.pounds = kilogram / 0.45359
        self.pounds = round(self.pounds, 3)
        return self.pounds
    
    def gramTopounds(self, gram):
        self.pounds = gram * 0.0022046
        self.pounds = round(self.pounds, 3)
        return self.pounds
    
    def poundsTogram(self, pounds):
        self.gram = pounds / 0.0022046
        self.gram = round(self.gram, 3)
        return self.gram
        
        
#Currency Converter.        
class Convert_currency():
    def __init__(self, naira=0, dollar=0, euro=0):
        self.naira = naira
        self.dollar = dollar
        self.euro = euro
        
    def nairaTodollar(self, naira):
        self.dollar = naira / 411.5
        self.dollar = round(self.dollar, 3)
        print ('$',self.dollar)
        
    def dollarTonaira(self, dollar):
        self.naira = dollar * 411.5
        self.naira = round(self.naira, 3)
        print ('ᵰ',self.naira)
        
    def nairaToeuro(self, naira):
        self.euro = naira / 484.08
        self.euro = round(self.euro, 3)
        print ('€',self.euro)
        
    def euroTonaira(self, euro):
        self.naira = euro * 484.08
        self.naira = round(self.naira, 3)
        print ('ᵰ',self.naira)
        
    def dollarToeuro(self, dollar):
        self.euro = dollar / 1.18
        self.euro = round(self.euro, 3)
        print ('€',self.euro)
        
    def euroTodollar(self, euro):
        self.dollar = euro * 1.18
        self.dollar = round(self.dollar, 3)
        print ('$',self.dollar)