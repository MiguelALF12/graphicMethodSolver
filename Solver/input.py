import csv
import time as tm
saved_excercises = []

def standardized_csv():
    global saved_excercises

    for item in saved_excercises:
        if '-' in item and len(item) == 2:
            saved_excercises.remove(saved_excercises[saved_excercises.index(item)])

def open_csv():
    global saved_excercises
    with open("Solver/excercises.csv", encoding=("utf-8-sig")) as File:
        reader = csv.reader(File, delimiter=";")
        for row in reader:
            saved_excercises.append(row)
        standardized_csv()
    print("El ejercicio cargado es el siguiente", saved_excercises)

def input():
    print("------------ BIENVENIDO AL SOLUCIONADOR USANDO MÉTODO GRÁFICO ------------\n")
    print("\t**Este método es usado para problemas que utilizan dos variables de análisis y decisión")
    print("\tEN ESTOS MOMENTOS SE ESTA LEYENDO EL PROBLEMA")
    time = 0
    while time < 4:
        print("* ",end="")
        tm.sleep(1)
        time+=1
    print("\n")
    open_csv()
    return saved_excercises

