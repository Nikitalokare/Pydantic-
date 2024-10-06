import json
from enum import Enum
from typing import Union
from typing_extensions import Annotated
from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class EMPBAR(BaseModel):
    count: int
    size: Union[float, None] = None

class EMP(str, Enum):
    id: int
    name: str
    address: str
    salary: int

class MainModel(BaseModel):
    model_config = ConfigDict(title='Main')

    foo_bar: EMPBAR
    gender: Annotated[Union[EMP, None], Field(alias='EMP')] = None
    snap: int = Field(
        42,
        title='The deatils of EMP',
        description='this is the value of EMP',
        gt=30,
        lt=50,
    )

main_model_schema = MainModel.model_json_schema()  # (1)!
print(json.dumps(main_model_schema, indent=2)) 