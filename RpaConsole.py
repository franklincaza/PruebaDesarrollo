from RPA.Browser.Selenium import Selenium
from RPA.Windows import Windows
import time



def consolaRpa (REQ):

        inicio="""
                                ************************Consola RPA ************************************
                                Que robot desea ejecutar ?  
                                __________________________________________________________________________________    

                                1.generar archivo txt.   
                                2.Cancelar.
                                __________________________________________________________________________________                                                    
                                Escribe tu repuesta = """
       
        print(inicio) 

        

        if REQ == 1: 
                respuesta = REQ
                import Rpa   
   
        if  REQ == 2:
                    print("""
                                ************************Consola RPA ***********************************************
                                ___________________________________________________________________________________
                                cerrando consola RPA,  si quieres volver a ejecutar el servidor , o espera 5 minutos
                                para que se ejecute automaticamente. 
                                ___________________________________________________________________________________ """)
        if REQ == None:
           respuesta = int(input())

           if respuesta==1:
                    import Rpa
           elif respuesta==2:
                     print("""
                                ************************Consola RPA ***********************************************
                                ___________________________________________________________________________________
                                cerrando consola RPA,  si quieres volver a ejecutar el servidor , o espera 5 minutos
                                para que se ejecute automaticamente. 
                                ___________________________________________________________________________________ """)
        


        return 
        





