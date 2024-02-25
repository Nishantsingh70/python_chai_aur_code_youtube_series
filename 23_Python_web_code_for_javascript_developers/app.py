## pip install uv
## pip install fastapi uvicorn

## pip install python-multipart => dealing with files.


from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()

@app.get('/')
def home():
    return {'data': 'welcome to home page.'}

@app.get('/contact')
def contact():
    return {'data': 'welcome to contact page.'}

@app.post('/upload')
def handleImage(files: list[UploadFile]):
    print(files)
    return {'status': 'got the file'}

uvicorn.run(app)

## for testing the API's we have to use App_URL/docs example: http://127.0.0.1:8000/docs