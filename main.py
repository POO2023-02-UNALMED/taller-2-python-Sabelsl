class Asiento:
    def __init__(self,color,precio,registro):
        self.precio = precio
        self.color = color
        self.registro = registro
        
    def cambiarColor(self,color):
        if color in ["rojo","verde","amarillo","negro","blanco"]:
                
            self.color = color
        
class Auto:
    def __init__(self):
        self.modelo= ""
        self.precio = 0
        self.asientos = []
        self.marca = ""
        self.motor= Motor()
        self.registro=0
        self.cantidadCreados=0
        
    def cantidadAsientos(self,):
        return len(self.asientos)
        
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if self.registro != asiento.registro:
                    return "Las piezas no son originales"
            return "Auto original"    
        else:   
            return "Las piezas no son originales"

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo= tipo
        self.registro = registro
        
    def cambiarRegistro(self,valorregistro):
        self.registro = valorregistro
        
    def asignarTipo (self,tipomotor):
        if self.tipo == "gasolina" or self.tipo== "electrico":
            
            self.tipo= tipomotor
    