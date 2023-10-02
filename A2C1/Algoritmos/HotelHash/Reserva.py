# -*- coding: utf-8 -*-

class Habitacion:
    def __init__(self, habitacion, cliente, f_inicio, f_fin):
        self.id = f"{habitacion.get_id()} : {f_inicio}"
        self.f_inicio = f_inicio
        self.f_fin = f_fin
        self.id_cliente = cliente

    def __str__(self) -> str:
        return f"Numero de Habitación: {self.id}"
    
    