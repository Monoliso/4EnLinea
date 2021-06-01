from src.PruebaPython import TableroVacio

def test_tablero_vacio_tiene_6_filas():
    tablero = TableroVacio()

    assert len(tablero) == 6