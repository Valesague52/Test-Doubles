from unittest.mock import Mock

from TicketPlus import TicketService
from TestTicketService import InventarioStub
from RepoFake import RepoFake
from Usuario import UsuarioDummy


def test_compra_exitosa():

    email_mock = Mock()

    service = TicketService(
        InventarioStub(),
        RepoFake(),
        email_mock
    )

    resultado = service.comprar(
        UsuarioDummy(),
        2
    )

    assert resultado is True

    email_mock.enviar_confirmacion.assert_called_once()
