import pandas as pd
import matplotlib.pyplot as plt
import os

def analizar_ventas():
    # 1. Carga de datos
    # Se utiliza una ruta relativa para garantizar la reproducibilidad en cualquier entorno
    ruta_datos = 'datos/ventas.csv'
    if not os.path.exists(ruta_datos):
        raise FileNotFoundError(f"No se encontró el archivo de datos en {ruta_datos}")
        
    df = pd.DataFrame(pd.read_csv(ruta_datos))
    
    # Asegurar el formato correcto de fecha para el análisis temporal
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
    
    # 2. Cálculos estadísticos requeridos
    # Calculamos el total de cada transacción (precio * cantidad)
    df['ventas_totales'] = df['precio'] * df['cantidad_vendida']
    ingresos_totales = df['ventas_totales'].sum()
    
    # Identificar el producto más vendido sumando la cantidad vendida
    producto_mas_vendido = df.groupby('producto')['cantidad_vendida'].sum().idxmax()
    cantidad_mas_vendida = df.groupby('producto')['cantidad_vendida'].sum().max()
    
    # Agrupar las ventas totales por mes para analizar la tendencia
    df['mes'] = df['fecha_venta'].dt.to_period('M')
    ventas_por_mes = df.groupby('mes')['ventas_totales'].sum()
    
    # 3. Mostrar resultados por consola
    print("=== RESULTADOS DEL ANÁLISIS DE VENTAS ===")
    print(f"Ingresos Totales de la Empresa: ${ingresos_totales:,.2f}")
    print(f"Producto más Vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")
    print("\nVentas por Mes:")
    for mes, total in ventas_por_mes.items():
        print(f"  - {mes}: ${total:,.2f}")
    print("=========================================")
    
    # 4. Generación de gráfico de tendencia de ventas por mes
    # Usamos matplotlib para visualizar el desempeño comercial
    plt.figure(figsize=(8, 5))
    ventas_por_mes.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Evolución de Ventas Mensuales (Primer Semestre 2026)', fontsize=12, fontweight='bold')
    plt.xlabel('Periodo (Mes)', fontsize=10)
    plt.ylabel('Ventas Totales ($)', fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Guardar gráfico en la carpeta de resultados utilizando ruta relativa
    ruta_grafico = 'resultados/evolucion_ventas.png'
    plt.savefig(ruta_grafico)
    plt.close()
    print(f"Gráfico guardado con éxito en: {ruta_grafico}")

if __name__ == "__main__":
    analizar_ventas()
