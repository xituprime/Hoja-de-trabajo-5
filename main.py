import random
from simulacion import Simulacion


def main():

    random.seed(42)

    print("===== SIMULACIÓN SISTEMA OPERATIVO =====")

    num_procesos = int(input("Cantidad de procesos: "))
    intervalo = float(input("Intervalo de llegada: "))
    capacidad_ram = int(input("Capacidad de RAM: "))
    velocidad_cpu = int(input("Instrucciones por unidad de tiempo: "))
    num_cpus = int(input("Número de CPUs: "))

    sim = Simulacion(
        num_procesos,
        intervalo,
        capacidad_ram,
        velocidad_cpu,
        num_cpus
    )

    sim.correr()

    promedio, desviacion = sim.calcular_estadisticas()

    print("\nRESULTADOS")
    print("Tiempo promedio:", promedio)
    print("Desviación estándar:", desviacion)


if __name__ == "__main__":
    main()
    