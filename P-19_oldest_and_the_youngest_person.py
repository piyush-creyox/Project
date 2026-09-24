'''Program 19: Write a Python program that accepts the names and birthdates (YYYY-MM-DD) 
of 3 people, then identifies and prints the oldest and the youngest person among them.'''


persons = []

for i in range(3):
    name = input("Enter your name : ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD) : ")
    persons.append({"name":name,"birthdate":birthdate})
    
print("the oldest person is :",min(persons, key=lambda x: x['birthdate']))
print("the youngest person is :",max(persons, key=lambda x: x['birthdate']))