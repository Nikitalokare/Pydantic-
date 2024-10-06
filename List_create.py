from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    First_name: str
    Last_name: str
    age: int = 20
    numbers: list[int]

s = Student(First_name="Nikita", Last_name="Lokare", numbers=[1,2,'10'])

print(s)