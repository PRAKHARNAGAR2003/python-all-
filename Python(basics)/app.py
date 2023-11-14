from class_and_objects import student
student1 = student("Prakhar Nagar",20,8.3,False)
student2 = student("rati dubey",20,8.0,True)

def on_honor_roll(self):
    if self.gpa >= 3.5:
        print("Honored Student")
    else:
        print("Not Honored Student")
    
print(student1.name)
print(student2.name)
print(on_honor_roll(student1))