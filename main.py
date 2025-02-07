from fastapi import FastAPI


#we are creating the FAST API instance here
app = FastAPI()



# this code below is a decorator that tells FastAPI:
#
# This function (index) should handle HTTP GET requests.
# It should be mapped to the root URL (/) of the API.
#


@app.get('/')

def index():
    return {'data': {'Name': 'Akshay New'}}

@app.get('/about')
def about():
    return {'data': {'about page'}}


