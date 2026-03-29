# class animals:
#     def __init__(self):
#         self.name="buzo"

#     def speak(self):
#         print(f'{self.name} speaks') 

# # class dogs(animals):
# #     def speak(self):
# #         print(f'{self.name} barks')

# # buzo=dogs('buzo')  
# # buzo.speak()      
# # output buzo barks
# class dogs(animals):
#     def __init__(self,behaviour):
#         super().__init__()
#         self.behaviour=behaviour
#     def speak(self):
#         super().speak()
#         print(f'{self.name} barks and is {self.behaviour}')

# buzo=dogs('playful')
# buzo.speak()        

###  multiple inheritance
# class a:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f'{self.name} speaks')

# class b(a):
#     def work(self):
#         print(f'{self.name} works')


# class c(b)     :
#     def playing(self):
#         print(f'{self.name} is playing')

# dulli=c('dulli')
# dulli.speak()
# dulli.work()
# dulli.playing()        

####heirachyal inheritance
# class a:  
#     def __init__(self,name):
#         self.name=name

#     def greet(self):
#         print(f'{self.name} says hello from a') 
# class b(a):
#     def greet(self):
#         print(f'{self.name} says hello from b')
# class c(a):
#     def greet(self):
#         print(f'{self.name} says hello from c')

# dulli=b('dulli')
# dulli.greet()    
# bulli=c('bulli')
# bulli.greet()            

### diamond problem
class a:  
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f'{self.name} says hello from a') 
class b(a):
    def greet(self):
        print(f'{self.name} says hello from b')
        super().greet()
class c(a):
    def greet(self):
        print(f'{self.name} says hello from c')
        super().greet()
class d(b,c):
    def greet(self):
        print(f'{self.name} says hello from d')
        super().greet()
dulli=d('dulli')
dulli.greet()
