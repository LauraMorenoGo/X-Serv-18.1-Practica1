#!/usr/bin/python3

import webapp

#PRÁCTICA 1

#diccURL = {}
#diccURLacort = {}  
contents = {}


formulario = """
<form action="" method="POST">
  Introduzca la URL que desea acortar:<br>
  <input type="text" name="url" value="URL a acortar"><br>
  <input type="submit" value="Enviar">
  <a href = ""><>
</form> 
"""

class contentApp(webapp.webApp):
    def parse(self, request):
        return (request.split()[0], request.split()[1], request)
        
    def process(self, parsedRequest):   #Recurso de la petición, es una tupla metodo, 
                                        #recurso de la peticion
        
        metodo, recurso, peticion = parsedRequest
        
                            
        if metodo == "POST":
            contents[recurso] = peticion.split('\r\n\r\n', 1)[1].split('=')[1]
         
            
            
        try:
            print(contents)
            print(recurso)
            return("200 OK", contents[recurso])
        except KeyError:
            return("200 OK", "<html>ACORTADOR DE URLs,<br>" + formulario + '</html>')
           
if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
