from utils import *
from models import *
from app import app
from flask import session, request, render_template, url_for, redirect
from datetime import datetime
import json

@app.route("/login", methods=['POST'])
def loginAlumno():
        alumno = Alumno.query.filter_by(usuarioAlumno=request.form['uname'], contrasena=request.form['psw']).first()
        if alumno:
                session['AUTH'] = 'Logged'
                session['USER'] = request.form['uname']
                return "Login Successful"
        else:
                return "Login Failed"

@app.route("/getInfo", methods=['GET'])
def getInfo():
        if session.get('AUTH') != None and session['AUTH'] == 'Logged':
                alumnos = Alumno.query.all()
                response = {}
                lista = []
                for alumno in alumnos:
                    temp = {}
                    temp['id'] = alumno.idAlumno
                    temp['user'] = alumno.usuarioAlumno
                    temp['password'] = alumno.contrasena
                    temp['name'] = alumno.nombre
                    temp['career'] = alumno.carrera
                    lista.append(temp)
                response['students'] = lista
                response['requester'] = session['USER']
                response['time of transaction'] = str(datetime.now())
                return json.dumps(response)
        else:
            return "Not logged in"
