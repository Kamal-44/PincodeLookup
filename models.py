from pydantic import BaseModel, field_validator
from pincode_db import pincode_db


class PincodeRequest(BaseModel):
    pincode:str
    @field_validator("pincode")
    @classmethod
    def pincode_validator(cls,value):
        if len(value)!=6 or not value.isdigit():
            raise ValueError("pincode is not of 6 digit")
        return value



class LookupResponse(BaseModel):
    pincode: int
    city: str
    state: str
    district: str

class BulkResponse(BaseModel):
    status:str="success"
    found:int
    not_found:int
    result:list
    missing:list

class BulkPincodeRequest(BaseModel):
    pincodes:list[str]
    @field_validator("pincodes")
    @classmethod
    def pincodes_validator(cls,values):
        if len(values) == 0:
            raise ValueError("at least one value should be sent")
        if len(values) > 20:
            raise ValueError("Maximum values can be 20")
        for value in values:
            if len(value)!=6 or not value.isdigit():
                raise ValueError("pincode is not of 6 digit")
        return values
