# WhyMex
Un proyecto para la recolección de datos sobre lá ubicación de problemas medioambientales en México. 
Cuyo **objetivo** principal es recolectar datos para saber de la existencia de los problemas y a partir de ahí
profundizar en dichos problemas y pensar en soluciones a estos problemas aprovechando los datos disponibles. 

[Ver página del proyecto](http://whymex.pythonanywhere.com/inicio/)

**NOTA**
> Actualmente el proyecto se encuentra alojado en pythonanywhere el cual solo nos permite almacenar 5 MB en la 
> base de datos proporcionada, por lo que se estará revisando periódicamente para no pasar este limite y cuando este por 
> alcanzarse, los datos serán descargados de la base de datos para ser respaldados aquí. Una vez respaldados aquí, se eliminaran 
> de la base de datos para dar paso a los nuevos datos. Esto mientras se encuentra un mejor hosting. 

# **Indice**
<ul>
  <li><a href="preguntas">Preguntas relevantes</a></li>
  <li><a href="#spanish">Información sobre el proyecto en español</a></li>
  <li><a href="#english">Información sobre el proyecto en inglés</a></li>
  <li><a href="#licen">Licencia del proyecto</a></li>
  <li><a href="#aut">Autores y colaboradores</a></li>
</ul>

<center><h1><strong><a name = "preguntas">Preguntas relevantes</a></strong></h1></center>

## ¿Qué es?

> Un sistema de recolección de datos no automatizado de la ubicación de problemas detectados por los mismos mexicanos.

## ¿Para quién es?

> El sistema es de código abierto, por lo que puede ser usado por cualquier persona o entidad. Yo inicié el proyecto con la finalidad de darle “voz” a todos los mexicanos. Hay problemas locales que parecen poco relevantes pero es justo en el inicio del problema donde se debería de solucionarlo antes de que sea mayor y más difícil de solucionar. 

## ¿Cuál es la idea detrás? 

> En un inicio yo quise plantear una solución a un problema sobre basura en la ciudad donde vivo. Dicho problema yo logre verlo porque suelo salir a correr y a veces hago nueva ruta y fue así como lo encontré entonces en lugar de encontrar una solución a ese problema se me ocurrió construir un sistema para que todas las personas puedan ubicar problemas de su localidad y a partir de ello, poder pasar a la parte de pensar en soluciones. 

## ¿Cómo planeas escalar el proyecto?
 
> Voy a acudir con organizaciones dedicadas al medio ambiente con la finalidad de obtener más datos para la base de datos del proyecto y/o trabajar en dicha institución y subir dicho sistema a sus servidores. 

 
 
<center><h1><strong><a name = "spanish">Información en español</a></strong></h1></center>

## Dependencias 
``` 
  Python3 Django
```
## Modo de uso

```
  python3 -m venv .whymexEnv
  source .whymexEnv/bin/activate
  pip install -r requirements.txt
```
> Por favor, antes de de ejecutar *pip install -r requirements.txt* lee el archivo **ReadBeforeStart.txt**
> Ahí podrás ver con más detalle los comandos *pip install* que fueron ejecutados.
> La razón de ello es que si ejecutas *pip install -r requirements.txt* instalará uno a uno, sin embargo, algunos paquetes se
> instalaron sin si quiera pedirlo. Así que te recomendamos leer **ReadBeforeStart.txt**. 


Una vez que has clonado el proyecto, corrobora si la rama de Pruebas también se ha bajado junto al repositorio, para ello solo ejecuta: 
> git branch 
y deberás obtener la rama main y la rama Pruebas. Si esta última no se bajo junto con el repositorio, te recomiendo que la crees o que la bajes de aquí 
mismo, ya que la rama de Pruebas tiene la configuración por defecto. Misma que encontraras en el archivo **WhyMex/local_settings.py**.

La rama de Pruebas tiene por finalidad que hagas las pruebas en tu computadora de manera local, una vez que han sido probadas y funcionan bien. 
Entonces puedes proceder a hacer un merge con la rama principal para efectuar un pull request al proyecto. La rama main por su parte ya esta 
configurada de la manera que el servidor donde esta alojada la página lo requiere. 

Dicho lo anterior, continua con los comandos en la terminal para poder abrir el proyecto de manera local:

```
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
```

 
<center><h1><strong><a name = "english">Information in English</a></strong></h1></center>

## Dependencies
``` 
  Python3 Django
```
## Usage mode
```
  python3 -m venv .whymexEnv
  source .whymexEnv/bin/activate
  pip install -r requirements.txt
```

> Please, before to execute *pip install -r requirements.txt* read the file **ReadBeforeStart.txt**
> There you can get more details about the commands *pip install* that we executed.
> The reason is because, when you execute *pip install -r requirements.txt* it will install one by one, however, some packages
> were installed without our desire. So, we recommend read the file **ReadBeforeStart.txt**. 


Once you have cloned the project, check if the Test branch has also been downloaded along with the repository, to do this just run:  
> git branch 
and you should get the main branch and the Tests branch. If the latter was not downloaded along with the repository,
I recommend you to create it or download it from here, since the Tests branch has the default configuration.
branch has the default configuration, which you will find in the **Testing branch. You will find it in the **WhyMex/local_settings.py** file.

The Tests branch is intended for you to run the tests on your computer locally, once they have been tested and are working well. 
Then you can proceed to make a merge with the main branch to make a pull request to the project. The main branch is already 
configured the way the server where the page is hosted requires it.



Having said that, continue with the commands in the terminal to open the project locally:

```
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
```


<center><h1><strong><a name = "licen">Licencia del proyecto </a></strong></h1></center>

### Licencia / License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

<center><h1><strong><a name = "aut">Autores y Colaboradores</a></strong></h1></center>

### Autores / Authors
* José Vidal Cardona Rosas / ladivcr@comunidad.unam.mx / [Github](https://github.com/Ladivcr/)

### Colaboradores / Collaborators
* Brian Kalid Garcia Olivo / briankalid2000@gmail.com / [Github](https://github.com/briankalid/)
