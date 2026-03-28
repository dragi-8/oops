class student:
    def __init__(self):
        print('student class is created')
        print(id(self))
        self.name='abd'
        self.id=11

    def study(self,work):
        print(f"{self.name } is working on a {work} project")  

abd=student()   
farid=student()       
abd.study('mushrooms')
print(id(abd))
print(id(farid))