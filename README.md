````
    #Comando para criar um ambiente virtual
    python3 -m venv .venv

    # comando para ativar o ambiente virtual
    .venv\scripts\activate
    
    # comando salvar as instalações das Libs
    .venv\scripts\pip3 freeze > requirements.txt

    # comando para instalar as Libs
    pip3 install requirements.txt

    # rodar os testes
    pytest .
    pytest -s -v
```