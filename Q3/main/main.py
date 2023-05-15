from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def read_root():
    '''
    Simple root functions
    '''
    return {
            "Author": "Tonson Praphabkul",
            "Id" : "st123010"
            }

@app.post("/string_converter")
async def string_converter(name:str):
    '''
    Function that accept string input and call string_converter app via http requests.
    It only call string_converter if the name is Tonson.
    '''

    if name == "Tonson":
        # We can used q3_app instead of actual ip address as we specify q3_app in docker-compose file.
        request_address = "http://q3_app:8080/convert_string?name=" + name
        request_results = requests.get(request_address)
        output = request_results.json()
    else:
        output = "This is not my name, my name is Tonson"

    return output  
