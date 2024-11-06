class Playlist():
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []

    def inserir(self, m):
        self.__musicas.append(m)
    def listar(self):
        return f"As musicas presentes nessa Playlist são: {self.__musicas}"
    def __str__(self) -> str:
        
        pass
    

class Musica():
    def __init__(self, artista, titulo, album):
        self.__artista = artista
        self.__titulo = titulo
        self.__album = album
        return [self.__artista, self.__titulo, self.__album]
    # def nova_musica(self, artista, titulo, album):
    #     self.__artista = artista
    #     self.__titulo = titulo
    #     self.__album = album

    def __str__(self):
        return f"Artista: {self.__artista}  Título: {self.__titulo}  Album: {self.__album}"
    


novaplaylist = Playlist("Sade Songs","playlist teste" )
musica = Musica("Sade", "Smooth Operator", "Best of Sade")
novaplaylist.inserir(musica)
novaplaylist.listar()
