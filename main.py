import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import pandas as pd
años = int(input("digite la cantidad de años: "))
ipc = float(input("digite el valor del IPC: "))
# techo = int(input("digite el valor del techo: "))
class Elemento:
    def __init__(self, vida_remanente, costo, años_restantes):
        self.vida_remanente = vida_remanente
        self.costo = costo
        self.años_restantes = años_restantes


class Activo:
    def __init__(self, estructura, herrajes, aisladores, cable_conductor, cable_guarda):
        self.estructura = estructura
        self.herrajes = herrajes
        self.aisladores = aisladores
        self.cable_conductor = cable_conductor
        self.cable_guarda = cable_guarda
        self.costo = {}

    def mostrar_años_restantes(self):
        return min(self.estructura.años_restantes, self.herrajes.años_restantes, self.aisladores.años_restantes, self.cable_conductor.años_restantes, self.cable_guarda.años_restantes)
    
    def mostrar_años(self):
        return self.estructura.años_restantes, self.herrajes.años_restantes, self.aisladores.años_restantes, self.cable_conductor.años_restantes, self.cable_guarda.años_restantes
    def mostrar_renovaciones(self):
        print(f"Cantidad de renovaciones:\nestructura: {self.estructura.vida_remanente}\nherrajes: {self.herrajes.vida_remanente}\naisladores: {self.aisladores.vida_remanente}\ncable conductor: {self.cable_conductor.vida_remanente}\ncable guarda: {self.cable_guarda.vida_remanente}")
    def proyeccion_años(self):
        estructura = self.estructura
        herrajes = self.herrajes
        aisladores = self.aisladores
        cable_conductor = self.cable_conductor
        cable_guarda = self.cable_guarda

        for año in range(años+1):
            if año == 0 :
                continue
            a, b, c, d, e = 0, 0, 0, 0, 0
            vida_remanente = self.mostrar_años_restantes()
            if estructura.años_restantes > 1:
                estructura.años_restantes -= 1
            else:
                a = self.proyeccion_costo(año, estructura.costo)
                estructura.años_restantes = estructura.vida_remanente
                vida_remanente = self.mostrar_años_restantes() + 6
            if herrajes.años_restantes > 1:
                herrajes.años_restantes -= 1
            else:
                b = self.proyeccion_costo(año, herrajes.costo)
                herrajes.años_restantes = herrajes.vida_remanente
                vida_remanente = self.mostrar_años_restantes() + 6
            if aisladores.años_restantes > 1:
                aisladores.años_restantes -= 1
            else:
                c = self.proyeccion_costo(año, aisladores.costo)
                aisladores.años_restantes = aisladores.vida_remanente
                vida_remanente = self.mostrar_años_restantes() + 6

            if cable_conductor.años_restantes > 1:
                cable_conductor.años_restantes -= 1
            else:
                d = self.proyeccion_costo(año, cable_conductor.costo)
                cable_conductor.años_restantes = cable_conductor.vida_remanente
                vida_remanente = self.mostrar_años_restantes() + 6

            if cable_guarda.años_restantes > 1:
                cable_guarda.años_restantes -= 1
            else:
                e = self.proyeccion_costo(año, cable_guarda.costo)
                cable_guarda.años_restantes = cable_guarda.vida_remanente
                vida_remanente = self.mostrar_años_restantes() + 6
            self.costo[año] = {"estructura": a, "herrajes": b, "aisladores": c, "cable conductor": d, "cable guarda": e, "vida_remanente": vida_remanente}
    def proyeccion_años_techo(self, techo):
        estructura = self.estructura
        herrajes = self.herrajes
        aisladores = self.aisladores
        cable_conductor = self.cable_conductor
        cable_guarda = self.cable_guarda
        vida_remanente = techo 
        for año in range(años+1):
            if año == 0 :
                continue
            vida_remanente -= 1
            a, b, c, d, e = 0, 0, 0, 0, 0
            if estructura.años_restantes > 1:
                estructura.años_restantes -= 1
            else:
                a = self.proyeccion_costo(año, estructura.costo)
                estructura.años_restantes = estructura.vida_remanente
                vida_remanente = estructura.vida_remanente * 2 if estructura.vida_remanente * 2 < techo else techo
            if herrajes.años_restantes > 1:
                herrajes.años_restantes -= 1
            else:
                b = self.proyeccion_costo(año, herrajes.costo)
                herrajes.años_restantes = herrajes.vida_remanente
                vida_remanente = herrajes.vida_remanente * 2 if herrajes.vida_remanente * 2 < techo else techo
            if aisladores.años_restantes > 1:
                aisladores.años_restantes -= 1
            else:
                c = self.proyeccion_costo(año, aisladores.costo)
                aisladores.años_restantes = aisladores.vida_remanente
                vida_remanente = aisladores.vida_remanente * 2 if aisladores.vida_remanente * 2 < techo else techo
            if cable_conductor.años_restantes > 1:
                cable_conductor.años_restantes -= 1
            else:
                d = self.proyeccion_costo(año, cable_conductor.costo)
                cable_conductor.años_restantes = cable_conductor.vida_remanente
                vida_remanente = cable_conductor.vida_remanente * 2 if cable_conductor.vida_remanente * 2 < techo else techo
            if cable_guarda.años_restantes > 1:
                cable_guarda.años_restantes -= 1
            else:
                e = self.proyeccion_costo(año, cable_guarda.costo)
                cable_guarda.años_restantes = cable_guarda.vida_remanente
                vida_remanente = cable_guarda.vida_remanente * 2 if cable_guarda.vida_remanente * 2 < techo else techo
            self.costo[año] = {"estructura": a, "herrajes": b, "aisladores": c, "cable conductor": d, "cable guarda": e, "vida_remanente": vida_remanente}



    def imprimir_costos(self):
        for key, value in self.costo.items():
            costos = {k: f"{v:.2f}" for k, v in value.items()}
            print(f"año: {key}, costos: {costos}")
    def proyeccion_costo(self, años, elemento):
        return elemento * (1 + ipc) ** años
    
    def grafica(self):
        claves = list(self.costo[1].keys())
        años = list(self.costo.keys())
        colores = cm.rainbow(np.linspace(0, 1, len(claves)))

        fig, axs = plt.subplots((len(claves) + 1) // 2, 2, figsize=(15, 10), sharex=True)
        fig.suptitle("Proyección", fontsize=16)

        for i, (clave, color) in enumerate(zip(claves, colores)):
            valores = [dic[clave] for dic in self.costo.values()]
            ax = axs[i // 2, i % 2]
           
            valores_filtrados = [valor for valor in valores if valor > 0]
            años_filtrados = [año for año, valor in zip(años, valores) if valor > 0]
            ax.plot(años_filtrados, valores_filtrados, label=clave, marker="o", linestyle="-", color=color)
            ax.set_ylabel("Costo")
            ax.legend()
            ax.grid(True)
            
        plt.xlabel("Años")
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
        plt.savefig("grafica.png")
    def print_toExcel(self):
        df = pd.DataFrame.from_dict(self.costo, orient='index')
        df.index.name = 'Año'
        with pd.ExcelWriter('costos.xlsx', mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name='Proyeccion de Costos')

   
        
aislador = Elemento(7, 1000000, 7)
herraje = Elemento(7, 1000000, 7)
estructura = Elemento(11, 1000000, 11)
cable_conductor = Elemento(24, 1000000, 24)
cable_guarda = Elemento(8, 1000000, 8)
cimentacion = Elemento(50, 1000000, 50)

activo = Activo(estructura, herraje, aislador, cable_conductor, cable_guarda)

activo.proyeccion_años()
activo.imprimir_costos()

activo.grafica()
activo.print_toExcel()