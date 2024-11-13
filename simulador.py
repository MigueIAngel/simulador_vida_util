
años = int(input("digite la cantidad de años: "))
ipc = float(input("digite el valor del IPC: "))

class Torre:
    def __init__(self, estructura, herrajes, aisladores, cable_conductor, cable_guarda):
        self.estructura = estructura
        self.herrajes = herrajes
        self.aisladores = aisladores
        self.cable_conductor = cable_conductor
        self.cable_guarda = cable_guarda
    def mostrar_años_restantes(self):
        return f"Años restantes:\nestructura: {self.estructura[0]}\nherrajes: {self.herrajes[0]}\naisladores: {self.aisladores[0]}\ncable conductor: {self.cable_conductor[0]}\ncable guarda: {self.cable_guarda[0]}"
    def mostrar_renovaciones(self):
        return f"Cantidad de renovaciones:\nestructura: {self.estructura[1]}\nherrajes: {self.herrajes[1]}\naisladores: {self.aisladores[1]}\ncable conductor: {self.cable_conductor[1]}\ncable guarda: {self.cable_guarda[1]}"
    

    def proyeccion_años(self):
        estructura = self.estructura
        herrajes = self.herrajes
        aisladores = self.aisladores
        cable_conductor = self.cable_conductor
        cable_guarda = self.cable_guarda
        for _ in range(años):
            if estructura[0] > 0:
                estructura[0] -= 1
            else:
                estructura[0] = 11
                estructura[1] +=1

            if herrajes[0] > 0:
                herrajes[0] -= 1
            else:
                herrajes[0] = 7
                herrajes[1] +=1

            if aisladores[0] > 0:
                aisladores[0] -= 1
            else:
                aisladores[0] = 7
                aisladores[1] +=1

            if cable_conductor[0] > 0:
                cable_conductor[0] -= 1
            else:
                cable_conductor[0] = 24
                cable_conductor[1] +=1

            if cable_guarda[0] > 0:
                cable_guarda[0] -= 1
            else:
                cable_guarda[0] = 8
                cable_guarda[1] +=1
        
    





torre = Torre(estructura=[11,0], herrajes=[7,0], aisladores=[7,0], cable_conductor=[24,0], cable_guarda=[8,0])
torre.proyeccion_años()
print(torre.mostrar_años_restantes())
print(torre.mostrar_renovaciones())