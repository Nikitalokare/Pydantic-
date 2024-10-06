from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    First_name: str
    Last_name: str
    age: int

# s = Student(First_name="Nikita", Last_name="Lokare", age=25)
# print(s)

# try:
#     Student(First_name="Nikita", Last_name="Lokare", age='25')
# except ValidationError as e:
#     print(e)

try:
    Student(First_name=25, Last_name="Lokare", age='nikita')
except ValidationError as e:
    exceptions = e
    print(exceptions.errors())