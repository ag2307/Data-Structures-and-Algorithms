class Stack:
	def __init__(self):
		print("hello")
		self.data=[]
		self.count=-1

	def push(self,x):
		self.data.append(x)
		self.count=self.count+1

	def pop(self):
		self.count=self.count-1
		return self.data[self.count+1]

	def top(self):
		return self.data[self.count]

	def isEmpty(self):
		if(self.count==-1):
			return True
		else:
			return False

stack=Stack()
