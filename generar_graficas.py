from graficador import Graficador

def main():
    graf = Graficador()
    procesos = [25, 50, 100, 150, 200]

    print("Generando gráficas del Sistema Operativo...\n")

    base_int_10 = [0.0, 0.0, 0.0, 0.0, 0.0]
    base_int_5  = [0.0, 0.0, 0.0, 0.0, 0.0]
    base_int_1  = [0.0, 0.0, 0.0, 0.0, 0.0]

    graf.graficar_rendimiento(procesos, base_int_10, "Base - Intervalo 10", "1_Base_Int10.png")
    graf.graficar_rendimiento(procesos, base_int_5,  "Base - Intervalo 5",  "2_Base_Int5.png")
    graf.graficar_rendimiento(procesos, base_int_1,  "Base - Intervalo 1",  "3_Base_Int1.png")

    ram200_int_10 = [0.0, 0.0, 0.0, 0.0, 0.0]
    ram200_int_5  = [0.0, 0.0, 0.0, 0.0, 0.0]
    ram200_int_1  = [0.0, 0.0, 0.0, 0.0, 0.0]

    graf.graficar_rendimiento(procesos, ram200_int_10, "RAM 200 - Intervalo 10", "4_RAM200_Int10.png")
    graf.graficar_rendimiento(procesos, ram200_int_5,  "RAM 200 - Intervalo 5",  "5_RAM200_Int5.png")
    graf.graficar_rendimiento(procesos, ram200_int_1,  "RAM 200 - Intervalo 1",  "6_RAM200_Int1.png")

    cpuRap_int_10 = [0.0, 0.0, 0.0, 0.0, 0.0]
    cpuRap_int_5  = [0.0, 0.0, 0.0, 0.0, 0.0]
    cpuRap_int_1  = [0.0, 0.0, 0.0, 0.0, 0.0]

    graf.graficar_rendimiento(procesos, cpuRap_int_10, "CPU Rápido (6) - Intervalo 10", "7_CPURapido_Int10.png")
    graf.graficar_rendimiento(procesos, cpuRap_int_5,  "CPU Rápido (6) - Intervalo 5",  "8_CPURapido_Int5.png")
    graf.graficar_rendimiento(procesos, cpuRap_int_1,  "CPU Rápido (6) - Intervalo 1",  "9_CPURapido_Int1.png")

    cpu2_int_10 = [0.0, 0.0, 0.0, 0.0, 0.0]
    cpu2_int_5  = [0.0, 0.0, 0.0, 0.0, 0.0]
    cpu2_int_1  = [0.0, 0.0, 0.0, 0.0, 0.0]

    graf.graficar_rendimiento(procesos, cpu2_int_10, "2 CPUs - Intervalo 10", "10_2CPUs_Int10.png")
    graf.graficar_rendimiento(procesos, cpu2_int_5,  "2 CPUs - Intervalo 5",  "11_2CPUs_Int5.png")
    graf.graficar_rendimiento(procesos, cpu2_int_1,  "2 CPUs - Intervalo 1",  "12_2CPUs_Int1.png")

    print("\n¡Proceso terminado! Revisa la carpeta de tu proyecto.")

if __name__ == "__main__":
    main()
    