# Task-Api

Crea un entorno virtual utilizando virtualenv o conda y luego ejecuta el comando ` pip install -r requirements.txt` o ` pip3 install -r requirements.txt ` para instalar las dependencias. 


# Endpoints

* New Task : `POST /api/newtask` crea una nueva tarea

* Tasks : `GET /api/tasks` trae todas las tareas de la base de datos

* One Task : `Get /api/task/<id>` trae una tarea en base a su _id

* Delete Task : `DELETE /api/task/<id>` eliminar una tarea en base a su _id

* Complete Task : `PUT /api/task/<id>` completar una tarea en base a su _id

* Update Task : `PUT /api/task/<id>` actua una tarea en base a su _id