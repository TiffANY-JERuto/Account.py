class Account:
	def __init__ (self,first_name,last_name,):
		self.first_name = first_name
		self.last_name = last_name
		self.balance = 0
		self.deposits= []
		self.withdrawals = []
		self.loan = 0

	def welcome(self):
		return "Hello {} {} your balance is {}".format(self.first_name,self.last_name, self.balance)

	def deposit(self,money_deposited):
		self.balance= self.balance + money_deposited
		self.deposits.append(money_deposited)        
		return "Hello {} {}, you have deposited {}".format(self.first_name, self.last_name, money_deposited)


	def withdraw(self,money_withdrawn):
		self.withdrawals.append(money_withdrawn)
		if money_withdrawn <= self.balance:
			self.balance = self.balance - money_withdrawn
			return "Hello {} {}, you have successfully withdrawn {}".format(self.first_name, self.last_name, money_withdrawn)
		else:
			return "Hello {} {}, your account balance is insufficient to withdraw {}".format(self.first_name, self.last_name, money_withdrawn)

	def show_balance(self):
		show_balance = self.balance
		return "Hello {} {}, your current account balance is {}, thank you for using our services.".format(self.first_name, self.last_name, self.balance)
    
	def show_deposits(self):
		for money_deposited in self.deposits:
			print(money_deposited)

	def show_withdrawals(self):
		for money_withdrawn in self.withdrawals:
			print(money_withdrawn)			
	
	def give_loan(self,amount):
		if len(self.deposits>= 5 and amount < (1/3)*(sum(self.deposists)) and self.loan==0:
			self.loan = self.loan + amount
			self.balance = self.balance + amount
			return "Hello {} {}, you have qualified for a loan of Ksh {}, your outstanding loan balance is {}".format(self_firstname,self.second_name,amount,self.balance)
		else:
			return "Hello {} {}, you do not qualify for this service, read the terms and conditions to qualify to get a loan".format(self.first_name,self.second_name)

	def repay_loan(self, amount):
		if self.loan==0:
			return "You do not have an outstanding loan, check our terms and conditions to borrow from our loan service"
		elif amount<self.loan:
			self.loan = self.loan-amount
			self.balance = self.balance - amount
			return "Hello {} {}, you have repaid {} from your loan, your ooutstanding balance is {}.".format(self.first_name,self.second_name,amount,self.balance)
		elif amount==self.loan:
			self.loan = self.loan - amount
			self.balance = self.balance - amount
			return "Hello {} {}, you have fully repaid your loan, your current balance is {}.".format(self.first_name, self.second_name, self.balance)
		elif amount< self.loan:
			excess= amount - self.loan
			self.balance = self.balance - amount
			self.balance = self.balance + excess
			self.loan = (self.loan + excess) amountreturn "Hello {} {}, you have sucessfully repaid your loan, your excess amount deposited is {}, your outstanding balance is {}".format (self.first_name, self.second_name,excess, self.balance)