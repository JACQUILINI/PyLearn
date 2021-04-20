

class budget:
    def __init__(category, amount):
        category.amount = amount
    
    def remainingbalance(category):
        balance = category.amount
        print('Your current balance is: $%d' %balance) 
        menu()

        
    def deposit(category):
        newdeposit = int (input('Enter the amount you want to deposit:\n$'))
        newbalance = newdeposit + category.amount
        category.amount = newbalance
        print('An amount of $%d was successfully deposited' % newdeposit)
        budget.remainingbalance(category)
        menu()
    
    def withdrawal (category):
        withamount = int(input('Enter the amount you want to withdraw: \n$'))
        if (withamount < category.amount ):
            newbalance = category.amount - withamount
            category.amount = newbalance
            print('A withdrawal of $%d was successful' % withamount)
            budget.remainingbalance(category)
        else:
            print('Insufficient balancefund your wallet or contact our customer care unit')
            menu()
        
        


    def fundtransfer(category):
    
       transferamount = int (input('Enter the amount you want to transfer'))
       if(transferamount  < category.amount):
           category.amount = category.amount - transferamount
       else: print('Insufficient balance')
       pass 
    #I'm stuck at how to deposit the deducted amount (transferamount) into the destination wallet
    #I wish there could be a way to see a how this can be fixed


def exit():
    print('Good bye Jaye')


    
def menu():
    selectoption = int (input('''Press 1 for Deposit              Press 2 for Withdrawal
            Press 3 for Balance Inquiry      Press 4 to exit \n'''))
    if (selectoption == 1):
        print('You selected the deposit option %d' %selectoption)
        print('Choose the wallet you\'ll like to deposit into')
        depositoption = int (input(''' 1 (Food Wallet)           2 (Clothing Wallet)
                                    3 (Entertainment Wallet    4 (Exit) \n'''))
        if(depositoption == 1):
            food.deposit()
        elif(depositoption == 2):
            clothing.deposit()
        elif(depositoption == 3):
            entertainment.deposit()
        elif(depositoption == 4):
            exit()
        else: 
            print('you selected an invalid option')
            menu()
        
    elif(selectoption == 2):
        print('You selected the Withdrawal option')
        print('Choose the wallet you\'ll like to withdraw from')
        withoption = int(input(''' 1 (Food Wallet)           2 (Clothing Wallet)
                                    3 (Entertainment Wallet    4 (Exit)\n '''))
        if(withoption == 1):
            food.withdrawal()
        elif(withoption == 2):
            clothing.withdrawal()
        elif(withoption == 3):
            entertainment.withdrawal()
        elif(withoption == 4):
            exit()
        else: 
            print('you selected an invalid option')
            menu()
    
    elif(selectoption == 3):
        print('You selected the balance inquiry option')
        print('Choose the wallet whose balance  you\'ll like to view')
        baloption = int(input(''' 1 (Food Wallet)           2 (Clothing Wallet)
                                    3 (Entertainment Wallet    4 (Exit) \n'''))
        if(baloption == 1):
            food.remainingbalance()
        elif(baloption == 2):
            clothing.remainingbalance()
        elif(baloption == 3):
            entertainment.remainingbalance()
        elif(baloption == 4):
            exit()
        else: 
            print('you selected an invalid option')
            menu()
    elif(selectoption == 4):
        exit()
    else: 
        print('You selected an invalid option')
        menu()
   
        

food = budget(50000)
clothing = budget(10000)
entertainment = budget(20000)

print('''                   Welcome Jaye             ''') #Jaye being a user
print('Please select the operation youll like to perform on your wallets')
menu()