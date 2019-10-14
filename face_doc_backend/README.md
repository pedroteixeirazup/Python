#Esse backend e apenas uma instância de um trabalho maior, o qual não pode ser publicado.
#zup-mechanical-turk
Projeto: ZUP Mechanincal Turk
Objetivo: Treinar um repositório de imagens para a abertura de contas em banco pela web.
Definição: Este projeto é um classificador de imagens, indenticando se há uma face e um documeto.
           Uma imagem só é aceita neste processo de seleção se ela tiver um rosto ou mais, que pode ser só o da pessoa, ou então o da pessoa e o presente no documento.
           Uma imagem é rejeitada se não possui nenhuma face, ou então não possui nenhum documento.
Tecnologias: Linguagem de programação Python e suas bibliotecas para o backend e scripts de detectção de faces e objeto.
             Backend criado em Flask para a integração dos serviços de detecção com o frontend.
             Junto com Tensorflow e OpenCV para que o treinamento das imagens fossem possíveis.
             Bibliotecas mais importantes: numpy, cv2, matplotlib, opencv_python, tensorflow, pickle, PIL, pandas, scikit-learn, jupyter, Flask
