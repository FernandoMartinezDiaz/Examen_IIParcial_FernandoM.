#Fernando Adalid Martinez Diaz
# -programa : genisys Inc
# Empresa de servicio de estacionamiento
#clases a agregar : 
#numero de placa , marca, Modelo , tipo de vehi
#hora de ingreso, Estado

import datetime

class datos:
    """"
    Representa la indormacion de nuestra libreria permite almacenar 
    una nota o un dato para asi poder colocarle etiquetas o buscar un dato 
    en otro registro que necesitemos
    """

    def __init__(self , tags = "", dato):
        """
        inicializa una nota con el valor de nustro dato 
