from typing import Optional
from pydantic import BaseModel, validator

class Futebol(BaseModel):
    id: Optional[int] = None
    nome: str 
    time: str  
    posicao: str

    @validator('time')
    def validar_time(cls, value: str):
        # Validacao 1
        palavras = value.split(' ')
        if len(palavras) < 1:
            print("O time deve ter pelo menos 1 palavra.")
            #raise ValueError('O time deve ter pelo menos 1 palavra.')
        # Validacao 2
        if value.islower():
            print("O time deve ser capitalizado")
            #raise ValueError('O time deve ser capitalizado.')
        return value
futebol = [
    Futebol(id=1, nome='jhonata', time='são paulo', posicao='meia-ata'),
    Futebol(id=2, nome='bruno', time='palmeiras', posicao='zagueiro'),
]
