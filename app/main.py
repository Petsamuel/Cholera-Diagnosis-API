from fastapi import FastAPI



app = FastAPI()
@app.get("/")
async def root():
    return {"name": "Cholora diagonsis", "versions":"1.0.0", "description":"api for cholera diagonosis in nigeria", "contact":{"name":"peter samuel 😎","email":"petsamuel4@gmail.com"}}
    