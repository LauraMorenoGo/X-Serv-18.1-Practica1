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
    numurlacort = 0    #Inicializo a 0 el número que voy a asignar a cada URL acortada
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
            
        print ("URL ==" + url)
    
        return (metodo, recurso, url)
        
        
    def process(self, parsedRequest):
    
        metodo, recurso, url = parsedRequest
        
        if parsedRequest:
            if metodo == "GET":
                if recurso == "":
                    if self.numurlacort > 0:
                        tabla = Tabla(self.urls, self.urlsacortadas)
                        returnCode = "200 OK"
                        htmlAnswer = "<html>ACORTADOR DE URLs<br>" + Formulario() + tabla + "</html>"
                    else:
                        returnCode = "200 OK"
                        htmlAnswer = "<html>ACORTADOR DE URLs<br>" + Formulario() + "</html>"
                        
                else:
                    if (int(recurso) < self.numurlacort):
                        nuevaurl = self.dicURLacort[int(recurso)]
                        returnCode = "307 REDIRECT"
                        htmlAnswer = "<html><body><h1>Redirigiendo...</h1><meta http-equiv='Refresh' content='0; url=" + str(nuevaurl) +"'></body></html>"

                    else:
                        returnCode = "400 Resource not found!"
                        htmlAnswer = "<html><body><h1>Error 404</h1></body></html>"
                    
                        
            if metodo == "POST":
                if url == "URL+a+acortar":  #Esto es lo que pone en el formulario en el hueco para poner la url, si recibimos 
                                            #esto significaria que no hemos enviado nada
                    returnCode = "400 Resource not found!"
                    htmlAnswer = "<html><body><h1>Introduce una URL</h1></body></html>"
                
                if url not in self.dicURL.keys():
				    self.dicURLacort[self.numurlacort] = url
				    self.dicURL[url] = self.numurlacort
				    self.urls += "<p>" + str(url) + "</p>"
				    self.urlsacortadas += "<p>http://localhost:1234/" + str(self.numurlacort) + "</p>"
				    self.numurlacort = self.numurlacort + 1                  
				
				urlacort = "http://localhost:1234/" + str(self.numurlacort - 1)
			    enlace = "<p><h4><a href=" + url + ">Url" + str(url) + "</a></h4></p><p><h4><a href=" + urlacort + ">Url acortada" + str(urlShorted) + "</a></h4></p>"
			    + "<p><a href='http://localhost:1234/'>Volver al formulario</a></p>"
			    returnCode= "200 OK!"
			    htmlAnswer = '<html><body style="background:#5C0349">' + enlaces + "</body></html>"
				    
			return(returnCode, htmlAnswer)
            
        else:
            return("400 Resource not found!", "<html><body><h1>Error 404</h1></body></html>")
        
        
            
            
        
           
if __name__ == "__main__":
    testWebApp = acortURLApp("localhost", 1234)
