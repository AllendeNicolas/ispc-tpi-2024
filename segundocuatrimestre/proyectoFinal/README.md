#INNOVACIÓN Y GESTIÓN DE DATOS: 

# GRUPO N° 19

<div id="top"></div>

<div align="center">
<h3 align="center">Proyecto Final: espacio curricular: Innovación en gestión de datos - ISPC</h3>
 <p align="center">
     Proyecto: DATA  HUMAN´S
    <br />
    VER ÍNDICE MÁS ABAJO
    
  </p>
</div>

<!-- INDICE -->
<details>
  <summary><strong>TABLA DE CONTENIDOS</strong></summary>
  <ul>
    <li>
      <a href="#integrantes">Integrantes</a>
    </li>
    <li><a href="#programaciónI">Innovación y gestión de datos</a>
     <ul>
        <li><a href="#presentación">Presentación del proyecto</a></li>
        <li><a href="#descripcion-archivos">Descripción de carpetas y archivos</a>
        <li><a href="#descripcionPI">Programación I</a></li>
        <li><a href="#descripcionBDII">Base de Datos II</a></li>
        <li><a href="#descripcionejecucion"> Requisitos del Programa</a></li>
        <li><a href="#descripcioneaplicacion">Para ejecutar el Programa</a></li>
     </ul>
     </li>
  </ul>
</details>

<hr/>

<!-- INTEGRANTES -->

# Integrantes

Marián Chazarreta - 37.509.774 - marianchazarreta@hotmail.com - https://github.com/marianuvita</br>
Lucas Ryser - 44.346.194 - lucasryser4k@gmail.com - https://github.com/lucasryser6</br>
Emanuel Guaráz - 38.276.061- guarazjemanuel@gmail.com https://github.com/JEmanuelG</br>
Nicolás Allende Olmedo - 35.871.057 - nicoallende92@gmail.com - https://github.com/AllendeNicolas</br>
Bruno Lobo Souza - 95.690.709 - lobosouza.it@gmail.com - https://github.com/lobosouza</br>
Carlos Direni - 28.117.281 - direnicarlos@gmail.com - https://github.com/Cdireni</br>

<hr/>

<p>DATA HUMAN'S es una empresa dedicada al desarrollo y mantenimiento de Software y Bases de Datos, orientada a la organización y asistencia de los departamentos de Recursos Humanos (RRHH), de las empresas en general.</p>

<p>Brindamos un sistema de Bases de Datos y Gestión de empleados, el cual cuenta con un sistema de selección de personal, mediante filtros de búsqueda entre los posibles candidatos, para los puestos vacantes de las empresas, ajustandose a las necesidades y requisitos a cumplir para el ingreso a planta.</p>

<p>De ampliarse el proyecto, nos gustaría que contase también con un análisis de producción de cada empleado, considerando las tareas que debe realizar, analizando su eficacia, y eficiencia laboral. También un análisis del ambiente laboral, teniendo en cuenta las relaciones interpersonales de los empleados dentro de la planta, y considerando la salud mental (aptos psicológicos) de los integrantes de la empresa.</p>

<p>Entre otras funciones, podríamos encontrar, conteos de empleados en planta, alta y baja de los mismos, filtros por departamentos, asignaciones de indumentaria laboral, pagos de sueldos, aportes y seguridad social, verificación de asistencia laboral, etc.</p>

<p>La descripción anterior es a lo que nos gustaría llegar como proyecto final, pero para esta instancia nos hemos enfocado únicamente en la carga de vacantes y búsqueda de postulantes.</p>

<hr/> 

<h3 align="center" id="programaciónI">Innovación y gestión de datos</h3>

<h4 id='descripcionPI'><strong>PROGRAMACION I</strong></h4>

<hr/>

<p>En el repositorio, específicamente dentro de la carpeta  segundo cuatrimestre, la carpeta Evidencia 3, que contiene un sub-archivo denominado app, con lo solicitado para cumplir los requisitos de la Evidencia 3, del módulo de Innovación y gestión de Base de Datos. Aquí se encuentran los archivos que continuan con lo solicitado en la Evidencia2, con las correcciones correspondientes, que habian quedado por resolver para esta evidencia. (accesos_funciones.py, crud_usuarios.py, loggedin.py, main.py, menu_evidencia2.py, ordenamiento_busqueda.py, registros_pluviales.py).
 
 en el caso de registros_pluviales.py, la aplicación funciona correctamente, sólo debe cerrar las ventanas emergentes con los gráficos, para que muestre el siguiente gráfico con los registros.<p/>

