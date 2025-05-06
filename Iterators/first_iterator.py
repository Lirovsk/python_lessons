# Defining and using an interator in Python
class Iterator_Int:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
    
for i in Iterator_Int(1, 10):
    print(i)