from flask import  Flask
from flask import render_template, request, redirect, url_for, flash, jsonify
from flaskext.mysql import MySQL     

app=Flask(__name__) 


#CONFIGURACION MYSQL
mysql=MySQL()  
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root' 
app.config['MYSQL_DATABASE_PASSWORD']='' 
app.config['MYSQL_DATABASE_DB']='arcor'  
mysql.init_app(app)

#SESION
app.secret_key = 'mysecretkey'


#RUTAS
#Inicio
@app.route('/')                             
def Index():
    sql="SELECT * FROM `arcor`.`productos` ORDER BY id DESC LIMIT 10;"
    conn=mysql.connect()             
    cursor=conn.cursor()             
    cursor.execute(sql)              
    productos=cursor.fetchall()
    
         
    conn.commit()
    return render_template('productos/index.html',productos=productos) 
 

@app.route('/new')            
def Add():
    return render_template('productos/new.html')

@app.route('/results', methods=["POST", "GET"])
def Search():
    if request.method == 'POST':
        txtSearch = request.form['txtSearch']
        
        print(txtSearch)
        conn=mysql.connect()        
        cursor=conn.cursor()
        sql="SELECT * FROM `arcor`.`productos` WHERE nombre LIKE '%{}%' OR marca LIKE '%{}%' OR rnpa LIKE '%{}%' or categoria LIKE '%{}%' ORDER BY categoria LIMIT 10".format(txtSearch,txtSearch,txtSearch,txtSearch)
    #   conn=mysql.connect()             
    #   cursor=conn.cursor()             
        cursor.execute(sql)           
        productos=cursor.fetchall()
        #flash('Resultados de '+ txtSearch) 
    return render_template('productos/results.html',productos=productos)

@app.route('/login')
def Login():

    return redirect(url_for('Index'))

@app.route('/edit/<int:id>')
def Edit(id): 
    sql="SELECT * FROM `arcor`.`productos` WHERE id=%s;"
    conn=mysql.connect()        
    cursor=conn.cursor()           
    cursor.execute(sql,(id))            
    productos=cursor.fetchall()
    conn.commit()
    print(productos)
    return render_template('productos/edit.html',productos=productos)


@app.route('/delete/<int:id>')
def Delete(id):
    sql="DELETE  FROM `arcor`.`productos` WHERE  id=%s;"
    conn=mysql.connect()         
    cursor=conn.cursor()        
        
    cursor.execute(sql,(id))     
    conn.commit()
    flash('El producto ha sido eliminado')
    return redirect('/')   


@app.route('/create', methods=['POST'])    
def  Create():    
    if request.method == 'POST':
        rnpa=request.form['txtRNPA']
        nombre=request.form['txtNombre'] 
        marca=request.form['txtMarca'] 
        categoria=request.form['txtCategoria']     
        
        sql="INSERT INTO productos (rnpa, nombre, marca,categoria) VALUES (%s,%s,%s,%s)"
        datos=(rnpa, nombre, marca, categoria)

        conn=mysql.connect()         
        cursor=conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
    
        flash('Producto ingresado existosamente')
        return redirect(url_for('Index'))

@app.route('/update',  methods=['POST'])     
def Update():                             
    rnpa=request.form['txtRNPA']
    nombre=request.form['txtNombre'] 
    marca=request.form['txtMarca'] 
    categoria=request.form['txtCategoria']
    id=request.form['txtId']

    sql="UPDATE `arcor`.`productos` SET  `rnpa`=%s,`nombre`=%s,`marca`=%s,`categoria`=%s WHERE id=%s"
    datos=(rnpa,nombre,marca,categoria, id)

    conn=mysql.connect()         
    cursor=conn.cursor()  

    cursor.execute(sql,datos)  
    conn.commit()
    flash('El producto fue modificado con éxito')
    return redirect('/') 




#**************************
if __name__=='__main__':  
    app.run(debug=True)

