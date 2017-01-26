#!/usr/bin/python3
import sys
import random 
import math
import time
def insertion_sort(a):
	for i in range(1,len(a)):
		key=a[i]
		j=i-1
		while j>=0 and key<a[j]:
			a[j+1]=a[j]
			j-=1
		a[j+1]=key
def merge_sort(a,p,q):
	if(p<q):
		mid=(p+q)//2
		merge_sort(a,p,mid)
		merge_sort(a,mid+1,q)
		merge(a,p,mid,q)
def merge(a,p,mid,q):
	l=a[p:mid+1]
	s=a[mid+1:q+1]
	l.append(1000000)
	s.append(1000000)
	i=0
	j=0
	for k in range(p,q+1):
		if l[i]<s[j]:
			a[k]=l[i]
			i+=1
		else:
			a[k]=s[j]
			j+=1

def main():
	max=0
	max1=0
	for k in range(1,5000,100):
		for j in range(1,11):
			a=[]
			i=0
			while i<int(k):
				a.append(random.randint(1,10000))
				i+=1
#			start1=time.time()
#			insertion_sort(a)
#			end1=time.time()
#			if end1-start1>max:
#				max1=end1-start1	
			start=time.time()
			merge_sort(a,0,len(a)-1)
			end=time.time()
			if end-start>max:
				max=end-start
#		print (k,max1*1000)
		print (k,max)
if __name__=='__main__':
	main()
