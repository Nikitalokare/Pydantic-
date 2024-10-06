from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    First_name: str | None = None
    Last_name: str
    age: int = 20

s = Student(Last_name="Lokare")

print(s)