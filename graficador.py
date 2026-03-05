import matplotlib.pyplot as plt

class Graficador:
    def __init__(self):
        # Estilo limpio para las gráficas
        plt.style.use('ggplot')

    def graficar_rendimiento(self, cantidad_procesos, tiempos_promedio, titulo, nombre_archivo):

        plt.figure(figsize=(8, 5))
        
        plt.plot(cantidad_procesos, tiempos_promedio, marker='o', linestyle='-', color='#1f77b4', linewidth=2)
        
        plt.title(titulo, fontsize=12, fontweight='bold')
        plt.xlabel('Cantidad de Procesos', fontsize=10)
        plt.ylabel('Tiempo Promedio en el Sistema', fontsize=10)
        
        plt.xticks(cantidad_procesos)
        
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()

        plt.savefig(nombre_archivo)
        plt.close()
        
        print(f"Éxito: Se generó '{nombre_archivo}'")
        