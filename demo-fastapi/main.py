from pydantic import BaseModel
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', tags=['Home'])
def read_home() -> Response:
  return {'detail': 'Welcome to FastAPI Tutorial!'}

@app.get('/health', tags=['Health'])
async def health() -> Response:
  return {'healthy': True}
