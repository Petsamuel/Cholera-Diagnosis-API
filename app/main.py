import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import FastAPI
from app.routes import auth,user

app = FastAPI()
@app.get("/")
async def root():
    return {"name": "Cholora diagonsis", "versions":"1.0.0", "description":"api for cholera diagonosis in nigeria", "contact":{"name":"peter samuel 😎","email":"petsamuel4@gmail.com"}}
    
    
app.include_router(auth.router)    
app.include_router(user.router)    
    
    
if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("main:app", host="127.0.0.1", port=8000,  reload=True)