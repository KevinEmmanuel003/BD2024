from flask import Flask, render_template, request, redirect, url_for
#importamos la libreria mysql para la conexión
import mysql.connector


app = Flask(__name__)

#Conexión a la base de datos
def create_connection():
    return mysql.connector.connect(
        host= "localhost",
        user = "root",
        password = "root",
        database = "reto",
    )
#Página principal (index)
@app.route('/')
def index():
    return render_template('index.html')

#formulario para agragar datos
@app.route('/add_data', methods = ['GET', 'POST'])
def agregarDatos():
    if request.method == 'POST':
        #Relación de variables
        pais = request.form['pais']
        estado = request.form['estado']
        ciudad = request.form['ciudad']
        codigo_postal = request.form['codigo_postal']
        colonia = request.form['colonia']
        connection = create_connection()
        cursor = connection.cursor()

        #ingresar pais
        curso.execute("INSERT INTO paises (nombre) VALUES (%s)",(pais,))
        connection.commit() #envia la decalraciòn al servidor de MySQL y confirma la transacciòn
        pais_id = cursor.lastrowid #devuelve el valor generado para el autoingramentable

        #ingresar estado
        curso.execute("INSERT INTO estados (nombre, pais_id) VALUES (%s, %s)",(estado, pais_id))
        connection.commit()
        estado_id = cursor.lastrowid

        #ingresar ciudad
        curso.execute("INSERT INTO ciudades (nombre, estado_id) VALUES (%s, %s)",(ciudad, estado_id))
        connection.commit()
        ciudad_id = cursor.lastrowid

        #ingresar còdigo postal
        curso.execute("INSERT INTO codigos_postales (nombre, ciudad_id) VALUES (%s, %s)",(codigo_postal, ciudad_id))
        connection.commit()
        codigo_postal_id = cursor.lastrowid

        #ingresar Colonia
        curso.execute("INSERT INTO colonias (nombre, ciudad_id, codigo_postal_id) VALUES (%s, %s, %s)",(colonia, ciudad_id, codigo_postal_id))
        connection.commit()
        colonia_id = cursor.lastrowid

        connection.commit()
        connection.close()

        return redirect(url_for('index'))
    else:
        return render_template('/add.html')
    return render_template('/add.html')

if __name__ == '__main__':
    app.run(debug=True)
