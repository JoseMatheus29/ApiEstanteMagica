from pydantic import BaseModel
from typing import List, Optional
from funcoes import gerarCodigo


#Classe que tera como objetos os dados de cada livro
class Livro(BaseModel):
    titulo: str = ""
    autor: str = ""
    professor: str = ""
    _codigo: Optional[str] = gerarCodigo()

    

#Lista do tipo livro para armazenar os dados dos livros, textos e imagens simulando um BD 
banco: List[Livro] = []