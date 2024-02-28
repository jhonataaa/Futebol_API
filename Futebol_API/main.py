from typing import Dict, List, Optional, Any
from fastapi import FastAPI, status, Depends
from time import sleep
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import HTTPException
from models import futebol, Futebol

app = FastAPI(
    title='API de Futebol',
    version='0.0.1',
    description='Uma API Fast'
)

def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)


@app.get('/futebol',
         description='Retorna todos os jogadores ou uma lista vazia.',
         summary='Retorna todos os jogadores',
         response_model=List[Futebol],
         response_description='jogadores encontrados com sucesso.')
async def get_futebol(db: Any = Depends(fake_db)):
    return futebol

@app.post('/futebol', status_code=status.HTTP_201_CREATED, response_model=Futebol)
async def post_futebol(futebol: Futebol):
    next_id: int = len(futebol) + 1
    futebol.id = next_id
    futebol.append(futebol)
    return futebol

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
