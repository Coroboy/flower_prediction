import os

from sqlalchemy import create_engine


def obtener_conexion():
    usuario = os.getenv("IRIS_DB_USER", "root")
    contrasena = os.getenv("IRIS_DB_PASSWORD", "Coroboy12")
    host = os.getenv("IRIS_DB_HOST", "localhost")
    puerto = os.getenv("IRIS_DB_PORT", "3306")
    base_de_datos = os.getenv("IRIS_DB_NAME", "iris_db")

    if not contrasena:
        raise RuntimeError(
            "Falta la variable de entorno IRIS_DB_PASSWORD. "
            "Configúrala antes de ejecutar el programa."
        )

    return create_engine(
        f"mysql+mysqlconnector://{usuario}:{contrasena}"
        f"@{host}:{puerto}/{base_de_datos}"
    )