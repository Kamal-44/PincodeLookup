from fastapi.openapi.utils import status_code_ranges
from fastapi.responses import JSONResponse
from fastapi import Request


class PincodeNotFoundError(Exception):
    def __init__(self,pincode:str):
        self.pincode=pincode

class InvalidPincodeError(Exception):
    def __init__(self,pincode:str,reason:str="invalid pincode"):
        self.pincode=pincode
        self.reason=reason

# Class Handlers

async def pincode_not_found_handler(request:Request , exc:PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
    content={
        "error": "Pincode not present in database",
        "message": f'No location for pincode: {exc.pincode}',
        "pincode": exc.pincode
    }
    )

async def invalid_pincode_handler(request:Request , exc:InvalidPincodeError):
    return JSONResponse(
        status_code=400,
    content={
        "error": "Pincode is invalid",
        "message": f'Pincode format is not correct: {exc.pincode}',
        "pincode": exc.pincode
    }
    )