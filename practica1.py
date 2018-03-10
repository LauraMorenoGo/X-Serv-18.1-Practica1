#!/usr/bin/python3

import webapp

#PRÁCTICA 1


def Formulario():
    """
    <form action="" method="POST">
      Introduzca la URL que desea acortar:<br>
      <input type="text" name="url" value="URL a acortar"><br>
      <input type="submit" value="Enviar">
      
    </form> 
    """
    return formulario
    
def TablaURL(url, urlacort):    #Lo hacemos así para poder pasarle la url y su correspondiente url acortada.
    
    "<table><tr><td>URL original</td><td>URL acortada</td></tr><tr><td>" + url + "</td><td>" + urlacort + "</td></tr></table>"
    return tabla

class acortURLApp(webapp.webApp):
    
    urls = ""
    urlsacortadas = ""
    urlacort = 0    #Inicializo a 0 el número que voy a asignar a cada URL acortada
    dicURL = {}
    dicURLacort = {}

    def parse(self, request):   #Vamos a necesitar: metodo, recurso y cuerpo
        
        metodo = request.split()[0]         #Nos devuelve un GET, POST
        recurso = request.split()[1][1:]    #Nos va a devolver la URL acortada(Sólo el número por eso ponemos 1:)
        if metodo == "POST":                #Hacemos esto aquí porque sino nos da un error de out of range si solo sacamos el cuerpo        
            cuerpo = request.split('\r\n\r\n', 1)[1].split('=')[1]      #Nos va a devolver lo que haya en el body
            if len(cuerpo.split("%3A%2F%2F")) == 1:
                url = "http://" + cuerpo
            else:
                url = cuerpo.replace("%3A%2F%2F", "://")
        else:
            cuerpo = ""
            url = cuerpo
            
        print ("***URL***" + url + "***")
    
        return (metodo, recurso, url)
        
        
    def process(self, parsedRequest):
    
        metodo, recurso, url = parsedRequest
        
        if parsedRequest:
            if metodo == "GET":
                if recurso == "":
                    tabla = Tabla()
                    return("200 OK", "<html>ACORTADOR DE URLs<br>" + Formulario() + tabla + '</html>')
                
            
        else:
            return("400 Resource nor found!", "<html><body><h1>Error 404</h1></body></html>")
        
        
            
            
        
           
if __name__ == "__main__":
    testWebApp = acortURLApp("localhost", 1234)
