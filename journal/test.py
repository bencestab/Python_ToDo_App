print("-------------------------------------------------------")
print("-------------------------------------------------------")

""" filenames = ['document', 'report', 'presentation']

for i,n in enumerate(filenames):
    print(f"{i}-{n.capitalize()}.txt")

 """



""" sss="valamike"
if len(sss) > 4:
    print("joo")
else:
    print("fdsa")
 """



""" waiting_list = ["john", "marry"]
 
print(waiting_list.index("marry")) """



""" def func():
    message = "hi"
    new_message = message.capitalize()
    print("hello")
    return (new_message)

greet = func()
print(greet) """



def check_password_strength(password):
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        return "Strong Password"
    else:
        return "Weak Password"

print(check_password_strength("ASDF1111111"))


