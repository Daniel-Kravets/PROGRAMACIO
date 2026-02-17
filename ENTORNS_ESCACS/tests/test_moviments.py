import copy
import pytest

# IMPORTA TU FICHERO PRINCIPAL (ajusta el nombre si tu archivo no se llama JOC_ESCACS_ENTORNS.py)
import JOC_ESCACS_ENTORNS


def fresh_board():
    """
    Devuelve un tablero nuevo para cada test.
    """
    board = JOC_ESCACS_ENTORNS.crear_tauler()
    JOC_ESCACS_ENTORNS.tauler = copy.deepcopy(board)
    return JOC_ESCACS_ENTORNS.tauler


# =========================
#   TESTS DE PEÓ (6)
# =========================

def test_peo_blanc_un_pas_endavant_valid():
    """
    Peón blanco avanza 1 casilla a una posición vacía (válido).
    """
    fresh_board()
    # P de (7,1) -> (6,1)
    assert JOC_ESCACS_ENTORNS.peon("blanc", 6, 7, 1, 1) is True
    assert JOC_ESCACS_ENTORNS.tauler[6][1] == "P"
    assert JOC_ESCACS_ENTORNS.tauler[7][1] == "."

def test_peo_blanc_dos_pasos_desde_inicial_valid():
    """
    Peón blanco avanza 2 casillas desde posición inicial con camino libre (válido).
    """
    fresh_board()
    assert JOC_ESCACS_ENTORNS.peon("blanc", 5, 7, 1, 1) is True
    assert JOC_ESCACS_ENTORNS.tauler[5][1] == "P"
    assert JOC_ESCACS_ENTORNS.tauler[7][1] == "."

def test_peo_blanc_bloqueado_delante_invalido():
    """
    Peón blanco no puede avanzar si hay una pieza delante.
    """
    fresh_board()
    # Colocamos una pieza delante del peón
    JOC_ESCACS_ENTORNS.tauler[6][1] = "p"
    assert JOC_ESCACS_ENTORNS.peon("blanc", 6, 7, 1, 1) is False

def test_peo_blanc_captura_diagonal_valida():
    """
    Peón blanco captura en diagonal una pieza negra (válido).
    """
    fresh_board()
    # Ponemos una pieza negra en diagonal
    JOC_ESCACS_ENTORNS.tauler[6][2] = "p"
    assert JOC_ESCACS_ENTORNS.peon("blanc", 6, 7, 2, 1) is True
    assert JOC_ESCACS_ENTORNS.tauler[6][2] == "P"
    assert JOC_ESCACS_ENTORNS.tauler[7][1] == "."

def test_peo_blanc_captura_sin_pieza_invalida():
    """
    Peón blanco intenta capturar en diagonal sin pieza rival (inválido).
    """
    fresh_board()
    assert JOC_ESCACS_ENTORNS.peon("blanc", 6, 7, 2, 1) is False

def test_peo_blanc_mover_atras_invalido():
    """
    Peón blanco intenta mover hacia atrás (inválido).
    """
    fresh_board()
    assert JOC_ESCACS_ENTORNS.peon("blanc", 8, 7, 1, 1) is False


# =========================
#   TESTS DE CAVALL (6)
# =========================

def test_cavall_blanc_moviment_L_buit_valid():
    """
    Caballo blanco se mueve en L a una casilla vacía (válido).
    """
    fresh_board()
    # C de (8,2) -> (6,1)
    assert JOC_ESCACS_ENTORNS.cavall("blanc", 6, 8, 1, 2) is True
    assert JOC_ESCACS_ENTORNS.tauler[6][1] == "C"
    assert JOC_ESCACS_ENTORNS.tauler[8][2] == "."

def test_cavall_blanc_captura_rival_valida():
    """
    Caballo blanco captura una pieza negra en movimiento en L (válido).
    """
    fresh_board()
    JOC_ESCACS_ENTORNS.tauler[6][1] = "p"
    assert JOC_ESCACS_ENTORNS.cavall("blanc", 6, 8, 1, 2) is True
    assert JOC_ESCACS_ENTORNS.tauler[6][1] == "C"
    assert JOC_ESCACS_ENTORNS.tauler[8][2] == "."

def test_cavall_moviment_no_L_invalido():
    """
    Caballo intenta moverse como torre o alfil (inválido).
    """
    fresh_board()
    assert JOC_ESCACS_ENTORNS.cavall("blanc", 8, 8, 3, 2) is False

def test_cavall_sortir_tauler_invalido():
    """
    Caballo intenta salir del tablero (inválido).
    """
    fresh_board()
    assert JOC_ESCACS_ENTORNS.cavall("blanc", 10, 8, 3, 2) is False

def test_cavall_capturar_propia_peza_invalido():
    """
    Caballo intenta capturar una pieza del mismo color (inválido).
    """
    fresh_board()
    JOC_ESCACS_ENTORNS.tauler[6][1] = "P"  # pieza blanca
    assert JOC_ESCACS_ENTORNS.cavall("blanc", 6, 8, 1, 2) is False

def test_cavall_salta_peces_valid():
    """
    El caballo puede saltar piezas: la presencia de obstáculos no afecta.
    """
    fresh_board()
    # Ponemos piezas bloqueando el camino (da igual para el caballo)
    JOC_ESCACS_ENTORNS.tauler[7][2] = "p"
    JOC_ESCACS_ENTORNS.tauler[7][1] = "p"
    assert JOC_ESCACS_ENTORNS.cavall("blanc", 6, 8, 1, 2) is True
