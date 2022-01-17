from fastapi import APIRouter, File, Query
from modelos import Livro, banco


#criação do router para ultilizar nas rotas
router = APIRouter()

#Rota para cadastrar livros
@router.post('/cadastrar')
def cadastrar(livro:Livro):
    """
        Função para realizar cadastro de livros.
        Recebe como parametro um objeto da classe livro .
    """
    banco.append(livro)
    return f'Livro cadastrado com sucesso com codigo {livro._codigo} para busca'

#Rota para cadastrar imagens
@router.post("/cadastrarImagem")
def cadastrarImagem(imagem: list[bytes] = File(...)):
    """
        Função para realizar cadastro das imagens.
        Verifica se a quantidade de imagens esta coerente.
        Recebe como parametro as imagens em byte.
    """
    if len(imagem) == 6:
        return "Imagens cadastradas com Sucesso"
    if len(imagem) < 6:
        faltam = 6 - len(imagem) 
        return f"Imagens não cadastradas, faltam {faltam}"
    if len(imagem) > 6:
        sobram = len(imagem) - 6
        return f"Imagens não cadastradas, existem {sobram} a mais."

#Rota para cadastrar textos        
@router.post("/cadastrarTexto")
def cadastrarTexto(texto: list[str] = Query(...)):
    """
        Função para realizar cadastro dos textos.
        Verifica se a quantidade de textos esta coerente .
        Recebe como parametro os textos.
    """
    if len(texto) == 6:
        banco.append(texto)
        return "Os textos foram cadastrados com Sucesso"
    if len(texto) < 6:
        faltam = 6 - len(texto) 
        return f"Textos não cadastradas, faltam {faltam}"
    if len(texto) > 6:
        sobram = len(texto) - 6
        return f"Textos não cadastradas, existem {sobram} a mais."    

#Rota para Buscar livros
@router.get('/buscar/{codigolivro}')
def buscarLivro(codigolivro = str):
    """
        Função para buscar os livros.
        Recebe como parametro o codigo do livro
    """
    for livro in banco:
        if livro._codigo == codigolivro:
            return livro
        else:
            return f"Livro não encontrado."
#Rota para listar livros 
@router.get('/listar')
def listarLivros():
    """
        Função Para listar cada livro presente no banco. 
        Armazena os titulos em uma lista e retorna os mesmos
    """
    titulos = list()
    for livro in banco:
        titulos1 = livro.titulo
        titulos.append(titulos1)
    return titulos      