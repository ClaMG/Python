class livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
    def detalhes(self):
        print("O livro", self.titulo, "foi publicado por", self.autor, "no ano", self.ano_publicado)
livros = livro(titulo= input("Qual o titulo do livro: "), autor=input("Qual o autor do livro: "), ano_publicado=int(input("Qual ano foi publicado: ")))
livros.detalhes()