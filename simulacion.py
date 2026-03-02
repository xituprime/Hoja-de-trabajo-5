import simpy
import random
import statistics
from proceso import Proceso


class Simulacion:

    def __init__(self, num_procesos, intervalo_llegada, capacidad_ram, velocidad_cpu, num_cpus):

        self.env = simpy.Environment()

        self.num_procesos = num_procesos
        self.intervalo = intervalo_llegada

        self.ram = simpy.Container(
            self.env,
            init = capacidad_ram,
            capacity = capacidad_ram
        )

        self.cpu = simpy.Resource(
            self.env,
            capacity = num_cpus
        )

        self.velocidad_cpu = velocidad_cpu
        self.tiempos = []

    def generar_procesos(self):

        for i in range(self.num_procesos):
            proceso = Proceso(i, self.env, self)
            self.env.process(proceso.ejecutar())

            tiempo_llegada = random.expovariate(1.0 / self.intervalo)
            yield self.env.timeout(tiempo_llegada)

    def correr(self):
        self.env.process(self.generar_procesos())
        self.env.run()

    def calcular_estadisticas(self):

        promedio = statistics.mean(self.tiempos) if self.tiempos else 0
        desviacion = statistics.stdev(self.tiempos) if len(self.tiempos) > 1 else 0

        return promedio, desviacion