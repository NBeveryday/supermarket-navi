from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Supermarket Navi Backend is running"}