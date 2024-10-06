from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    First_name: str
    Last_name: str
    age: int

data ={
    "First_name": "Nikita",
    "Last_name": "Lokare",
    "age": 25
}

data_json = '''
{
    "First_name": "Nikita",
    "Last_name": "Lokare",
    "age": 25
}
'''

s = Student.model_validate_json(data)
print(s)