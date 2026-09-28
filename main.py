from fastapi import FastAPI, requests

from models import LookupResponse, BulkResponse, BulkPincodeRequest
from pincode_db import pincode_db
from exceptions import PincodeNotFoundError, InvalidPincodeError,pincode_not_found_handler,invalid_pincode_handler

app=FastAPI(title="Pincode Lookup request", description="Sending a request for pincode lookup")
app.add_exception_handler(PincodeNotFoundError,pincode_not_found_handler)
app.add_exception_handler(InvalidPincodeError,invalid_pincode_handler)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Pincode lookup "
    }

@app.get("/about")
def root():
    return {
        "message": "Developed by Kamal Mittal "
    }


@app.get("/pincode/{code}",response_model=LookupResponse)
def get_pincode(code:str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPincodeError(code,"pincode is not in correct format")
    if code not in pincode_db:
        raise PincodeNotFoundError(code)
    return  pincode_db[code]


@app.post("/pincode/bulk",response_model=BulkResponse)
def get_pincode(request:BulkPincodeRequest):
    missed = []
    results = []
    for code in request.pincodes:
        if code not in pincode_db:
            results.append(code)
        else:
            missed.append(code)
    return BulkResponse(
        found=len(results),
        not_found=len(missed),
        result=results,
        missing=missed
    )