import numpy as np
import pandas as pd
import random
import os
import calendar
import matplotlib.pyplot as plt

# Función para generar registros pluviales aleatorios
def generar_registro_pluvial():
    # Crear un DataFrame con días como filas y meses como columnas
    dias = 31  # Max días en un mes
    registros = []

    for mes in range(1, 13):
        if mes in [4, 6, 9, 11]:
            dias = 30
        elif mes == 2:
            dias = 28  # Asumimos un año no bisiesto

        # Generar lluvia aleatoria para los días del mes
        lluvia_mes = [random.uniform(0, 20) for _ in range(dias)]
        # Rellenar con ceros los días restantes si el mes tiene menos de 31 días
        lluvia_mes.extend([0] * (31 - dias))
        registros.append(lluvia_mes)

    # Crear un DataFrame con los registros
    df = pd.DataFrame(np.array(registros).T, columns=[calendar.month_name[m] for m in range(1, 13)])
    return df

# Función para guardar el registro en un archivo CSV
def guardar_en_csv(df, year):
    df.to_csv(f'registroPluvial{year}.csv', index=False)
    print(f"Registro pluvial guardado en 'registroPluvial{year}.csv'.")

# Función para leer el archivo CSV
def leer_registro_csv(year):
    return pd.read_csv(f'registroPluvial{year}.csv')

# Función para mostrar registros del mes elegido
def mostrar_registro_mes(df, mes):
    mes_nombre = calendar.month_name[mes]
    registros_mes = df[mes_nombre]
    
    print(f"Registros de lluvia para el mes {mes_nombre}:")
    print(registros_mes.to_string(index=False))

# Función para graficar los datos
def graficar_datos(df):
    # Gráfico de barras de lluvias anuales
    total_anual = df.sum()
    total_anual.plot(kind='bar', title='Lluvias Anuales (mm)', xlabel='Meses', ylabel='Lluvia (mm)')
    plt.xticks(rotation=45)
    plt.show()

    # Gráfico de dispersión
    dias = np.arange(1, 32)
    for mes in df.columns:
        plt.scatter([list(calendar.month_name).index(mes)] * len(df[mes]), dias[:len(df[mes])], label=mes)
    
    plt.title('Dispersión de Lluvias por Mes')
    plt.xlabel('Meses')
    plt.ylabel('Días')
    plt.xticks(range(1, 13), list(calendar.month_name[1:]), rotation=45)
    plt.legend()
    plt.show()

    # Gráfico circular
    total_mensual = df.sum()
    plt.pie(total_mensual, labels=total_mensual.index, autopct='%1.1f%%')
    plt.title('Distribución de Lluvias Mensuales')
    plt.show()

# Función principal
def main():
    year = 2023
    filename = f'registroPluvial{year}.csv'

    # Verificar si el archivo CSV existe
    if os.path.exists(filename):
        print("Cargando registros pluviales desde el archivo CSV...")
        df = leer_registro_csv(year)
    else:
        print("Archivo no encontrado. Generando registros pluviales aleatorios...")
        df = generar_registro_pluvial()
        guardar_en_csv(df, year)

    # Solicitar al usuario que elija un mes
    mes = int(input("Introduce el número del mes (1-12) para mostrar el registro de lluvia: "))
    
    if 1 <= mes <= 12:
        mostrar_registro_mes(df, mes)
    else:
        print("Mes no válido. Debe estar entre 1 y 12.")
    
    # Graficar los datos
    graficar_datos(df)

if __name__ == "__main__":
    main()
