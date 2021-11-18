# __PÁGINA PARA RESERVAR NAVES GALÁCTICAS__

#### En este proyecto lo que hemos hecho es una página que nos permite poder hacer una o más reservas de naves.
#### Las naves se dividirán en diferentes Secciones: Ligeras, Medianas, Grandes.
#### En cada sección habrá tres diferentes naves con diferentes especificaciones.

#



## __INSTRUCCIONES PARA TENER INSTALADO EL ENTORNO VIRTUAL, CON TODAS LAS DEPENDENCIAS NECESARIAS__

##  WINDOWS
#
- Crea un directorio
##
    mkdir Starship-Business

![Crea un directorio](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/windows/crear_carpeta_windows.png)

##


#
- sitúate encima
##
    cd Starship-Business

![sitúate encima](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/windows/situate_encima_windows.png)

#

- Clonar el repositorio:  
 ##
    git clone https://github.com/OualidZM/Ricksy-business.gitofofor

![Clonar repositorio](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/windows/git_clone_windows.png)    
#

- Instalamos el **entorno Virtual** en nuestro ordenador:  
##
    pip install virtualenv

![Instalar entorno Virtual](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/windows/instalacion_env.png)  

# 

- Creamos el **entorno Virtual**:       
##
     C:\Users\q\Starship-Business\Ricksy-business>python -m venv env

![crear entorno Virtual](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/windows/creacion_env.png)  

#

- Iniciamos el **entorno Virtual**:       
##
     C:\Users\q\Starship-Business\Ricksy-business>env\Scripts\activate

![iniciamos entorno Virtual](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/windows/activacion_env.png)  

#
- Ahora instalamos todas las dependencias:
##

    (env) C:\Users\q\Starship-Business\Ricksy-business>pip install -r requirements.txt


![dependencias](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/windows/requirement_windows.png)  


# Linux

- Crea un directorio
##
    mkdir Starship-Business




![Crea un directorio](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/linux/Crear_carpeta_linux.png)
#

- Sitúate encima
##
    cd Starship-Business

![Sitúate encima](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/linux/entramos_en_carpeta.png)
#
- Clonar repositorio:  
##  
    git clone https://github.com/OualidZM/Ricksy-business.git

![Clonar repositorio](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/linux/git_clone_linux.png)

#


- Instalamos pip en nuestro ordenador:  
##
    $ sudo apt install python3-pip


![pip](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/linux/instalacion-pip.png) 

#



 
- Instalamos el **entorno Virtual** en nuestro ordenador: 
##
    $ sudo apt-get install python3-venv -y

![entorno Virtual](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/linux/download_venv.png)

#




- Creamos un  **entorno Virtual** en nuestro ordenador:  
##
    python3 -m venv venv

![Crear entorno Virtual](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/linux/crear_venv_linux.png)

#
    
    

- Iniciamos el **entorno Virtual**:       
##
    $ source venv/bin/activate

![Iniciar entorno Virtual](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/linux/venv_linux_iniciar.png)

#

- Ahora instalamos todas las dependencias:
##
    (venv) $ pip3 install -r requirements.txt

![dependencias](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/linux/requirements_linux.png)
#




# __Funcionamiento del programa__

    El programa se divide en dos partes,
    el Crawler y el Scraper,
    El Crawler se dedicará a recoger todos
    los links que hay en la página y los 
    devolvera en una lista, seguidamente
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
    al MongoDB en forma de diccionario.

#
# __Ejecución__

- Nos Situamos en la carpeta desde la terminal si no lo estamos    
##
    cd Starship-Business
    cd Ricksy-business

![cd directorio](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/Ejecuci%C3%B3n/dirrecion_absoluta.png)


#

- Ejecutamos el archivo **app.py** 
##
    python app.py // python3 app.py

![Ejecutamos app.py](https://github.com/OualidZM/Ricksy-business/blob/master/markdown_pictures/Ejecuci%C3%B3n/app.png)


#




# __Diagrama de Componentes__

![Diagrama de Componentes](https://github.com/OualidZM/Ricksy-business/blob/master/diagrama_de_componentes/diagrama_de_componentes.png)
# __Clockify__

![Clockify](https://github.com/OualidZM/Ricksy-business/blob/master/clockify/clockify.png)






# __Herramientas Utilizadas__

    vscode
    gimp
    Clockify


# __Conclusion__

    Para concluir, pensamos que el proyecto fue
    bastante interesante y aprendimos demasiado,
    pero una cosa mala es que tuvimos demasiados
    contratiempos que nos perjudicaron al final.
    Nos sirvió este proyecto para darnos cuenta 
    de problemas mencionados anteriormente, que
    nos podrán servir para mejorar en el próximo.
    
#
    
# __Autores__

### Oualid Zaaj  y Toni Caimari







