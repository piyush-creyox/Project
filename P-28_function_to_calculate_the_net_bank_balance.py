''' Program 28: Write a Python function to calculate the net bank balance from an input 
string representing a transaction log string (same logic format as Program 10, but structured 
within a returning function).'''


def transection(logs):
    amount = int(input("Enter base amount :"))
    for log in range(0,len(logs),2):
        if logs[log] == 'D' or logs[log] == 'd':
            amount += int(logs[log+1])
        elif logs[log] == 'W' or logs[log] == 'w':
            amount -= int(logs[log+1])
        else:
            print("Invalid input")
    return amount
    
logs = input("Enter the transection logs :").split()
        
print(transection(logs))