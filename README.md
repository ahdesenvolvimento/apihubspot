### Integração com Hubspot

#### Considerações

- Foi utilizado Django Restframework para desenvolver a api que se comunica com o frontend e a api do Hubspot.
- Frontend foi feito em React.
- Não foi implementado banco de dados na api que se comunica com o Hubspot.
- Apesar de conter somente duas telas, o layout esta responsivo.

### Funcionalidades criadas

- Cadastrar contato
- Listagem de contatos
- Atualizar contato
- Deletar contato

## Usando o sistema

- Para fazer uso das 4 funcionalidades, o usuário deve fazer o login na plataforma do Hubspot, a url http://localhost:3000/login irá conter o link para a autenticação na Hubspot
- Feito isso, o usuário deverá selecionar a conta e então será redirecionado para a url http://localhost/?code=CODIGO_USADO_PARA_OBTER_O_TOKEN_DE_ACESSO, ao ser redirecionado para esta url, o sistema de imediato ira gerar o token de acesso e o token de refresh.
- Apos esse passo, o usuário ficará livre para utilizar das 4 funcionalidades
- Caso o usuário tente enviar dados para a api sem está logado, os dados não irão salvar e uma mensagem será enviada ao usuário.

1. Cadastrar contato e Atualizar contato
- Ao preencher os dados e enviar, o sistema irá verificar se existe uma propriedade "weight" associada aos contatos, para o usuário logado, caso tenha ele ignora, caso não tenha ele cria essa propriedade, em seguida o sistema verifica se o e-mail fornecido já está cadastrado, caso seja true, é feito uma sobrescrita dos dados, caso false um novo contato é criado.
2. Listagem de contatos
- Ao clicar no botão de "Listar Contatos", no primeiro clique ele não irá exibir os dados, mas fechando e abrindo novamente é listado todos os contatos relacionados ao usuário logado, bem como suas propriedades (email, phone, date_of_birth e weight). OBS: POR SER FUNCIONALIDADE EXTRA, NÃO CONSEGUI IDENTIFICAR A TEMPO A CAUSA DO BUG.
3. Deletar contato
- Ao ser exibida a listagem de contatos, irá abrir um modal com uma tabela (responsiva) que irá conter os dados dos contatos e um botão de excluir, clicando no botão o contato será deletado e o modal será fechado. OBS: FUNCIONALIDADE EXTRA.
