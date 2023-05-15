from fastapi import FastAPI
import base64

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

@app.get("/convert_string")
def convert_sring(name:str):
    '''
    This functions accept string and convert to base64 string.
    '''
    message_bytes = name.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    
    return base64_message