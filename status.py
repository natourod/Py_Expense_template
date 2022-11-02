
def show_status():
    with open("users.csv", newline='') as f:
        data = [line.rstrip() for line in f]
    users = [[d,0] for d in data]
    expenses_f = open("expense_report.csv", "r")
    expenses = expenses_f.readlines()
    for e in expenses:
        expense = e.split(";")
        amount = int(expense[0])
        spender = expense[2]
        involved = expense[3:(len(expense)-1)]
        num_implied = len(involved) + 1
        debt = amount / num_implied
        for u in users:
            if u[0] in involved:
                u[1] += debt
            if u[0] == spender:
                u[1] = u[1] - amount + debt
        for u in users :
            for s in users :
                if u[1] == -1 * s and u[1] > 0 :
                    continue
                    
    return