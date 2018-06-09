Queue = []
maxLength = 5
front = 0
back = -1

def isFull(Queue):
    if len(Queue) == maxLength:
        return True
    else:
        return False
