

def fecha(mm):
    if mm == "01":
            resultado="enero"
    elif mm== "02":
            resultado="febrero"
    elif mm=="03":
            resultado="marzo"
    elif mm=="04":
            resultado="abril"
    elif mm=="05":
            resultado="mayo"
    elif mm== "06":
            resultado="junio"
    elif mm=="07":
            resultado="julio"
    elif mm=="08":
            resultado="agosto"
    elif mm=="09":
            resultado="septiembre"
    elif mm=="10":
            resultado="octubre"
    elif mm=="11":
            resultado="noviembre" 
    elif mm=="12":
            resultado="diciembre"  







    return resultado


def fechaint(mm):
    if mm == 1:
            resultado="enero"
    elif mm== 2:
            resultado="febrero"
    elif mm==3:
            resultado="marzo"
    elif mm==4:
            resultado="abril"
    elif mm==5:
            resultado="mayo"
    elif mm== 6:
            resultado="junio"
    elif mm==7:
            resultado="julio"
    elif mm==8:
            resultado="agosto"
    elif mm==9:
            resultado="septiembre"
    elif mm==10:
            resultado="octubre"
    elif mm==11:
            resultado="noviembre" 
    elif mm==12:
            resultado="diciembre"  







    return resultado


def TablaHtml(Inhtml):
        Inhtml=Inhtml
        mensaje = open("templates/"+ Inhtml  ,"r")
        outHtml= mensaje.read()
        outHtml.replace("[@dato]")
        outHtml.format("hola")





#ejemplo=TablaHtml("Reporte_llamadas.html","hola")
#print(ejemplo)