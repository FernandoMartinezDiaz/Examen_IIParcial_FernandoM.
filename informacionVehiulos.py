# -*- coding: utf8 -*-
#Fernando Adalid Martinez Diaz
# -programa : genisys Inc
# Empresa de servicio de estacionamiento
#clases a agregar : 
#numero de placa , marca, Modelo , tipo de vehi
#hora de ingreso, Estado


class vehiculo;

    def __init__(self,placa,marca, modelo, tipo_de_vehiculo, hora_de_ingreso,estado):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo_de_vehiculo = tipo_de_vehiculo
        self.hora_de_ingreso = hora_de_ingreso
        self.estado = estado
    
    #Metodo de acceso a informacion usando un Get

    def getPlaca(self):
        return self.placa
    def getMarca(self)
        return self.marca
    def getmodelo(self):
        return self.modelo
    def getTipoDeVehiculo(self):
        return self.tipo_de_vehiculo
    def hora_de_ingreso(self):
        return self.hora_de_ingreso
    def estado():
        return self.estado

     def mostrarVehiculo(self)
        print("\nPlaca:" +self.getPlaca()+ "\nMarca:" + self.getMarca()+"\nModelo"+self.getmodelo())

    placa = raw_imput("Porfavor ingrese una placa: ")
    marca = raw_imput("porfavor ingrese una marca: ")
    modelo = raw_imput("Favor ingrese el modelo de su vehiculo: ")
    e = vehiculo(placa,marca,modelo)
    e.mostrarVehiculo


