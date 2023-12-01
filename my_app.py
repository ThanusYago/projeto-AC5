from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

 
# Rutas estáticas (archivos CSS, imágenes, etc.)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/aplication')
def application():
    return render_template('aplication.html')

@app.route('/ingresso')
def ingresso():
    return render_template('ingresso.html')

@app.route('/mat')
def mat():
    return render_template('mat.html')

@app.route('/Qiskit')
def qiskit():
    return render_template('Qiskit.html')

if __name__ == '__main__':
    app.run(debug=True)