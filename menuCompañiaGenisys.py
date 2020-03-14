# -*- coding: utf8 -*-
#Fernando Adalid Martinez Diaz
# -programa : genisys Inc
# Empresa de servicio de estacionamiento
#clases a agregar : 
#numero de placa , marca, Modelo , tipo de vehi
#hora de ingreso, Estado


import sys
import platform
from datosEmpresa from infromacionVehiculos
from datetime import datetime, timedelta

class menu:
    """
    En esta parte se mostrara las opciones a elegir 
    para obtener informacion sobre su vehiculo
    """

    def __init__(self):
        self.datosEmpresa = datosEmpresa()
        self.options = {"1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.exit}

    def display_caracteristicas_vehiculo(self)
        """Caracteristicas de el vehiculo"""
        print("""
        Caracteristicas 
        1. Numero De Placa del Vehiculo 
        2. Marca
        3. Modelo 
        4. Tipo de Vehiculo -Automovil o motocicleta 
        5. Hora de ingreso
        6. Estado 
        """
        )
    

    def ejecutar(self)
        """Metodo de entrada para la aplicacion"""
        while True:
            Self.display_menu()
            choise = imput("Elija una opcion: ")
            action = self.options.gets(choise)
        
        if  action:
            action()
        else:
            print("{0} error de seleccion intente con otro numero ")

    def mostrar_datos(self, datosEmpresa=None):
        """Despliega nuestros datos agreagados en la empresa"""
        if not datosEmpresa:
            datosEmpresa = self.infromacionVehiculos.datosEmpresa
    
        for target_list in expression_list:

    def tarifa_por_hora ()
    """
    definimos las tarifas establecidas en las horas

    >Automóvil: L 20.00 la primera hora o fraccción

    >Motocicleta: L 10.00 la primera hora o fracción

    """









            
