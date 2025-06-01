
def add_person():
    name =input("Name: ")
    age = input("Age: ")
    email = input('Email: ')

    person = {"name" : name, "age" : age, "email" : email}
    return person


print("Hello,welcome to the contact managment system. ")
print()
people = []
while True:
    command = input("You can 'add' or 'delete'or 'search'or 'print'and 'q' for quit: ").lower()
    
    if command == "add":
        person  =  add_person()
        people.append(person)
        print(f"Person added: Name: {person['name']}, Age: {person['age']}, Email: {person['email']}") 
    elif command == "print":
        if people:
            print(f"The number of people in our database is: {len(people)}: ")
        

    elif command == 'delete':
        pass
    elif command == 'search':
        pass
    elif command == 'q':
        break
    else:
        print("Invalide command")



 
  