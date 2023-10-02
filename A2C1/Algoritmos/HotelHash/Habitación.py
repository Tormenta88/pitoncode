# -*- coding: utf-8 -*-

class Habitacion:
    def __init__(self, num_habitacion):
        self.id = num_habitacion

    def __str__(self) -> str:
        return f"Numero de Habitación: {self.id}"
    
    def get_id(self):
        return self.id