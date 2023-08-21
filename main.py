class Asiento:
    def __init__(self,color,precio,registro):
        self.precio = precio
        self.color = color
        self.registro = registro
        
    def cambiarColor(self,color):
        if color in ["rojo","verde","amarillo","negro","blanco"]:
                
            self.color = color
        
class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo= modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor= motor
        self.registro=registro
        self.cantidadCreados += 1
        
    def cantidadAsientos(self,):
        cantidad=0
        for item in self.asientos:
            if item !=None:
                cantidad+=1
        return cantidad
        
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if asiento != None:
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
        if tipomotor == "gasolina" or tipomotor== "electrico":
            
            self.tipo= tipomotor
    