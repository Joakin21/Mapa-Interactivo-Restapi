
from flask import Flask, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

sucursales = {10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[]}

def obtenerColor(numero):
    color = ""
    if numero == 0:
        color = "orange"
    if numero == 1:
        color = "purple"
    if numero == 2:
        color = "green"
    if numero == 3:
        color = "red"
    if numero == 4:
        color = "blue"
    return color
    

def leerCsvSucursales():
    global sucursales
    #sucursales = []
    with open('sucursales.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sucursal = row["sucursal"]
            formato_cpe = obtenerColor(int(row["formato cpe"]))
            formato_m1 = obtenerColor(int(row["Formato M1"]))
            lat = float(row["Latitud"].replace(',','.'))
            lng = float(row["Longitud"].replace(',','.'))

            obj_sucursal = {"sucursal":sucursal, "formato_cpe":formato_cpe, "formato_m1":formato_m1, "coordenadas":{"lat":lat, "lng":lng}}

            if (sucursal == '10'):
                sucursales[10].append(obj_sucursal)
            if (sucursal == '11'):
                sucursales[11].append(obj_sucursal)
            if (sucursal == '12'):
                sucursales[12].append(obj_sucursal)
            if (sucursal == '13'):
                sucursales[13].append(obj_sucursal)
            if (sucursal == '14'):
                sucursales[14].append(obj_sucursal)
            if (sucursal == '15'):
                sucursales[15].append(obj_sucursal)
            if (sucursal == '16'):
                sucursales[16].append(obj_sucursal)

leerCsvSucursales()




@app.route('/sucursales/<int:sucursal>')
def getSucursal(sucursal):
    #sucursales = leerCsvSucursales()

    return jsonify(sucursales[sucursal])


if __name__ == '__main__':
    app.run(debug=True, port=4000)




