import threading




class SingletonMeta(type):
    _instance = {}
    _lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]

class Singleton(metaclass=SingletonMeta):
    pass

a = Singleton()
b = Singleton()
c = Singleton()
d = Singleton()

print(a == b == c ==d)