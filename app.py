from flask import Flask ,request,jsonify,render_template,url_for,Request
import models





app = Flask(__name__)

app.config.from_mapping(
       DEBUG = False,
       SECRET_KEY = 'devtod')

@app.route("/")

def GETINDEX():
    
    return render_template('Index.html')
    url_for("/")


@app.route("/BASE_DE_DATOS")
def GETllamadas():       
        dato=  models.Dt_llamadas
        gestor=models.Dt_gestionAsesor
        vendedor=models.Dt_Usuarios
        venta=models.Dt_CantLLAMADAS
        Comision=models.Dt_Comision

        return render_template('Reportes.html',dato=dato
                                              ,gestor=gestor
                                              ,vendedor=vendedor
                                              ,venta=venta
                                              ,Comision=Comision
                                              )

@app.route("/RPA")

def CallRPA():
     return render_template('RPA.html')   


@app.route("/lauchRPA", methods=[ 'POST','GET' ])
@app.route("/lauchRPA?", methods=[ 'GET' ])
def LAUCHRPA():
      
      
      import RpaConsole
      RpaConsole.consolaRpa(1)
      rpa=models.Dt_Rpa
      
     
      
      return render_template('RPAComfir.html',rpa=rpa) 

  
    



     
@app.route("/GITLAB", methods=['GET' , 'POST'])
def DocumentAPI():   
     return render_template('Documentacion.html')
     

if __name__ == '__main__':
    app.run(debug=True , host="0.0.0.0")
