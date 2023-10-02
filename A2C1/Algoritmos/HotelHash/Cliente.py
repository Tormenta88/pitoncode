# -*- coding: utf-8 -*-

class Cliente:
    def __init__(self, dni,  nombre, apellido):
        self.id = dni
        self.nombre = nombre
        self. apellido = apellido

    def __str__(self) -> str:
        return f"DNI: {self.id}, {self.nombre} {self.apellido}"
    
    def get_id(self):
        return self.id