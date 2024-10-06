from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    First_name: str
    Last_name: str
    age: int = 20

s = Student(First_name="Nikita", Last_name="Lokare")

print(s.model_fields)