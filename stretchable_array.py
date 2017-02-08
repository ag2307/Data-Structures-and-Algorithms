from ctypes import *
class StretchableArray:
	def __init__(self):
		self.max_cap=2
		self.cur_cap=0
		self.array=(c_int*2)()
	def __stretch(self):
		self.max_cap*=2
		temporary=(c_int*self.max_cap)()
		for i in range(self.cur_cap):
			temporary[i]=self.array[i]
		self.array=temporary
	def __shrink(self):
		self.max_cap//=2
		temporary=(c_int*self.max_cap)()
		for i in range(self.cur_cap):
			temporary[i]=self.array[i]
		self.array=temporary
	def insert(self,element):
		if(self.cur_cap==self.max_cap):
			self.__stretch()
		self.array[self.cur_cap]=element
		self.cur_cap+=1
	def delete(self):
		if(self.cur_cap==0):
			raise ValueError("Array is empty.")
		self.cur_cap-=1
		if(self.cur_cap==self.max_cap//4):
			self.__shrink()
	def printing(self):
		for i in range(self.cur_cap):
			print(self.array[i],end=" ")
		print()
my_array=StretchableArray()
my_array.insert(1)
my_array.insert(2)
my_array.insert(3)
my_array.insert(4)
my_array.insert(5)
my_array.insert(6)
my_array.insert(7)
my_array.printing()
my_array.delete()
my_array.delete()
my_array.delete()
my_array.printing()
