# __Página para reservar naves__

#### En este proyecto lo que hemos hecho es una página que nos permite poder hacer una o más reservas de naves.
#### La sección de naves se dividirá en diferentes Secciones: Ligeras, Medianas, Grandes.
#### En cada sección habrá tres diferentes naves con diferentes especificaciones.

#



## __INSTRUCCIONES PARA TENER INSTALADO EL ENTORNO VIRTUAL, CON TODAS LAS DEPENDENCIAS NECESARIAS__

##  WINDOWS
#
- Crea un directorio y sitúate encima
##
    mkdir Projecta
    cd Projecta
#
- Clonar el repositorio:  
 ##
    git clone https://github.com/OualidZM/Ricksy-business.git
#

- Instalamos **entorno Virtual** en nuestro ordenador:  
##
    pip install virtualenv

# 

- Iniciamos el **entorno Virtual**:       
##
     C:\Users\q\Desktop\Projecta\Ricksy-business>env\Scripts\activate
#
- Ahora instalamos todas las dependencias:
##

    (env) C:\Users\q\Desktop\project\Ricksy-business>pip install -r requirements.txt



# Linux

- Crea un directorio y sitúate encima
##
    mkdir Projecta
    cd Projecta

#
- Clonar repositorio:  
##  
    git clone https://github.com/OualidZM/Ricksy-business.git
#


- Instalamos **entorno Virtual** en nuestro ordenador:  
#
    $ sudo apt-get install python3.6-venv

#

    
    

- Iniciamos el **entorno Virtual**:       
##
    $ python3.6 -m venv venv
    $ source venv/bin/activate

#

- Ahora instalamos todas las dependencias:
##
    (venv) $ pip3 install -r requirements.txt
#




# __Funcionamiento del programa__

    El programa se divide en dos partes,
    el Crawler y el Scraper,
    El Crawler se dedicará a recoger todos
    los links que hay en la página y los 
    devolvera en un diccionario, seguidamente
    al obtener todos los links podremos utilizar
    el scrapper para poder sacar de cada link la 
    información que a nosotros nos sirva, en este 
    caso a nosotros la información que nos importa
    son las especificaciones de la nave ligera, la 
    nave normal y la nave grande, para eso lo que 
    tenemos que hacer, es hacer un filtro que solo
    coja los tres link: ligera, mediana, grande.
    De cada uno devolverá los valores sin los tags
    del html "<>" ni nada por el estilo, solo el
    texto, y finalmente esa información la subiremos
    al MongoDB

#
# __Ejecución__

- Nos Situamos en la carpeta desde la terminal       
##
    cd projecta
    cd Ricksy-business

#

- Ejecutamos el archivo **app.py**       
##
    python app.py // python3 app.py



#


# __Conclusion__

    Para concluir, pensamos que el proyecto fue
    bastante interesante y aprendimos demasiado,
    pero una cosa mala es que tuvimos demasiados
    contratiempos que nos perjudicaron al final.
    Nos sirvió este proyecto para darnos cuenta 
    de problemas mencionados anteriormente, que
    nos podrán servir para mejorar en el próximo.
    
# __Autores__

### Oualid Zaaj  y Toni Caimari







