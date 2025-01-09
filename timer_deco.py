import time


def Timer(func):

    def interne(self):
        start = time.time()
        func(self)
        end = time.time()
        print("La fonction a mis "+str(end - start)+"s pour s'éxecuter")

        
    return interne