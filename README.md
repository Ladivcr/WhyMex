# WhyMex
Un proyecto para la recolección de datos sobre los lugares con problemas medioambientales. 

Indice
<ul>
  <li><a href="#spanish">Información sobre el proyecto en español</a></li>
  <li><a href="#english">Información sobre el proyecto en inglés</a></li>
</ul>
 
<center><h1><strong><a name = "spanish">Información en español</a></strong></h1></center>

# Dependencias 
``` 
  Python3 Django
```
# Modo de uso

```
  python3 -m venv .env
  source .env/bin/activate
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

# Dependencies
``` 
  Python3 Django
```
# Usage mode
```
  python3 -m venv .env
  source .env/bin/activate
  pip install -r requirements.txt
```

> Please, before to execute *pip install -r requirements.txt* read the file **ReadBeforeStart.txt**
> There you can get more details about the commands *pip install* that we executed.
> The reason is because, when you execute *pip install -r requirements.txt* it will install one by one, however, some packages
> were installed without our desire. So, we recommended read the file **ReadBeforeStart.txt**. 





# Licencia 
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

# Autor
* José Vidal Cardona Rosas / ladivcr@comunidad.unam.mx

# Colaboradores
* Angel 
