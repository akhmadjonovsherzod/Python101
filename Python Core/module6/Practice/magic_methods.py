# iterator pattern, finite iterator, context manager, and callable object

class Callable:
   def __call__(self, *args, **kwargs):
     print("__call__ method is called")

obj = Callable()
obj()

numbers = [2, 5, 7, 1, 0]
for num in numbers:
   print(num)


class Repeat:
    def __init__(self, msg):
        self.msg = msg

    def __iter__(self):
        return self

    def __next__(self):
        return self.msg

obj = Repeat("car")
for message in obj:
   print(message) #this goes infinite

obj = Repeat("car")
obj_iterator = obj.__iter__()
while True:
  message = obj_iterator.__next__()
  print(message) #this goes infinite


class FiniteRepeat:
    def __init__(self, msg, max_count):
        self.msg = msg
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        return self.msg

obj = FiniteRepeat("car", 5)
for message in obj:
   print(message)

obj = FiniteRepeat("car", 5)
obj_iterator = iter(obj)
while True:
  try:
    message = next(obj_iterator)
  except StopIteration:
    break
  print(message)

#they go finite


class ContextManager:
    def __init__(self):
        print('__init__ method called')

    def __enter__(self):
        print('__enter__ method called')
        return self

    def __exit__(self, exc_type,
                 exc_value, exc_traceback):
        print('__exit___ method called')


with ContextManager() as manager:
    print('inside with statement block')


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,
                         self.mode)
        return self.file

    def __exit__(self, exc_type,
                 exc_value, exc_traceback):
        self.file.close()


with FileManager('data.txt', 'w') as f:
    f.write("First Line\n")
    f.write("Second Line")