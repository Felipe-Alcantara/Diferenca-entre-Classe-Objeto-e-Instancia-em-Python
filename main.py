# Classe

# Objeto

# Instância

# Filme
# Séries
# Perfis de usuários

# Definindo a classe Filme
class Filme:
    # O método __init__ é um método especial que é chamado automaticamente quando um objeto da classe é criado.
    # Ele serve para inicializar (ou seja, atribuir valores iniciais) para os atributos de um objeto.
    def __init__(self, nome, genero, informacoes, tags):
        # Aqui estamos definindo quatro atributos para a classe Filme: nome, genero, informacoes e tags.
        # self é uma referência à instância atual da classe e é usado para acessar as variáveis ​​que pertencem à classe.
        self.nome = nome
        self.genero = genero
        self.informacoes = informacoes
        self.tags = tags

# Aqui estamos criando uma instância da classe Filme.
# Estamos chamando o método __init__ da classe Filme e passando os argumentos necessários.
filmeBom = Filme("Nome do Filme", "Gênero do Filme", "Informações sobre o Filme", ["tag1", "tag2"])

# Aqui temos uma string chamada texto.
texto = "Meu nome é Felipe"
# O método replace() é um método da classe string que substitui uma parte da string por outra.
# Neste caso, estamos substituindo "nome" por "apelido".
texto = texto.replace("nome", "apelido")