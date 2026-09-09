class car:
    numCarros = 0
    
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        car.numCarros += 1
    
    def imprimir(self):
        print(f"Marca del carro: {self.marca}")
        
taxi = car("nissan",2004,"123-abc")
carro = car("honda", 2009, "12315")
taxi.imprimir()

print(f"Numero de carros: {car.numCarros} ")