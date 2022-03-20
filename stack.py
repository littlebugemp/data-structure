def create_stack():
    stack = []
    return stack
    
def push(stack, element):
    stack.append(element)
    return stack
    
def check_empty(stack):
    return len(stack) == 0
    
def pop(stack):
    if check_empty(stack):
        return "stack is empty"
    return stack.pop()


stack=create_stack()
print(stack)
print(push(stack,2))
print(push(stack,5))
print(pop(stack))
print(stack)
print(pop(stack))
print(stack)
print(check_empty(stack))

