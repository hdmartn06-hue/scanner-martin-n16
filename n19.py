import os
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Scanner Martin N19 Cloud")

@app.get("/")
def home():
    return {"status": "ONLINE", "nivel": "N19 CLOUD", "dono": "MARTIN"}

@app.get("/api/status")
def status():
    return {"api": "ONLINE", "n19": "CLOUD ONLINE"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"[N19] Iniciando CLOUD na porta {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)