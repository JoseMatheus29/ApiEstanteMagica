from fastapi import FastAPI
from rotas import router
import uvicorn

app = FastAPI()

#Inclusão das rotas no app
app.include_router(router, prefix='')

#verificando se o arquivo main esta sendo executado
if __name__ == '__main__':
    #rodando a api utilizando uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)