import pyodbc
import pandas as pd
from datetime import datetime
import fechastr

Dt_llamadas= [{'Mes':'',
             'Ventas':''
             }]
    

Dt_gestionAsesor=[
    {'Notas':'',
     'Ventas':''}
    ]

Dt_Usuarios=[
   {'NOMBRE':'',
    'APELLIDOS':'',
    'FECHA_NACIMIENTO':'',
    'edad':'',
    'ID_CARGO':'',
    'VENTAS':'',
}
    ]

Dt_CantLLAMADAS=[
   {'ID_USUARIO':'',
    'NOMBRE_APELLIDOS':'',
    'EMAL':'',
    'CARGO':'',
    'AÑO':'',
    'MES':'',
    'SALARIO':'',
    'CANTIDAD_DE_LLAMADAS':'',
}
    ]

Dt_Comision=[
   {'ID_USUARIO':'',
    'NOMBRE_APELLIDOS':'',
    'ID_CARGO':'',
    'MES':'',
    'AÑO':'',
    'SALARIO':'',
    'VENTAS':'',
    'COMISION':''
}
    ]

Dt_trigger=[
                {'ID_USUARIO':'',
                    'TELEFONO':'',
                    'FECHA':'',
                    'TURNO':'',
                    'NOTAS':'',
                    'ACTIVO':'',
                    'FECHA_CREACION':'',
                    'FECHA_BAJA':''
                }
                ]

Dt_Rpa= [{'Fecha_ejecucion':'',
             'Lauch_Bot':'',
             'Name_Bots':''
             }]



connection = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-14U34O5J\SQLEXPRESS;DATABASE=PRUEBA_DESARROLLO;Trusted_Connectio=yes;')
cursor = connection.cursor()
Qr1=cursor.execute("""
                        SELECT TOP(5) MONTH(FECHA) 'FECHA',COUNT(NOTAS) 'VENTAS'
                        FROM T_LLAMADA 
                        WHERE [NOTAS]='APROBADO' 
                        GROUP BY MONTH(FECHA) 
                        ORDER BY COUNT(NOTAS)  DESC
                        """) #PREGUNTA 1
for rows in Qr1:
   
   MesINT= fechastr.fechaint(mm=rows[0])
   Dt_llamadas.append({'Mes':MesINT,
                      'Ventas':rows[1]
                        })
cursor.close()


cursor = connection.cursor()
Qr2=cursor.execute("""
                        SELECT 
                        NOTAS, COUNT(NOTAS) 'VENTAS'
                        FROM T_LLAMADA
                        WHERE [NOTAS] <> 'APROBADO'
                        GROUP BY NOTAS
                    """) #PREGUNTA 2
for DtG in Qr2:
     Dt_gestionAsesor.append({
                        'Notas':DtG[0],
                        'Ventas':DtG[1]
                        })
cursor.close()   




cursor = connection.cursor()
Qr3=cursor.execute("""

                        /****** pregunta 3 ******/

                        SELECT NOMBRE 'NOMBRE' ,
                        APELLIDOS 'APELLIDO', 
                        FECHA_NACIMIENTO 'FECHA_NACIMIENTO', 
                        YEAR(FECHA_NACIMIENTO) 'EDAD',
                        ID_CARGO, 
                        COUNT(NOTAS) 'VENTAS' 
                        FROM [T_LLAMADA] CE INNER JOIN T_USUARIO da on CE.ID_USUARIO = da.ID_USUARIO
                        WHERE [NOTAS] = 'APROBADO'
                        GROUP BY ID_CARGO,APELLIDOS,NOMBRE,FECHA_NACIMIENTO,YEAR(FECHA_NACIMIENTO)
                        ORDER BY COUNT(NOTAS)  DESC
                        """) #PREGUNTA 3
año=2023
for USER in Qr3:
     Edad=2023-int(str(USER[2][0:4]))
     Dt_Usuarios.append(
                         {
                            
                            'NOMBRE':USER[0],
                            'APELLIDOS':USER[1],
                            'FECHA_NACIMIENTO':USER[2],
                            'edad':USER[2],
                            'ID_CARGO':USER[4],
                            'VENTAS':USER[5],
                           
                            } 
                           
                        )
cursor.close()



cursor = connection.cursor()
Qr4=cursor.execute("""
                       /****** pregunta 4  ******/

  WITH Dt_table AS (
  SELECT 
  ID_USUARIO, COUNT(NOTAS) 'VENTAS' 
  FROM [T_LLAMADA] 
  WHERE [NOTAS] = 'APROBADO' AND FECHA >= '01-06-2022'

  GROUP BY ID_USUARIO) 

   SELECT 
   da.ID_USUARIO 'ID_USUARIO',
   CONCAT(da.NOMBRE,' ',da.APELLIDOS) 'NOMBRE_APELLIDOS',
   EMAIL'EMAL',
   ca.NOMBRE 'CARGO',
   YEAR(FECHA) 'AÑO',
   MONTH(FECHA) 'MES',
   SALARIO 'SALARIO',
   COUNT(*) AS 'CANTIDAD DE LLAMADAS'
   FROM [T_LLAMADA] CE 
   INNER JOIN T_USUARIO da on CE.ID_USUARIO = da.ID_USUARIO 
   INNER JOIN T_CARGO ca on da.ID_CARGO =ca.ID_CARGO
   INNER JOIN T_SALARIO salario on  da.ID_CARGO =salario.ID_CARGO
   WHERE CE.ID_USUARIO = (SELECT ID_USUARIO from Dt_table where VENTAS =  (SELECT MAX(VENTAS) FROM Dt_table))
   GROUP BY 
   da.ID_USUARIO,
   CONCAT(da.NOMBRE,' ',da.APELLIDOS) ,
   EMAIL,
   ca.NOMBRE,
   YEAR(FECHA),
   MONTH(FECHA),
   SALARIO 
                        """) #PREGUNTA 4
