class RepoFake:
    def __init__(self):
        self.compras = []
    def guardar(self, usuario, cantidad):
        self.compras.append({
            'usuario': usuario,
            'çantidad': cantidad 
        })  

repositorio = RepoFake()
repositorio.guardar('Ana', 2)
repositorio.guardar('Pedro', 5)
print(repositorio.compras)

