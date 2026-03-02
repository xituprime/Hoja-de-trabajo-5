import random

class Proceso:
    
    def __init__ (self, id_proceso, env, simulacion):
        self.id = id_proceso
        self.env = env
        self.sim = simulacion

        self.memoria_requerida = random.randint(1,10)
        self.instrucciones_totales = random.randint(1,10)
        self.intrucciones_restantes = self.instrucciones_totales

        self.tiempo_llegada = env.now
        self.tiempo_salida = None

    def ejecutar(self):

        yield self.sim.ram.get(self.memoria_requerida)

        while self.intrucciones_restantes > 0:

            with self.sim.cpu.request() as req:
                yield req

                intrucciones = min(
                    self.sim.velocidad_cpu,
                    self.intrucciones_restantes
                )

                yield self.env.timeout(1)
                self.intrucciones_restantes -= intrucciones

            if self.intrucciones_restantes > 0:
                decision = random.randint(1, 21)
                if decision == 1:
                    yield self.env.timeout(1)

        self.tiempo_salida = self.env.now

        yield self.sim.ram.put(self.memoria_requerida)

        tiempo_total = self.tiempo_salida - self.tiempo_llegada
        self.sim.tiempos.append(tiempo_total)