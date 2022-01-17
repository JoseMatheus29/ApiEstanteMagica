from fastapi import APIRouter
import controladores
#Criando router para receber as rotas 
router = APIRouter()

#Incluição das rotas no router e adicionando prefixo livros
router.include_router(controladores.router, prefix='/livros')
