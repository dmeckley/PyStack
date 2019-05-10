class Stack(object):

	""" Constructs an empty stack: """
	def __init__(self):
		self.__elements = []
		# A list to store the elements in the stack.

	""" Stores an element at the top of the stack: """
	def push(self, value):
		self.__elements.append(value)
		# Adds the value to the last index location of stack.

	""" Returns True if the stack is empty: """
	def isEmpty(self):
		if(len(self.__elements) == 0):
			return(True)
			# Returns True for an empty stack.
		else:
			return(False)
			# Returns False for a non-empty stack.

	""" Returns the number of elements in the stack: """
	def getSize(self):
		return(len(self.__elements))
		# Returns the length of the stack elements.	

	""" Removes the element at the top of the stack and returns it: """
	def pop(self):
		if(self.isEmpty() == True):
			return(None)
			# Returns nothing if the stack is empty.
		else:
			return(self.__elements.pop())
			# Returns the last element(top of stack) from self.__elements list, 
			# removing it completely from the stack. 
			# self.__elements.pop(index) where index is -1 by default 
			# if no argument is provided. ''' 

	""" Returns the element at the top of the stack 
		without removing it from the stack: """
	def peek(self):
		if(self.isEmpty() == True):
			return(None)
			# Returns nothing if the stack is empty.
		else:
			return(self.__elements[-1])
			# Returns the last element(top of stack) from self.__elements list, 
			# without removing it from the stack. 
			# self.__elements[-1] refers to the last element of the stack  
			# using negative indexing. 


	