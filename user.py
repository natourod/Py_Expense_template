from PyInquirer import prompt
import sys
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    original = sys.stdout
    with open ('users.csv', 'a') as f:
        sys.stdout = f
        print(infos["name"])
        sys.stdout = original
    print("User Added !")
    return True