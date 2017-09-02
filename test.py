class Customer(Object):
	
	def __init__(self, name, balance = 0.0):
		'''Returns a customer object/instance with balance'''
		self.name = name
		self.balance = balance

	def withdraw(self, amount):
		'''Returns the amount remaining after withdrawal'''
		if amount > self.balance:
			raise RuntimeError('Amount is greater than your balance')
		else:
			self.balance -= amount
		return self.balance

	def deposit(self, amount):
		#return hands a value back to its caller
		self.balance += amount
		return self.balance
