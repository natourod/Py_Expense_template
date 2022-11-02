from PyInquirer import prompt, print_json
import sys
import csv
expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"confirm",
        "name":"default",
        "message": "Is everyone involved ? ",
        "default": True
    }
]

involved_questions = [
    {
        "type":"input",
        "name":"involved",
        "message":"Involved person (Tap Enter for no one)",
    }
]

def new_expense(*args):
    infos = prompt(expense_questions)
    with open("users.csv", newline='') as f:
        data = [line.rstrip() for line in f]
    
    if infos["spender"] not in data:
        print("Error: Spender is not in the user list")
        print("Here are the users : ")
        print(data)
        return False
    if not infos["amount"].isnumeric():
        print("Error: Amount should be numeric")
        return False
    involved_list = []
    if not infos["default"]:
        involved = prompt(involved_questions)
        while involved["involved"] != "":
            if involved["involved"] == infos["spender"]:
                print("Error: Spender is in the list by default")
                involved = prompt(involved_questions)
                continue
            elif involved["involved"] in involved_list:
                print("Error: User already involved")
                involved = prompt(involved_questions)
                continue
            elif involved["involved"] not in data:
                print("Error: Involved user is not in the user list")
                print("Here are the users : ")
                print(data)
                involved = prompt(involved_questions)
                continue
            involved_list.append(involved["involved"])
            involved = prompt(involved_questions)
    else:
        involved_list = data
        involved_list.remove(infos["spender"])
        
    original = sys.stdout
    with open ('expense_report.csv', 'a') as f:
        sys.stdout = f
        print(infos["amount"]+";" + infos["label"] + ";"+infos["spender"] + ";", end= '')
        print(*involved_list, sep=";")
        sys.stdout = original
        
    print("Expense Added !")
    return True


