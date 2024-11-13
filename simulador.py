
años = int(input("digite la cantidad de años: "))
ipc = float(input("digite el valor del IPC: "))

class Torre:
    def __init__(self, estructura, herrajes, aisladores, cable_conductor, cable_guarda):
        self.estructura = estructura
        self.herrajes = herrajes
        self.aisladores = aisladores
        self.cable_conductor = cable_conductor
        self.cable_guarda = cable_guarda
        self.costo = {}
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
        a, b, c, d, e = 0, 0, 0, 0, 0
        for año in range(años):
            if estructura[0] > 0:
                estructura[0] -= 1
            else:
                a= self.proyeccion_costo(año, estructura[2])
                estructura[0] = 11
                estructura[1] +=1

            if herrajes[0] > 0:
                herrajes[0] -= 1
            else:
                b = self.proyeccion_costo(año, herrajes[2])
                herrajes[0] = 7
                herrajes[1] +=1

            if aisladores[0] > 0:
                aisladores[0] -= 1
            else:
                c = self.proyeccion_costo(año, aisladores[2])
                aisladores[0] = 7
                aisladores[1] +=1

            if cable_conductor[0] > 0:
                cable_conductor[0] -= 1
            else:
                d = self.proyeccion_costo(año, cable_conductor[2])
                cable_conductor[0] = 24
                cable_conductor[1] +=1

            if cable_guarda[0] > 0:
                cable_guarda[0] -= 1
            else:
                e = self.proyeccion_costo(año, cable_guarda[2])
                cable_guarda[0] = 8
                cable_guarda[1] +=1
            self.costo[año] = {"estructura": a, "herrajes": b, "aisladores": c, "cable conductor": d, "cable guarda": e}
    def proyeccion_costo(self, años, elemento):
        return elemento * (1 + ipc) ** años
    
    def proyeccion_años_v2(self):
        estructura = self.estructura
        herrajes = self.herrajes
        aisladores = self.aisladores
        cable_conductor = self.cable_conductor
        cable_guarda = self.cable_guarda
        año = 0
        while año < años:
            minimo = min(estructura[0], herrajes[0], aisladores[0], cable_conductor[0], cable_guarda[0])
            estructura[0] -= minimo
            herrajes[0] -= minimo
            aisladores[0] -= minimo
            cable_conductor[0] -= minimo
            cable_guarda[0] -= minimo
            año += minimo
            a, b, c, d, e = 0, 0, 0, 0, 0
            if estructura[0] <= 1:
                a = self.proyeccion_costo(año, estructura[2])
                estructura[0] = 11
                estructura[1] += 1
            if herrajes[0] <= 1:
                b = self.proyeccion_costo(año, herrajes[2])
                herrajes[0] = 7
                herrajes[1] += 1
            if aisladores[0] <= 1:
                c = self.proyeccion_costo(año, aisladores[2])
                aisladores[0] = 7
                aisladores[1] += 1
            if cable_conductor[0] <= 1:
                d = self.proyeccion_costo(año, cable_conductor[2])
                cable_conductor[0] = 24
                cable_conductor[1] += 1
            if cable_guarda[0] <= 1:
                e = self.proyeccion_costo(año, cable_guarda[2])
                cable_guarda[0] = 8
                cable_guarda[1] += 1
            self.costo[año] = {"estructura": a, "herrajes": b, "aisladores": c, "cable conductor": d, "cable guarda": e}
    def imprimir_costos(self):
        for key, value in self.costo.items():
            print(f"año: {key}, costos: {value}") 
    


torre = Torre(estructura=[11,0,100], herrajes=[7,0,100], aisladores=[7,0,100], cable_conductor=[24,0,100], cable_guarda=[8,0,100])
torre.proyeccion_años_v2()
print(torre.mostrar_años_restantes())
print(torre.mostrar_renovaciones())
print(torre.imprimir_costos())

