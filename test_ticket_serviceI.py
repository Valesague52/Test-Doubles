from unittest.mock import Mock

from TicketPlus import TicketService
from Inventario import InventarioSpy
from RepoFake import RepoFake
from Usuario import UsuarioDummy


def test_flujo_completo_compra():

    inventario = InventarioSpy()

    repositorio = RepoFake()

    email = Mock()

    service = TicketService(
        inventario,
        repositorio,
        email
    )

    resultado = service.comprar(
        UsuarioDummy(),
        2
    )

    assert resultado is True

    assert inventario.veces_consultado == 1

    assert len(repositorio.compras) == 1

    email.enviar_confirmacion.assert_called_once()