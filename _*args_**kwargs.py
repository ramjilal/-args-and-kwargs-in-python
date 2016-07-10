#use of '*' with list .
def fun(a,b,c):
	print (a,b,c)

l = [1,2,3]
fun (*l)

#usr of '*args'
def fun2(*args):
	a,b,c = args
	print (a,b,c)

fun2(1,2,3)

#use of '*args' with tuple:
def fun3(*k):
	a,b,c = k
	print (a,b,c)
t = (1,2,3)
fun3(*t)

#use of '*args' and print element using 'for':
def fun4(*args):
	for arg in args:
		print (arg)

t = ('a','b','c')
fun4(*t)

#use of '**'

#_________ReMeMbEr__________for '*' we use list/tuple but for '**' we use 'dictionary'

def fun5(x,y,z):
	print (x,y,z)

d = {'x':1,'y':2,'z':3}
fun5(**d)


#use of "**kwargs"
def fun6(**kw):
	for key,value in kw.items():
		print (key,value)			

d = {'x':1,'y':2,'z':3}
fun6(**d)

