from graficador import Graficador

def main():
    graf = Graficador()
    procesos = [25, 50, 100, 150, 200]

    print("Generando gráficas del Sistema Operativo...\n")

    base_int_10 = [2.7399221701870933, 3.2341411479761355, 3.041771278469274, 2.8983259560040544, 2.944508395061419]
    base_int_5  = [3.7590929784500395, 4.185911053134365, 3.8416799521283567, 3.5917737273044343, 3.580103527835947]
    base_int_1  = [26.00121219033349, 42.12467989786027, 69.87472631896838, 99.3357984809701, 131.2278856060693]

    graf.graficar_rendimiento(procesos, base_int_10, "Base - Intervalo 10", "1_Base_Int10.png")
    graf.graficar_rendimiento(procesos, base_int_5,  "Base - Intervalo 5",  "2_Base_Int5.png")
    graf.graficar_rendimiento(procesos, base_int_1,  "Base - Intervalo 1",  "3_Base_Int1.png")

    ram200_int_10 = [2.7399221701870933, 3.2341411479761355, 3.041771278469274, 2.8983259560040544, 2.944508395061419]
    ram200_int_5  = [3.7590929784500395, 4.185911053134365, 3.8416799521283567, 3.5917737273044343, 3.580103527835947]
    ram200_int_1  = [26.00121219033349, 45.186519935691365, 72.9394617517474, 101.55218565920141, 128.8711207855608]

    graf.graficar_rendimiento(procesos, ram200_int_10, "RAM 200 - Intervalo 10", "4_RAM200_Int10.png")
    graf.graficar_rendimiento(procesos, ram200_int_5,  "RAM 200 - Intervalo 5",  "5_RAM200_Int5.png")
    graf.graficar_rendimiento(procesos, ram200_int_1,  "RAM 200 - Intervalo 1",  "6_RAM200_Int1.png")

    cpuRap_int_10 = [1.502871848362984, 1.6215636145315364, 1.5294811270758777, 1.5651951653625, 1.5516494489074806]
    cpuRap_int_5  = [1.7366554924497102, 1.8317763629539756, 1.7207741457572967, 1.7521328910158722, 1.7259501287008376]
    cpuRap_int_1  = [9.506573581449898, 15.198625224333973, 27.98798708033443, 40.85951777065686, 54.793699503338864]

    graf.graficar_rendimiento(procesos, cpuRap_int_10, "CPU Rápido (6) - Intervalo 10", "7_CPURapido_Int10.png")
    graf.graficar_rendimiento(procesos, cpuRap_int_5,  "CPU Rápido (6) - Intervalo 5",  "8_CPURapido_Int5.png")
    graf.graficar_rendimiento(procesos, cpuRap_int_1,  "CPU Rápido (6) - Intervalo 1",  "9_CPURapido_Int1.png")

    cpu2_int_10 = [2.12, 2.2891304364356406, 2.284969018919341, 2.2577267911649472, 2.3341019119553787]
    cpu2_int_5  = [2.414419429635321, 2.379838068722746, 2.2943427097705467, 2.3464723451920406, 2.3907148468045936]
    cpu2_int_1  = [6.231156997688436, 5.238621314960557, 6.155833664195896, 9.123371152195167, 10.098383721304021]

    graf.graficar_rendimiento(procesos, cpu2_int_10, "2 CPUs - Intervalo 10", "10_2CPUs_Int10.png")
    graf.graficar_rendimiento(procesos, cpu2_int_5,  "2 CPUs - Intervalo 5",  "11_2CPUs_Int5.png")
    graf.graficar_rendimiento(procesos, cpu2_int_1,  "2 CPUs - Intervalo 1",  "12_2CPUs_Int1.png")

if __name__ == "__main__":
    main()
    
    