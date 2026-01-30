from fastapi import FastAPI

app = FastAPI()

@app.get('/ex001.py')
def home():
    return {'mensagem': 'api rodando'}