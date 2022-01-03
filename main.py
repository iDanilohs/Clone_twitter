from fastapi import FastAPI

app = FastAPI()

@app.get(path="/")
def home():

    """
    Home

    This function say the welcome to the users and is the first thing to see.

    parameters:This function don't have parameters

    return the string Twitter API working in the screen
    """

    return {"Twitter API": "Working"}