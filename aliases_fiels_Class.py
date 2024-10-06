from pydantic import BaseModel, ValidationError, Field

data ={
    "Firstname": "Nikita",
    "Lastname": "Lokare",
    "age": 25
}

class Student(BaseModel):
    First_name: str = Field(alias="Firstname")
    Last_name: str = Field(alias="Lastname")
    age: int = 20

s = Student(Firstname="Pooja", Lastname="hyfd")

print(s.model_validate(s))

# Serialization (Generate JSON )
print(s.model_dump())
print(s.model_dump_json())
print(s.model_dump(by_alias=True))
print(s.model_dump_json(by_alias=True))