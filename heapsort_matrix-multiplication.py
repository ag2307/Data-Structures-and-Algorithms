import math
import random
class Heap:
	array=[]
	length=0
	def maxHeapify(self,index):
		leftchild=2*index+1
		rightchild=2*index+2
		largest=index
		if(leftchild<self.length and self.array[index]<self.array[leftchild]):
			largest=leftchild
		if(rightchild<self.length and self.array[largest]<self.array[rightchild]):
			largest=rightchild
		if(largest!=index):
			self.array[largest],self.array[index]=self.array[index],self.array[largest]
			self.maxHeapify(largest)

	def buildHeap(self):
		self.length=len(self.array)
		for i in range(len(self.array)//2 -1,-1,-1):
			self.maxHeapify(i)

	def heapSort(self):
		for i in range(len(self.array)-1,0,-1):
			self.array[i],self.array[0]=self.array[0],self.array[i]
			self.length=self.length-1
			self.maxHeapify(0)
class Matrix:
	row=0
	column=0
	a=None
	def __init__(self,r,c):
		self.row=r
		self.column=c
		self.a=[[] for x in range(r)]

	def __add__(self,matrix):
		if(self.row!=matrix.row or self.column!=matrix.column):
			print("Wrong matrix dimensions.\n")
			return
		sum=Matrix(matrix.row,matrix.column)
		for i in range(0,matrix.row):
			for j in range(0,matrix.column):
				sum.a[i].append(matrix.a[i][j]+self.a[i][j])
		return (sum)

	def __mul__(self,matrix):
		if(self.column!=matrix.column):
			print("Wrong matrix dimensions.\n")
			return
		product=Matrix(self.row,matrix.column)
		for i in range(0,self.row):
			for j in range(0,matrix.column):
				intermediate=0
				for k in range(0,matrix.row):
					intermediate=intermediate+self.a[i][k]*matrix.a[k][j]
				product.a[i].append(intermediate)
		return(product)

	def input(self):
		for i in range(0,self.row):
			self.a[i]= list(map(int, input("Enter row number "+str(i+1)+" : ").split()))
	def printer(self):
		for i in range (0,self.row):
			print(self.a[i])

check=input("Type 'm' for matrix operations and 'h' for heap sort : ")
if(check=='m'):
	# tester for matrix class

	print("Matrix Operations\n")
	x,y=map(int,input("Dimensions of first matrix : ").split())
	matrix1=Matrix(x,y)
	x,y=map(int,input("Dimensions of second matrix : ").split())
	matrix2=Matrix(x,y)
	matrix1.input()
	matrix2.input()
	print("Addition\n")
	sum=matrix1+matrix2
	if(sum!=None):
		sum.printer()
	print("Multiplication\n")
	product=matrix1*matrix2
	if(product!=None):
		product.printer()	
else:			
	# tester for heap sort

	print("Heap Sort Program\n")

	object=Heap()
	count=100
	for i in range(0,count):
		object.array.append(random.randint(1,1000))
	object.buildHeap()
	object.heapSort()
	for i in range(0,count):
		print (object.array[i])
