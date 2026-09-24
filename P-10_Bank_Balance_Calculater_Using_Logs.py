''' Write a Python program that computes a net bank balance based on a 
transaction log given as string input. D means Deposit and W means 
Withdrawal (e.g., "D 100 W 50 D 40").'''

logs1 = input("Enter your transaction logs(e.g., \"D 100 W 50 D 40 \"):").split()
balance = int(input("Enter your balance:"))

print(logs1)

for i in range(0,len(logs1),2):
    if logs1[i] == "D":
        balance += int(logs1[i+1])
    else:
        balance -= int(logs1[i+1])
        
print("Your net balance is:",balance)
    
    
