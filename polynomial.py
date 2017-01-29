import cmath
import math
import time
import random

# Basic Multiplication Method for O(n^2) complexity
def normal_multiplication(a,b):
	d=[]
	for i in range(0,len(a)):
		d.append(0)
	n=len(a)
	for k in range(0,n):
		for i in range(0,k+1):
			d[k]+=a[i]*b[k-i]
	return d		

# FFT-DFT for O(nlogn) complexity	
def fft(a,w_n):
	n=len(a)
	if(n==1):
		return a
	w=1
	first1=a[0::2]
	second1=a[1::2]
	first=fft(first1,w_n**2)
	second=fft(second1,w_n**2)
	y = [0] * n
	for k in range(0,n//2):
		y[k]=first[k]+w*second[k]				# Evaluating multiplication of 2 matrices
		y[k+n//2]=first[k]-w*second[k]			# One matrix is one form of Vandermonde Matrix
		w=w_n*w 								# Other matrix is either coefficient matrix or output matrix`
	return y

# Finding output matrix for final polynomial
def point_multiplication(a,b):
	c=[x*y for x,y in zip(a,b)]
	return c

a=[]
b=[]
n1=input("Degree of polynomial 1 : ")
n2=input("Degree of polynomial 2 : ")

# Taking Integer Inputs
for i in range(0,int(n1)+1):
	a.append(int(input("1st polynomial (Integer Input): ")))
for i in range(0,int(n2)+1):	
	b.append(int(input("2nd ploynomial (Integer Input): ")))

# Padding each of the polynomial with zero coefficients so that correct product polynomial can bbbe obtained
if(len(b)>=len(a)):
	k=len(b)
	for i in range(len(b),2**(int(math.ceil(math.log2(k)))+1)):
		b.append(0)
	for i in range(len(a),2**(int(math.ceil(math.log2(k)))+1)):
		a.append(0)
else:
	k=len(a)
	for i in range(len(a),2**(int(math.ceil(math.log2(k)))+1)):
		a.append(0)
	for i in range(len(b),2**(int(math.ceil(math.log2(k)))+1)):
		b.append(0)
print("\n")
print("Normal Multiplication\n")
print(normal_multiplication(a,b))
n=len(a)
w=cmath.exp(2*cmath.pi*1j/n)
w1=cmath.exp(-2*cmath.pi*1j/n)
y=fft(point_multiplication(fft(a,w),fft(b,w)),w1)
y1=[x/n for x in y]						# Final Product Polynomial but with very small imaginary part and floating point numbers
y1=[x.real for x in y1]					# Product Polynomial with imaginary part removed
y1=[math.floor(x+.5) for x in y1]		# Product Polynomial with floating point numbers rounded to nearest integers
print("Fast Fourier Transform Method")
print(y1)
