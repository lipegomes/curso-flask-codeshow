# curso-flask-codeshow

[![codecov](https://codecov.io/gh/lipegomes/curso-flask-codeshow/branch/main/graph/badge.svg?token=DJ04VUD1GV)](https://codecov.io/gh/lipegomes/curso-flask-codeshow)
[![Updates](https://pyup.io/repos/github/lipegomes/curso-flask-codeshow/shield.svg)](https://pyup.io/repos/github/lipegomes/curso-flask-codeshow/)
[![Python 3](https://pyup.io/repos/github/lipegomes/curso-flask-codeshow/python-3-shield.svg)](https://pyup.io/repos/github/lipegomes/curso-flask-codeshow/)

Código desenvolvido durante o curso de desenvolvimento web com o webframework [Flask](https://flask.palletsprojects.com/en/1.1.x/) para [Python](https://www.python.org/) do [CodeShow](https://www.youtube.com/user/brunovegan).

Link para o curso:

https://www.notion.so/Curso-de-Desenvolvimento-Web-0bf89f9f0dfa4ecead03a237360e5af1

## Requerimentos:
- Ter a versão 3.xx do python instalada no notebook ou pc.
- instalar o virtualenv para criar um ambiente virtual
    ```console
    pip install virtualenv
    ```
- Criar o ambiente virtual na pasta do projeto e instalar os requirements:
  
  Criar o .venv, ativar o shell do ambiente virtual:
    ```console
    virtualenv .venv
    source .venv/bin/activate
    ```

    Instalar as dependências:
    ```console
    pip install -r requeriments.txt
    pip install -r requeriments-dev.txt
    ```

## Para rodar a aplicação é necessário exportar as variáveis do flask para setar como deselvolvimento, depois usar o comando flask run:

Linux e Mac:
```sh
export FLASK_APP=delivery/app.py
export FLASK_ENV=development
flask run
```

Windows:
```sh
set FLASK_APP=delivery/app.py
set FLASK_ENV=development
flask run
```

## Realizar testes:

```sh
pytest tests/ -v --cov=delivery
```

## Ferramentas utilizadas:

Ambiente virtual:
1. [VirtualEnv](https://virtualenv.pypa.io/en/latest/)

Framework:
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)

Testes e qualidade do código:
1. [isort](https://pycqa.github.io/isort/)
2. [black](https://black.readthedocs.io/en/stable/)
3. [flake8](https://flake8.pycqa.org/en/latest/)
4. [flask-debugtoolbar](https://flask-debugtoolbar.readthedocs.io/en/latest/)
5. [flask-shell-ipython](https://pypi.org/project/flask-shell-ipython/)
6. [pytest](https://docs.pytest.org/en/stable/index.html)
7. [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/)
8. [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/index.html)

Deploy:
1. [git](https://git-scm.com/)
2. [pythonanywhere](https://www.pythonanywhere.com)
3. [GithubActions](https://github.com/features/actions)

Cobertura de testes:
1. [Codecov](https://app.codecov.io/)

Gestão da atualização de dependências:

1. [PyUp](https://pyup.io)

## Licença

Este projeto é licenciado sobre a licença MIT - veja [LICENSE](https://github.com/lipegomes/curso-flask-codeshow/blob/main/LICENSE) para mais informações.

## Acknowledgments

- CodeShow [Youtube](https://www.youtube.com/user/brunovegan)