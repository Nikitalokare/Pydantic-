from pydantic  import BaseModel, EmailStr, field_validator
'''
Type hint = yes
Data validation = yes
serialization = yes
Built in = no
'''

'''
When working with APIs or other external systems,
Pydantic can validate the data before it’s used within your Django application. 
This is especially useful if you are using Django alongside modern frameworks
'''

print("Working pydantic model")
class Emp(BaseModel):
    id: int
    name: str
    address: str
    salary: int
    email: EmailStr

    @field_validator("salary")
    def validate_sal(cls, value):
        if value <= 10000:
            raise ValueError(f"Salary must be grater than 10000:- {value}")
        return value

emp1 = Emp(
    id=1, name="Nikita", address='Mumbai', salary='40000', email='nikita@gmail.com'
)
print(emp1)