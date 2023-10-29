date = input("Enter today's date: ")
mood = input("What is your mood today from 1-10? ")
journal = input("Let your thougts flow:\n")

with open(f"journal/{date}.txt","w") as file:
    file.write(mood + " ")
    file.write(journal)