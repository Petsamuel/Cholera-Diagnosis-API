from fastapi import FastAPI



app = FastAPI()
@app.get("/")
async def root():
    return {"name": "Cholora diagonsis", "versions":"1.0.0", "description":"api for cholera diagonosis in nigeria", "contact":{"name":"peter samuel 😎","email":"petsamuel4@gmail.com"}}
    
    
    
    
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,  reload=True)