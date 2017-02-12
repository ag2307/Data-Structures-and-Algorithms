class LinkedList():
	def __init__(self):
		self.data=None
		self.pointer=None
class Queue():
	def __init__(self):
		self.number_of_elements=0
		self.head=None
		self.tail=None

	def enque(self,element):
		temp=LinkedList()
		temp.data=element
		if(self.number_of_elements==0):
			self.head=temp
			self.tail=temp
			self.number_of_elements+=1
		else:
			self.tail.pointer=temp
			self.tail=temp
			self.number_of_elements+=1

	def deque(self):
		if(self.number_of_elements<=0):
			raise ValueError("Queue is empty. !!")
			return
		element=self.head.data
		self.head=self.head.pointer
		self.number_of_elements-=1
		return element

	def isEmpty(self):
		if(self.number_of_elements<=0):
			return True
		else:
			return False

	def size(self):
		return self.number_of_elements

	def search(self,element):
		temp=self.head
		index=1
		while(not temp==None):
			if(temp.data==element):
				print("Element found at index: "+str(index))
				return
			else:
				temp=temp.pointer
				index+=1
		print("Element not found.!!")

	def printing(self):
		temp=self.head
		while(not temp==None):
			print(temp.data)
			temp=temp.pointer

# tester for queue class
queue=Queue()
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
queue.enque(6)
queue.enque(7)
print(queue.size())
queue.deque()
queue.deque()
print(queue.size())
print(queue.isEmpty())
queue.search(8)
queue.search(6)
queue.search(4)
queue.printing()