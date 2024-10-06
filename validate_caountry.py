from pydantic import BaseModel
from pydantic_extra_types.country import CountryAlpha2

class CountryModel(BaseModel):
    country_code: CountryAlpha2

try:
    country = str(input("Enter Country code:- "))
    validated_country_code = CountryModel(country_code=country)
    print(validated_country_code)
except ValueError as e:
    print(e)