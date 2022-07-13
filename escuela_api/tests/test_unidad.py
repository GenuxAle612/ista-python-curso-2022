from escuela_api import api

def test_eliminar_estudiante():
    api.eliminar_estudiante('1234567892') == 'Estudiante eliminado'