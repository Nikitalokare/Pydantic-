from pydantic import BaseModel, field_validator, ValidationError
from pydantic_extra_types.phone_numbers import PhoneNumber

import phonenumbers

class ValidatePhoneNumbers(BaseModel):
    phone: PhoneNumber
    region: str

    @field_validator('phone')
    def validate_phone(cls, phone, values):
        region = values.get('region')
        if region:
            try:
                # Ensure region is in uppercase to match phonenumbers expectations
                num = phonenumbers.parse(phone, region.upper())
                if not phonenumbers.is_valid_number(num):
                    raise ValueError(f"Phone number '{phone}' is not valid for region '{region}'")
            except phonenumbers.NumberParseException:
                raise ValueError(f"Phone number '{phone}' is not properly formatted")
        return phone

try:
    ph = input("Enter phone number: ")
    rg = input("Enter Region Code: ")
    user = ValidatePhoneNumbers(phone=ph, region=rg)
    print(user)
except ValidationError as e:
    print(e)
