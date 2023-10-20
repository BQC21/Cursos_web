from flask import Flask, render_template, redirect, url_for, flash, request, session # importar librerias
from dao.DAOCursos import DAOCursos # para la base de datos definida
import os

app = Flask(__name__)
app.secret_key = "gyh6huj556htrjyliñ"
db = DAOCursos()

@app.route('/')
def inicio():
    return render_template('index.html')

########################################################################
############################# CRUD cursos ##############################
########################################################################

#### read operation

@app.route('/cursos')
def index():
    data = db.read(None)
    return render_template('cursos/index.html', data = data)

#### insert operation

@app.route('/cursos/add/')
def add():
    return render_template('/cursos/add.html')

@app.route('/cursos/addcurso', methods = ['POST', 'GET'])
def addcurso():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo curso creado")
        else:
            flash("ERROR, al crear curso")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

#### update operation

@app.route('/cursos/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('cursos/update.html', data = data)

@app.route('/cursos/updatecurso', methods = ['POST'])
def updatecurso():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

#### delete operation

@app.route('/cursos/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('cursos/delete.html', data = data)

@app.route('/cursos/deletecurso', methods = ['POST'])
def deletecurso():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('curso eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

########################################################################
########################################################################
########################################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=4000, host="0.0.0.0",debug=True)
