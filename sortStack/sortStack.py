def sortStack(stack):
    if len(stack) == 0:
		return stack
	first = stack.pop()
	sortStack(stack)
	insertInSorted(stack, first)

	return stack
def insertInSorted(stack, val):
	if stack == [] or stack[-1] <= val:
		stack.append(val)
		return
	first = stack.pop()
	insertInSorted(stack, val)
	stack.append(first)
