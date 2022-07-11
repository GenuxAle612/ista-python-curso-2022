from flask import Flask
import csv, json


app=Flask(__name__)

@app.route('/')
def index():
    return 'Lista de estudiantes de Genesis por CSV'

@app.route('/estudiantes', methods=['GET'])
def lista_estudiantes():
    with open('datos\estudiante.csv') as file:
        reader = csv.reader(file)
        next(reader)       
        lista = []
        for columna in reader:
            lista.append({
                'cedula': columna[0],
                'primer_apellido': columna[1],
                'segundo_apellido': columna[2],
                'primer_nombre': columna[3],
                'segundo_nombre': columna[4]
            })
    return json . dumps(lista)


if __name__ == '__main__':
    app.run(debug=True)
    
    """
    import csv
 
with open('example.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
    
    """