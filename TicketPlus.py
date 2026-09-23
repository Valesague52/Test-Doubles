from TestTicketService import InventarioStub
from Usuario import UsuarioDummy
from RepoFake import RepoFake
from EmailDummy import EmailDummy
from unittest.mock import Mock
from Inventario import InventarioSpy


inventario_spy = InventarioSpy()

class TicketService:
   def __init__(self, inventario, repositorio, email_service):
      self.inventario = inventario
      self.repositorio = repositorio
      self.email_service = email_service
 
   def comprar(self, usuario, cantidad):
      disponibles = self.inventario.consultar_disponibilidad()
      if disponibles < cantidad:
          return False
      self.repositorio.guardar(usuario, cantidad)
      self.email_service.enviar_confirmacion(usuario)
      return True


# service = TicketService(None, None, None)
# service = TicketService(inventarioStub(), None, None)
# service = TicketService(InventarioStub(), UsuarioDummy(), None)
#service = TicketService(InventarioStub(), RepoFake(), EmailDummy())
# service = TicketService(InventarioStub(), RepoFake(), email_mock)

email_mock = Mock()
service = TicketService(inventario_spy, RepoFake(), email_mock)

#resultado = service.comprar("Ana", 2)
resultado = service.comprar(UsuarioDummy(), 2)
print(inventario_spy.veces_consultado)
print(resultado)

email_mock.enviar_confirmacion.assert_called_once()

# Segunda compra
resultado = service.comprar(UsuarioDummy(), 1)
print(resultado)
print(inventario_spy.veces_consultado)

# Como ahora hay 2 llamadas al Mock, comprobamos el número de llamadas
assert email_mock.enviar_confirmacion.call_count == 2
