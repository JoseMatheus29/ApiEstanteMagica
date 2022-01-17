<h1 align = "center">Readme</h1>
<h1 align = "center">Api Estante Magica</h1>
<p align = "center ">
    <a href="#Sobre">Sobre</a>
    <a href="#Descrição">Descrição</a>
    <a href="#Pré-requisitos">Pré-Requisitos</a>
    <a href="#Passo-Passo">Passo-Passo</a>
</p>

# Sobre
<p id = "Sobre">Proposta de projeto desafio do processo seletivo na empresa Estante Magica.Bem simples porem muito legal de ser desenvolvido, ultilizei o framework FastApi que até então nunca tinha ultilizado. Porem a semelhança do framework com o framework Flask e o fato do mesmo ser bem simples/autodidata e ter uma otima documentação ajudou muito para o desenvolvimento do projeto.Gostei muito de desenvolver o projeto e espero que vocês tambem gostem dele.</p>

# Descrição 
<p>Desenvolvido ultilizando o framework FastApi em linguagem python consiste em uma Api com 5 rotas, onde o usuario consegue cadastrar os dados de seu livro, os textos do livro, as ilustrações do livro, buscar um livro e listar todos os livros cadastrados.</p>

# Pré-requisitos 
<p>Para Rodar o projeto é necessario ter instalado em seu computador:</p>
    <ul>
        <li>Python instalado na sua maquina(O porjeto ultiliza versão 3.9.9)</li>
        <li><a href="https://pypi.org/project/pip/">Gerenciador de pacotes Pip</a></li>
        <li>Módulos Nativos:</li>
            <ul>
                <li>Módulo Random</li>
                <li>Módulo String</li>
                <li>Módulo typing</li>
            </ul>
        <li>Módulos Externos:</li>
            <ul>
                <li><a href="https://fastapi.tiangolo.com/pt/">Módulo FastAPI</a></li>
            </ul>
        <li>Uma IDE para executar o projeto</li>
            <ul>
                <li><a href="https://code.visualstudio.com/download">VsCode</a></li>
                <li><a href="https://www.jetbrains.com/pt-br/pycharm/download">Pycharm</a></li>
                <li>Ou qualquer outra </li>
            </ul>
        <li>Um navegador Web</li>
    </ul>

# Passo-Passo
<p>Para rodar o projeto é necessario:</p>
    <ul>
        <li>Basta abrir o projeto com seu ambiente de desenvolvimento e executar o arquivo main.py</li>
        <li>Acesse o Link http://127.0.0.1:8000/docs e então você irá acessar uma tela semelhante a tela abaixo</li>
        <h1>
            <img alt='Readme' src="./img/Documentação Api.png" >
        </h1>
        <li>Nesta tela podemos testar todas as rotas de nossa api, basta selecionar a rota e clicar em "Try it out", como mostrado abaixo</li>
        <h1>
            <img alt='Readme' src="./img/Utilizar Rota.png" >
        </h1>
        <li>E então basta preencher os dados ao lado direito do dicionario e clicar em executar</li>
        <h1>
            <img alt='Readme' src="./img/Preenceher dados Rotas.png" >
        </h1>
        <li>Logo abaixo surgirá a resposta do servidor, com codigo 200 de sucesso</li>
        <h1>
            <img alt='Readme' src="./img/Resposta Sucesso.png" >
        </h1>
        <li>Observe que no response body foi gerado um codigo que pode ser ultilizado para busca, basta copia-lo e cola-lo na rota /livros/buscar executando o mesmo passo a passo dado acima, mudando apenas o campo de preenchimento, onde você preencherá com codigo gerado na rota de cadastro. E então logo abaixo surgirá a resposta do servidor com o livro achado, com codigo 200 de sucesso</li>
        <li>Caso queira selecionar imagens o processo é parecido, selecione a rota /livros/cadastrarImagens e então basta repetir o passo a passo da rota cadastrar, mas não iremos digitar nada e sim adicionar um string item e nesse intem selecionar o arquivo que queremos enviar, faremos isso até ja temos colocado as 6 imagens e então executarmos e recebermos resposta de sucesso com o codigo 200</li>
        <li>Para cadastrar textos o processo é exatamente igual o das imagens, porem inves de selecionarmos arquivos vamos digitar nossos textos, até completar os 6 textos obrigatorios, quando poderemos executar e receberemos a resposta de sucesso com o codigo 200</li>
    </ul>





<p>Feito por José Matheus✌ <a href = "https://www.linkedin.com/feed/">Veja meu Linkedin</a></p>
