from dataclasses import dataclass, field

print("Dataclass lib working")
'''
When you declare dataclass using decorator then its automatically creates methods like __init__,__repr__, __eq__, and __hash__ 
based on class attributes
__init__ :- used for initialized the instance
__repr__ :- this method used for string presentation of the object work s as a __str__ method
__eq__ :- used for comparing two instances
__hash__ :- 
'''

@dataclass
class EmpManagement():
    id:int
                                                                                                                                                                                                                                                           

emp = EmpManagement(
    '101', 'Priya', 'Mumbai', 22000
)
emp1 = EmpManagement(
    101, 'Priya', 'Mumbai', 22000
)

# Difference between normal class and dataclass
class EmpManage():
    def __init__(self, id, name, address, salary):
        self.id = id
        self.name = name
        self.address = address
        self.salary = salary

emp3 = EmpManage(
    101, 'Priya', 'Mumbai', 22000
)
emp4 = EmpManage(
    101, 'Priya', 'Mumbai', 22000
)


print("Dataclass equal:- ", emp == emp1)
print("Normalclass equal:- ", emp3 == emp4)

'''
Equality between two objects using == operator in python checks for the same memory location.
Since two objects take different memory locations on creation, the output for equality is False.
Equality between DataClass objects checks for the equality of data present in it. 
This accounts for True as output for equality check between two DataClass objects which contain same data.
'''

'''
post_init :- Modifyfying code without writing code in init method after creating object
'''
name = {"emp_name": "Nikita"}

@dataclass
class EmpManagement:
    id:int
    name:str = field(init=False)
    address:str
    salary:int = 10000

    def __post_init__(self):
        self.name = name['emp_name']

Post_eg = EmpManagement(
    101, 'Mumbai'
)
print(Post_eg)

'''
Type hint = yes
Data validation = no
serialization = no
Built in = yes
'''

'''
Type Hint = Type hints do not affect the runtime behavior of the code
but provide useful information for developers and tools.
type hints help you and others understand what kind of data is being used in your code
and catch errors related to incorrect types before they cause problems.
'''

'''
we can also declare init values using init=False
'''

'''
frozen=False (which is the default), you can modify the attributes of an instance of the data class after it has been created.
Data Classes with frozen=False: Also mutable, allowing attribute modifications.
Data Classes with frozen=True: Make instances immutable, preventing attribute modifications after creation.
In noraml classes in Python are mutable by default. 

'''
Post_eg.id=501
print(Post_eg)

# immutable normal class
#  __slots__ = ['_name', '_age']  # Restrict attributes to these names

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     def __setattr__(self, key, value):
#         if hasattr(self, key):
#             raise AttributeError(f"Cannot modify attribute '{key}'")
#         super().__setattr__(key, value)

'''
slot=Flase
fixed set of attributes and exclude the default __dict__ attribute. This feature is useful for improving performance and memory usage.
'''