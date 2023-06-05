from RPA.Browser.Selenium import Selenium
from RPA.Windows import Windows
import pyodbc
import time


                    
library = Windows()
browser = Selenium()
                    
browser.open_available_browser("http://192.168.1.5:5000/BASE_DE_DATOS",)
                
time.sleep(5)
browser.maximize_browser_window()
                

Captura=browser.get_text('//*[@id="Pregunta_1"]')
f = open ('Reporte TOP 5 por mes.txt','w')
f.write(Captura)
f.close()
print("Reporte TOP 5 por mes.txt")
browser.execute_javascript("window.scrollTo(0,500)")

                 
                    
time.sleep(2)

Captura=browser.get_text('//*[@id="Pregunta_2"]')
f = open ('Reporte por asesores.txt','w')
f.write(Captura)
f.close()
print("se genera archivo Reporte por asesores.txt")
browser.execute_javascript("window.scrollTo(0,1000)")
time.sleep(5)
             
Captura=browser.get_text('//*[@id="Pregunta_3"]')
f = open ('Reporte vendedor del año.txt','w')
f.write(Captura)
f.close()
print("Reporte vendedor del año.txt")
browser.execute_javascript("window.scrollTo(0,900)")
time.sleep(5)
                   
Captura=browser.get_text('//*[@id="Pregunta_4"]')
f = open ('Reporte vendedor del a partir de 01062022.txt','w')
f.write(Captura)
f.close()
print("Reporte vendedor del año.txt")
browser.execute_javascript("window.scrollTo(0,900)")
                    
                    
browser.execute_javascript("window.scrollTo(0,2000)")
time.sleep(2)
                   
Captura=browser.get_text('//*[@id="Pregunta_5"]')
f = open ('Reporte de comision por vendedor.txt','w')
f.write(Captura)
f.close()
print("Reporte de comision por vendedor.txt")
browser.close_all_browsers() 

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-14U34O5J\SQLEXPRESS;DATABASE=PRUEBA_DESARROLLO;Trusted_Connectio=yes;')
cursor = connection.cursor()
cursor.execute("""
        INSERT INTO T_RPA 
        VALUES (GETDATE(), 1,'Bot de Reporte TXT');        
        """) 
cursor.commit()
cursor.close()                           
   


       