for LLAMADAS in Qr4:
     fr=int(LLAMADAS[5])
     MesString0= fechastr.fechaint(mm=fr)
     Dt_CantLLAMADAS.append(
                          {'ID_USUARIO':LLAMADAS[0],
                            'NOMBRE_APELLIDOS':LLAMADAS[1],
                            'EMAL':LLAMADAS[2],
                            'CARGO':LLAMADAS[3],
                            'AÑO':LLAMADAS[4],
                            'MES':MesString0,
                            'SALARIO':LLAMADAS[6],
                            'CANTIDAD_DE_LLAMADAS':LLAMADAS[7],
}
                           
                        )
cursor.close()


cursor = connection.cursor()
Qr5=cursor.execute("""
                       SELECT  llamada.ID_USUARIO,
		  CONCAT(usu.NOMBRE,' ',usu.APELLIDOS) 'NOMBRE_APELLIDOS',
	      usu.ID_CARGO,
		  MONTH(llamada.FECHA_CREACION) 'MES',
		  YEAR(llamada.FECHA_CREACION) 'AÑO',
		  salary.SALARIO,
		  COUNT(*) AS 'VENTAS'	        
   FROM T_LLAMADA llamada
   INNER JOIN T_USUARIO usu on llamada.ID_USUARIO =usu.ID_USUARIO
   INNER JOIN  T_SALARIO salary on usu.ID_CARGO = salary.ID_CARGO
   WHERE [NOTAS] = 'APROBADO'
   AND MONTH(llamada.FECHA_CREACION) = 8 
   AND YEAR(llamada.FECHA_CREACION) = 2023
   GROUP BY
          llamada.ID_USUARIO,
		  CONCAT(usu.NOMBRE,' ',usu.APELLIDOS) ,
	      usu.ID_CARGO,
		  MONTH(llamada.FECHA_CREACION) ,
		  YEAR(llamada.FECHA_CREACION) , 
          salary.SALARIO
                        """) #PREGUNTA 5
for COMISION in Qr5:    
     Dt_Comision.append(
                       
                        {   'ID_USUARIO':COMISION[0],
                            'NOMBRE_APELLIDOS':COMISION[1],
                            'ID_CARGO':COMISION[2],
                            'MES':COMISION[3],
                            'AÑO':COMISION[4],
                            'SALARIO':COMISION[5],
                            'VENTAS':COMISION[6],
                            'COMISION':((COMISION[6]*(0.01))*COMISION[5])+COMISION[5]
}
                           
                        )
    
cursor.close()


       
cursor = connection.cursor()
Qr6=cursor.execute(""" SELECT TOP (1000) [FechaEjecucion]
                        ,[lauchbots]
                        ,[Name_Bots]
                        FROM [PRUEBA_DESARROLLO].[dbo].[T_RPA]  """) 
for RPA in Qr6:

     Dt_Rpa.append(
      {'Fecha_ejecucion':RPA[0],
       'Lauch_Bot':RPA[1],
        'Name_Bots':RPA[2]
                        }
                )
     
cursor.close()





df5=pd.DataFrame(Dt_llamadas)
print("""
•	Top 5 de mayor a menor de las cantidades
 de llamadas aprobadas por mes
 """)
respuesta_1=df5
print(respuesta_1)



print("""
•    Cantidad de llamadas por estados 
que no hayan sido gestionadas por asesores
""")
df6=pd.DataFrame(Dt_gestionAsesor)
respuesta_2=df6
print(respuesta_2)


  
print("""
•	Nombre, apellidos y edad para el mejor
    vendedor del año
""")
df7=pd.DataFrame(Dt_Usuarios)
respuesta_3=df7
print(respuesta_3)


print("""•	Cantidad de llamadas realizadas por cada mes a
 partir de 01/06/2022 para el mejor vendedor del año,
 con el siguiente encabezado: ID_USUARIO, NOMBRE_APELLIDOS,
 EMAL, CARGO, SALARIO, MES, CANTIDAD DE LLAMADAS""")

df8=pd.DataFrame(Dt_CantLLAMADAS)
respuesta_4=df8
print(respuesta_4)



print("""
•	Generar el salario a pagar a cada asesor para el mes de agosto,
 donde cada llamada aprobada tiene una bonificación del 
 0.01% sobre su sueldo básico.
 """)

df9=pd.DataFrame(Dt_Comision)
respuesta_5=df9
print(respuesta_5)





def trigguer (ID_USUARIO
              ,TELEFONO
              ,FECHA
              ,TURNO
              ,NOTAS
              ,ACTIVO
              ,FECHA_CREACION
              ,FECHA_BAJA
              ):

     Dt_trigger.append(
                        ID_USUARIO=ID_USUARIO,
                        TELEFONO=TELEFONO,
                        FECHA=FECHA,
                        TURNO=TURNO,
                        NOTAS=NOTAS,
                        ACTIVO=ACTIVO,
                        FECHA_CREACION=FECHA_CREACION,
                        FECHA_BAJA=FECHA_BAJA
                     
     )
     for w in Dt_trigger:
         captura=w  
         return captura
     


           
    
     



ejemplo=("ID_USUARIO","TELEFONO","FECHA","TURNO","NOTAS" ,"ACTIVO" ,"FECHA_CREACION","FECHA_BAJA")
print(ejemplo)

