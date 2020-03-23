class CheckingAccount:
    def __init__(self,first_name,last_name,account_name,account_number,address,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_name = account_name
        self.account_name = account_number
        self.address = address
        self._balance = float(balance)
        
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_account_number(self):
        return self.get_account_number
    
    def get_balance(self):
        return "$" + str(round(self._balance,2))

    # Remove money out of account 
    def withdrawal(self,credit):
        if credit == 0:
            return "${} amount was withdrawn. Your current balance is: ${} ".format(credit, self._balance)
        else:
            if self._balance - credit < 0:
                return "Insufficient funds. You attempted to withdraw ${}. You currently have ${} in your account.".format(credit,self._balance)
            else:
                self._balance = self._balance - credit
                return "You withdrew ${}. Your current balance: ${}".format(credit,self._balance)
    #Deposi money to account
            
    def deposit(self,debit):
        if debit == 0:
            return "${} amount was deposited. Your current balance is: ${}".format(debit, self._balance)
        else:
            return "You deposited ${} in your account. Your current balance: ${}.".format(debit, self._balance)
            

account_1 = CheckingAccount("Angelo", "Martinez", "checking", "4538457983", "2610 Philadelphia Pike, Claymont,DE", "50000")
account_2 = CheckingAccount("Brenda", "Weaver", "savings", "675352245", "456 South 7th, Reading,PA", "13000")

# Display what the current balance name
print("Your current balance is: {}".format(account_1.get_balance()))
print("Your current balance is: {}".format(account_2.get_balance()))

#Withdraw money to the account
print(account_2.withdrawal(100))

#Deposited money to account
print(account_1.deposit(5000))