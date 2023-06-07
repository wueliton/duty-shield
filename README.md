Nome do Projeto

Duty Shield



Descrição

O Sistema de Gestão de Usuários e Matrizes SoD é uma aplicação desenvolvida em Python com a biblioteca customtkinter,
responsável pela criação e gerenciamento de usuários, sistemas, perfis e matrizes de Segregation of Duties (SoD). Ele permite a criação e atribuição de usuários a sistemas e perfis, garantindo que não haja conflitos com outras matrizes SoD existentes. As informações de consulta ao banco de dados são obtidas a partir de um arquivo XLSX.



Recursos

    Criação e gerenciamento de usuários, sistemas e perfis.
    Criação e atribuição de usuários a sistemas e perfis.
    Verificação de conflitos entre as matrizes SoD existentes.



Instalação

    Clone o repositório em sua máquina local.
    Certifique-se de ter o Python [versão] instalado.
    Execute o comando pip install -r requirements.txt para instalar as dependências.
    Execute o comando python main.py para iniciar a aplicação.
    
    Caso tenha algum problema com as depêndencias execute o comando 
    pip install customtkinter pandas Pillow openpyxl
    



Contato

Para entrar em contato com a equipe de desenvolvimento, envie um e-mail para luisfelipebianchini@gmail.com ou paulo.wueliton@hotmail.com.



Agradecimentos

Gostaríamos de agradecer aos professores por trazer esse desafio como projeto:

    ANDRE LUIS AVELINO SOBRAL
    ROBERTO DIAS DA CRUZ MAIA



FAQ (Perguntas frequentes)

1. O que é uma matriz SoD?

Uma matriz SoD (Segregation of Duties) é uma estrutura que define as permissões de acesso a sistemas e perfis para usuários em uma organização. Ela garante que um usuário não tenha permissões conflitantes que possam permitir ações indevidas ou fraudulentas.

2. Como as informações do banco de dados são consultadas a partir de um arquivo XLSX?

O sistema lê as informações do banco de dados a partir de um arquivo XLSX usando a biblioteca pandas.