<hr/>

<h4 id='descripcionBDII'><strong>BASE DE DATOS II</strong></h4> 

<hr/>

<h3 align="center" id='descripcion-archivos'>DESCRIPCIÓN DE LOS ARCHIVOS</h3>

<h4 id="db"> 📂 Carpeta <code>db</code></h4>

<p>Contiene los archivos:</p>

📂 Carpeta datahumans_db

 <p>Este archivo contienen todo lo referido a la Base de Datos del Proyecto</p>

- datahumans_actualizada_2.sql
<p>Archivo con la base de datos completa de la aplicación. Este archivo será el que utilizaremos para la ejecución de la aplicación (más adelante se encuentran los pasos a seguir).</p>

- datahumans_bd_structureonly_actualizada.sql
<p>Contiene únicamente la estructura del esquema, sin datos.</p>

- datahumans_bd_dataonly_actualizada.sql
<p>Contiene únicamente los datos  correspondientes al esquema.</p>

<p> En el mismo archivero -bd-, se encuentra también:</p>

- consultas.sql
<p>En este archivo se encuentran diferentes consultas para hacer sobre la base de datos, que se utilizarán en backend.</p>

<p> El modelo Crow Foot completo y actualizado</p>

🖼️ - datahumans_DER.sql.mwb

<p> Y un archivo SQL, con las modificaciones sugeridas para la evidencia 3</p>

- modificaciones_sugeridas.sql

<hr />

<h4 id='descripcionejecucion'><strong> Requisitos del programa</strong></h4>

<p>1) Será de utilidad tener instalado un entorno de desarrollo, en este caso, utilizamos de preferencia <strong>"VISUAL STUDIO CODE"</strong>.</p>

<P>2) En el mismo entrono de desarrollo, intalaremos <strong>"PYTHON"</strong>, como lenguaje de programación, para el desarrollo y puesta en funcionamiento de la aplicación</P>

<p>3) Y para ejecutar el Programa, es necesario tener descargada la Librería <strong>"PANDAS"</strong>, que fue la Librería seleccionada para la creación de los objetos en Python. (la misma se instala de la siguiente manera: En <strong>Visual Studio Code</strong>, ya  en el archivo Python a desarrollar o ejecutar, abrimos la <strong>Terminal</strong> dedicada, e ingresamos la siguiente línea de código… <strong>"pip install pandas"<strong/> y damos <strong>Enter</strong>,  Python realizará la descarga e instalación de la librería automáticamente, y estará lista para ser utilizada)</p>

<p> 4) También será necesario tener descargada la Librería de <strong>Matplotlib</strong>, que fue la librería solicitada para el desarrollo de los registros pluviales con Python. (la misma se instala de la siguiente manera: En <strong>Visual Studio Code</strong>, ya  en el archivo Python a desarrollar o ejecutar, abrimos la <strong>Terminal</strong> dedicada, e ingresamos la siguiente línea de código… <strong>"pip install matplotlib"<strong/> y damos <strong>Enter</strong>,  Python realizará la descarga e instalación de la librería automáticamente, y estará lista para ser utilizada)</p>

<hr/>

<h4 id='descripcionaplicacion'><strong> Ejecución del programa</strong></h4>

<p> Para Ejecutar la aplicación debemos seguir los siguientes pasos:</p>
<p> 1) Ejecutar el script principal "main.py" que se encuentra en la carpeta "app".</p>
<p> 2) Elegir una opción de las que ofrece el menú.</p>
<p> 3) Ingresar los datos según corresponda.</p>

<hr/> 
<h3> Link Evidencia 3</h3>
<p align="center"><a href= https://github.com/AllendeNicolas/ispc-tpi-2024/tree/main/segundocuatrimestre/evidencia3><strong>Ver Evidencia 2 »</strong></a></p>

