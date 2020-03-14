#Fernando Adalid Martinez Diaz
# -programa : genisys Inc
# Empresa de servicio de estacionamiento
#clases a agregar : 
#numero de placa , marca, Modelo , tipo de vehi
#hora de ingreso, Estado

#Biblioteca para obtener informacion de tiempos 
from datetime import datetime, timedelta

class tiempoEnEstacionamiento:
"""
Esta funcion podra simular el tiempo que un cliente puede estar 
en el estacionamiento y asi ser incremental para poder obtener el cobro de el cliente
"""
    from datetime import datetime, timedelta
    plus_five_hours = datetime.now() + timedelta(hours=5)

class ticket_vehiculo():

    def calculateCharges(hours):
        """
         Para poder simular el tiempo que un cliente puede estar en el estacionamiento puede utilizar un
         valor aleatorio (entre 1 y 5 horas por ejemplo). Con dicho valor aleatorio puede sumarse al valor de la
         fecha/hora actual utilizando 
        """
    charge = 0
    if hours <= 3:
        charge= 20
    if hours >3:
        charge = 20 + (5*(hours-3))
        if charge > 50:
            charge= 50
    return charge
suma_horas= (1+4+24)
suma_costo= (calculateCharges(1)+calculateCharges(4)+calculateCharges(24))
print ("El costo por estacionar 1 horas es  ", calculateCharges(1))
print ("El costo por estacionar 4 horas es  ", calculateCharges(4))
print ("El costo por estacionar 24 horas es  ", calculateCharges(24))
print("La suma total de horas es: " , suma_horas )
print("El total de cargo es: ", suma_costo)

class datos:
    """"
    Representa la indormacion de nuestra libreria permite almacenar 
    una nota o un dato para asi poder colocarle etiquetas o buscar un dato 
    en otro registro que necesitemos
    """

    def __init__(self , tags = "", datos):
        """
        inicializa una nota con el valor de nustro dato en esta logramos 
        comprobar nuestros datos 
        """


        from datetime import datetime, timedelta
        plus_five_hours = datetime.now() + timedelta(hours=5)

        self.datos = datos
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id


    def buscar(self,searchFilter):
        """
        En esta nuestra busqueda en el valor de nuestro filtro
        retorna True si es igual o falso , asi el estado de nustro
        vehiculo en este caso
        """

