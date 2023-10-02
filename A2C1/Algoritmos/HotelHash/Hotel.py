from Cliente import Cliente
from Habitación import Habitacion



class Hotel:
    def __init__(self, num_habitaciones) -> None:
        self.__num_habitaciones = num_habitaciones
        self.__habitaciones = []
        self.clientes = []

    def __str__(self) -> str:
        pass

    def nuevo_cliente(self, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        self.agregar_cliente(cliente)

    
    def agregar_cliente(self, cliente)
        self.clientes.append(cliente)


    def nueva_habitacion(self, num_habitacion):
        habitacion = Habitacion(num_habitacion)
        self.agregar_habitacion(habitacion)

    
    def agregar_habitacion(self, habitacion)
        self.__habitaciones.append(habitacion)

    def reservar_habitacion(self, num_habitacion, dni_cliente, f_ini, f_fin):
        pass

    def get_reservas_de_cliente(self,dni):
        pass

    def get_habitacion_disponible(self, f_ini, f_fin):
        pass

    def cancelar_reserva(self, id_reserva):
        pass