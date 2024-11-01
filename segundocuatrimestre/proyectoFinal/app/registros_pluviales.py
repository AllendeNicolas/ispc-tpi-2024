import numpy as np
import pandas as pd
import os
import calendar
import matplotlib.pyplot as plt

# Ruta generalizada para almacenamiento de archivos
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datosAnalizados")
os.makedirs(path, exist_ok=True)  # Crear carpeta si no existe

# Función para generar y guardar registros pluviales en un CSV si no existe
def generar_registro_pluvial(year):
    import random
    filename = os.path.join(path, f'registroPluvial{year}.csv')
    
    # Verificar si el archivo ya existe
    if os.path.exists(filename):
        print(f"Archivo '{filename}' encontrado. Cargando datos existentes...")
        return pd.read_csv(filename)
    else:
        print("Generando registros pluviales aleatorios para el año", year)
        np.random.seed(42)  # Consistencia en datos aleatorios
        precipitaciones = np.round(np.random.rand(372) * 100, 2).reshape(31, 12)
        
        # Crear DataFrame de Pandas con nombres de columnas (meses)
        columnas = [calendar.month_name[m] for m in range(1, 13)]
        df = pd.DataFrame(precipitaciones, columns=columnas)

        # Guardar el DataFrame como CSV
        df.to_csv(filename, index=False)
        print(f"Registro pluvial guardado en '{filename}'.")
        return df

# Función para mostrar estadísticas anuales
def mostrar_estadisticas_anuales(df):
    print('-' * 80)
    print("Estadísticas anuales de precipitación:")
    print("Máximo anual:", df.max().max())
    print("Mínimo anual:", df.min().min())
    print("Promedio anual:", df.mean().mean())

# Función para mostrar estadísticas de un mes específico
def mostrar_estadisticas_mes(df, mes):
    mes_nombre = calendar.month_name[mes]
    registros_mes = df[mes_nombre]

    # Mostrar estadísticas
    print(f"Estadísticas de lluvia para el mes {mes_nombre}:")
    print(f"Máximo: {registros_mes.max():.2f} mm")
    print(f"Mínimo: {registros_mes.min():.2f} mm")
    print(f"Promedio: {registros_mes.mean():.2f} mm\n")
    print("Registros diarios de precipitación en", mes_nombre)
    print(registros_mes.to_string(index=False))

# Función para crear gráficos
def graficar_datos(df, mes=None):
    # Gráfico de barras de lluvias anuales
    plt.figure()
    total_anual = df.sum()
    total_anual.plot(kind='bar', title='Lluvias Anuales (mm)', xlabel='Meses', ylabel='Lluvia (mm)')
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(path, "grafico_barras_anual.png"))
    plt.close()

    # Gráfico de dispersión
    plt.figure()
    dias = np.arange(1, 32)
    for mes_col in df.columns:
        plt.scatter([list(calendar.month_name).index(mes_col)] * len(df[mes_col]), dias[:len(df[mes_col])], label=mes_col)
    plt.title('Dispersión de Lluvias por Mes')
    plt.xlabel('Meses')
    plt.ylabel('Días')
    plt.xticks(range(1, 13), list(calendar.month_name[1:]), rotation=45)
    plt.legend()
    plt.savefig(os.path.join(path, "grafico_dispersión_anual.png"))
    plt.close()

    # Gráfico circular anual
    plt.figure()
    total_mensual = df.sum()
    plt.pie(total_mensual, labels=total_mensual.index, autopct='%1.1f%%')
    plt.title('Distribución de Lluvias Mensuales')
    plt.savefig(os.path.join(path, "grafico_pie_anual.png"))
    plt.close()

    if mes is not None:
        # Gráfico circular para el mes específico
        mes_nombre = calendar.month_name[mes]
        dias_en_mes = len(df[mes_nombre])  # Obtener días en el mes específico
        plt.figure()
        plt.pie(df[mes_nombre], labels=np.arange(1, dias_en_mes + 1), autopct='%1.1f%%')
        plt.title(f'Distribución de Lluvias en {mes_nombre}')
        plt.savefig(os.path.join(path, f"grafico_pie_{mes_nombre}.png"))
        plt.close()

# Función principal que incluye el menú
def menuRegistrosPluviales():

    print('')
    print("-" * 30 ,"ANÁLISIS DE DATOS","-" * 30)
    print("-" * 30 ,"REGISTROS PLUVIALES","-" * 30)
    print('')

    year = int(input('Ingresa el año que desea analizar (1985-2024): '))
    while year < 1985 or year > 2024:
        print("Año no válido. Debe estar entre 1985 y 2024.")
        year = int(input("Introduce un año nuevamente: "))
    
    # Cargar o generar registros pluviales
    df = generar_registro_pluvial(year)

    while True:
        print('')
        print("-" * 30 ,"REGISTROS PLUVIALES","-" * 30)
        print("-" * 30 , "Menú", "-" * 30)
        print("1) Mostrar estadísticas anuales de precipitación")
        print("2) Generar gráficos de registros pluviales anuales")
        print("3) Analizar un mes específico")
        print("4) Volver al menú anterior")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_estadisticas_anuales(df)
        elif opcion == "2":
            graficar_datos(df)
            print("Gráficos guardados en la carpeta 'datosAnalizados'.")
        elif opcion == "3":
            mes = int(input("Introduce el número del mes (1-12) para analizar: "))
            while mes < 1 or mes > 12:
                print("Mes no válido. Debe estar entre 1 y 12.")
                mes = int(input("Introduce el número del mes (1-12) nuevamente: "))
            mostrar_estadisticas_mes(df, mes)
            graficar_datos(df, mes)
            print(f"Gráfico para {calendar.month_name[mes]} guardado en 'datosAnalizados'.")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")