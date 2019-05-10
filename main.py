from stack import Stack 

print()

# Pushing and Popping Stack:
stack1 = Stack()
for iterator in range(10):
	stack1.push(iterator)
print('''The pop() function returns the top of stack element 
and removes it from the stack.''')
print("===================================================")
print("Stack1 =", stack1.getSize(), "elements before pop stack function.", sep = ' ')
while not stack1.isEmpty():
	print(stack1.pop(), end = ' ')
print()
print("Stack1 =", stack1.getSize(), "elements after pop stack function.", sep = ' ')
print()

# Pushing and Peeking Stack:
stack2 = Stack()
for iterator in range(10, 20):
	stack2.push(iterator)
print('''The peek() function returns the top of stack element 
without removing it from the stack.''')
print("====================================================")
print("Stack2 =", stack2.getSize(), "elements before peek stack function.", sep = ' ')
print("stack2.peek() =", stack2.peek())
print("Stack2 =", stack2.getSize(), "elements after peek stack function.", sep = ' ')
print()