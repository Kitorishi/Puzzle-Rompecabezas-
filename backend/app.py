#Aqui se agregan lo de python 
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app =  FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Modelo de datos con tipado estricto 
class ConfiguracionJuego(BaseModel):
    n: int
@app.post("/api/iniciar")
def iniciar_Juego(config: ConfiguracionJuego):
    return {"mensaje": f"Juego iniciado con tabla de {config.n}x{config.n}", "matriz": []}

@app.get("/api/resolver")
def resolver_Juego():
    return {"pasos solucion": ["arriba", "izquierda", "derecha", "abajo"]}

#Clase que describe el movimiento
class MovimientoPieza(BaseModel):
    tablero_actual: list[list[int]] #enteros => elementos i de la matriz
    pieza_a_mover: int #el elemento i de la matriz
app.post("/api/mover")
def mover_pieza(movimiento: MovimientoPieza):
    #Logica: (tomada de anteriores programas)
    #Estan Juntos? Aqui es donde intercambian posiciones
    return #El nuevo tablero y un mensaje de si gano

#Clase Resolver Juego
