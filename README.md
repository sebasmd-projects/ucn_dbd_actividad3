<a name="informe-de-diseño-del-sistema-de-gestión-de-biblioteca-universitaria"></a>
# Informe de Diseño del Sistema de Gestión de Biblioteca Universitaria

- [Informe de Diseño del Sistema de Gestión de Biblioteca Universitaria](#informe-de-diseño-del-sistema-de-gestión-de-biblioteca-universitaria)
  - [Introducción](#introducción)
  - [Funcionalidades Principales](#funcionalidades-principales)
    - [Modelo ER](#modelo-er)
    - [Usuarios](#usuarios)
      - [Modelo `UserModel`](#modelo-usermodel)
    - [Libros](#libros)
      - [Modelo `BookModel`](#modelo-bookmodel)
    - [Préstamos](#préstamos)
      - [Modelo `LoanModel`](#modelo-loanmodel)
    - [Personal de Biblioteca](#personal-de-biblioteca)
      - [Modelo `LibraryStaffModel`](#modelo-librarystaffmodel)
    - [Multas](#multas)
      - [Modelo `FineModel`](#modelo-finemodel)
  - [Decisiones de Diseño](#decisiones-de-diseño)
    - [Eficiencia y Escalabilidad](#eficiencia-y-escalabilidad)
    - [Mantenimiento y Extensibilidad](#mantenimiento-y-extensibilidad)
    - [Integridad de Datos](#integridad-de-datos)
  - [Contribución de Cada Elemento](#contribución-de-cada-elemento)
    - [Usuarios y Personal de Biblioteca](#usuarios-y-personal-de-biblioteca)
    - [Préstamos y Multas](#préstamos-y-multas)
  - [Desarrollo de la actividad](#desarrollo-de-la-actividad)
    - [Vistas](#vistas)
    - [Consultas](#consultas)
    - [Lógica de cambio de estados](#lógica-de-cambio-de-estados)
  - [Conclusión](#conclusión)

<a name="introducción"></a>
## Introducción

Este informe describe el diseño de un sistema de gestión de una biblioteca universitaria, incluyendo las funcionalidades principales, las decisiones tomadas durante el desarrollo y cómo cada elemento contribuye a la eficiencia del sistema. El sistema abarca la gestión de usuarios, libros, préstamos, personal de biblioteca, jerarquía del personal y multas.

<a name="funcionalidades-principales"></a>
## Funcionalidades Principales

<a name="modelo-er"></a>
### Modelo ER


![Vista #1](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/ModeloER.png?raw=true)

<a name="usuarios"></a>
### Usuarios

El sistema gestiona dos tipos de usuarios: estudiantes y profesores. Cada usuario registra datos como:

- Carnet
- Nombre
- Apellidos
- Carrera (para estudiantes)
- Departamento (para profesores)
- Dirección
- Teléfono

<a name="modelo-usermodel"></a>
#### Modelo `UserModel`

- `is_teacher` y `is_student`: Booleanos que determinan si el usuario es profesor o estudiante.
- `identification_card`, `cell_phone`, `birthday`, `address`: Campos para almacenar la información personal del usuario.
- `career`: Relación con la carrera (para estudiantes).
- `department`: Relación con el departamento (para profesores).
- Métodos adicionales como `get_age()` para calcular la edad del usuario y `save()` para formatear correctamente los nombres y el nombre de usuario.

<a name="libros"></a>
### Libros

Facilita la gestión detallada de libros, autores y géneros, permitiendo búsquedas y categorizaciones eficientes.

Cada libro tiene:

- Identificación única
- Título
- Autor(es)
- Género(s)
- Fecha de publicación
- Disponibilidad

<a name="modelo-bookmodel"></a>
#### Modelo `BookModel`

- `title`, `publication_date`, `is_available`: Campos que describen el libro.
- `author`, `genre`: Relaciones Many-to-Many para asociar múltiples autores y géneros con el libro.
- Método `__str__()` para una representación legible del libro.

<a name="préstamos"></a>
### Préstamos

Registra los préstamos de libros a usuarios, incluyendo:

- Usuario
- Libro(s)
- Fecha de inicio
- Fecha de devolución
- Estado (activo, vencido, devuelto)

<a name="modelo-loanmodel"></a>
#### Modelo `LoanModel`

- `user`, `book`, `start_date`, `end_date`, `status`, `return_date`: Campos y relaciones necesarios para registrar y gestionar los préstamos.
- Método `save()` para actualizar el estado del préstamo.
- Señales `post_save` y `m2m_changed` para gestionar automáticamente las multas y la disponibilidad de los libros.

<a name="personal-de-biblioteca"></a>
### Personal de Biblioteca

Datos sobre el personal, incluyendo:

- Nombre
- Apellidos
- Departamento
- Teléfono
- Jerarquía (bibliotecario jefe y superior)

<a name="modelo-librarystaffmodel"></a>
#### Modelo `LibraryStaffModel`

- `user`, `department`, `is_chief_librarian`, `superior`: Campos y relaciones necesarios para gestionar el personal y su jerarquía.

<a name="multas"></a>
### Multas

Registro de multas por devoluciones tardías, con detalles como:

- Fecha
- Usuario
- Libro
- Valor de la multa

<a name="modelo-finemodel"></a>
#### Modelo `FineModel`

- `loan`, `date`, `amount`, `paid`, `return_date`: Campos necesarios para gestionar las multas.
- Señal `post_save` para actualizar el estado del préstamo cuando se paga una multa.

<a name="decisiones-de-diseño"></a>
## Decisiones de Diseño

<a name="eficiencia-y-escalabilidad"></a>
### Eficiencia y Escalabilidad

- Uso de relaciones `ForeignKey` y `ManyToManyField` para manejar asociaciones entre modelos de manera eficiente.
- Implementación de señales para automatizar procesos, como la actualización del estado de los préstamos y las multas.
- Campos `UUID` para las identificaciones, asegurando unicidad y seguridad.

<a name="mantenimiento-y-extensibilidad"></a>
### Mantenimiento y Extensibilidad

- Herencia de `TimeStampedModel` para agregar automáticamente campos de `created_at` y `updated_at` a todos los modelos.
- Uso de `AbstractUser` para extender el modelo de usuario predeterminado de Django, permitiendo una personalización flexible.

<a name="integridad-de-datos"></a>
### Integridad de Datos

- Métodos `save()` personalizados en modelos para asegurar la consistencia de los datos (e.g., formateo de nombres, actualización de estados).
- Relaciones `on_delete=models.SET_NULL` para manejar eliminaciones sin perder la integridad referencial.

<a name="contribución-de-cada-elemento"></a>
## Contribución de Cada Elemento

<a name="usuarios-y-personal-de-biblioteca"></a>
### Usuarios y Personal de Biblioteca

- Proporciona un sistema robusto para gestionar diferentes tipos de usuarios con sus respectivas características y relaciones jerárquicas.

<a name="préstamos-y-multas"></a>
### Préstamos y Multas

- Automatiza la gestión de préstamos y multas, asegurando que los usuarios y el personal de la biblioteca puedan seguir fácilmente el estado de los libros y las posibles sanciones por devoluciones tardías.

<a name="desarrollo-de-la-actividad"></a>
## Desarrollo de la actividad

El administrador de Django se ha personalizado para ofrecer una interfaz de usuario intuitiva y funcionalidades específicas para la gestión de la biblioteca universitaria. A continuación se detallan las vistas y consultas implementadas para responder a las necesidades de los usuarios del sistema

<a name="vistas"></a>
### Vistas

1. **Listado de Personal de Biblioteca con Libros Prestados:** La vista muestra la información del personal de biblioteca junto con los libros que tienen prestados y la cantidad acumulada de préstamos realizados.

    ![Vista #1](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/vistas/vista1.png?raw=true)

2. **Listado de Usuarios con Libros Prestados y Multas:** Esta vista presenta un listado de usuarios con los libros que tienen prestados y el total acumulado de multas.

    ![Vista #2](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/vistas/vista2.png?raw=true)

3. **Listado de Libros Disponibles y Cantidad de Préstamos:** Proporciona un listado de libros disponibles y la cantidad acumulada de préstamos realizados.

    ![Vista #3.0](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/vistas/vista3.0.png?raw=true)
    ![Vista #3.1](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/vistas/vista3.1.png?raw=true)

4. **Listado de Personal de Biblioteca con Libros y Préstamos Acumulados:** Muestra la información del personal de biblioteca con los libros que tienen y la cantidad acumulada de préstamos realizados.

    ![Vista #4.0](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/vistas/vista4.0.png?raw=true)
    ![Vista #4.1](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/vistas/vista4.1.png?raw=true)

5. **Listado de Multas Detallado:** Detalla las multas registradas con información sobre la fecha, usuario, libro y valor de la multa.

    ![Vista #5](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/vistas/vista5.png?raw=true)

<a name="consultas"></a>
### Consultas

1. **Información Completa de Personal de Biblioteca y Libros Prestados:** Muestra la información detallada del personal de biblioteca con datos y la información de los libros que tienen prestados.

    ![Consulta #1](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta1.png?raw=true)

2. **Información Completa de Usuarios, Libros Prestados y Multas:** Proporciona un listado de usuarios con sus datos y la información de los libros que tienen prestados y las multas acumuladas.

    ![Consulta #2](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta2.png?raw=true)

3. **Libros Disponibles y Cantidad de Préstamos en un Día Específico:** Detalla un listado de libros disponibles y la cantidad de préstamos realizados en un día específico.

    ![Consulta #3.0](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta3.0.png?raw=true)
    ![Consulta #3.1](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta3.1.png?raw=true)
    ![Consulta #3.2](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta3.2.png?raw=true)
    ![Consulta #3.3](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta3.3.png?raw=true)
    ![Consulta #3.4](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta3.4.png?raw=true)
    ![Consulta #3.5](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta3.5.png?raw=true)

4. **Personal de Biblioteca con Libros y Préstamos Acumulados:** Ofrece un listado de personal de biblioteca con los libros que tienen y la cantidad acumulada de préstamos realizados.

    ![Consulta #4.0](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta4.0.png?raw=true)
    ![Consulta #4.1](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta4.1.png?raw=true)

5. **Información Completa de Multas:** Detalla un listado de multas registradas con número de usuario, libro, fecha y valor de la multa.

    ![Consulta #5](https://github.com/sebasmd-projects/ucn_dbd_actividad3/blob/master/media/imgs/consultas/consulta5.png?raw=true)

<a name="lógica-de-cambio-de-estados"></a>
### Lógica de cambio de estados

En el sistema de gestión de biblioteca universitaria, se implementó una lógica para cambiar automáticamente el estado de los préstamos y generar multas cuando corresponda. Esto se logra a través de señales (signals que hacen referencia a los triggers) en Django que se activan después de guardar un préstamo o una multa.

Por ejemplo, cuando se guarda un préstamo, se verifica si ha superado la fecha de devolución. Si es así, se cambia automáticamente el estado del préstamo a "vencido" y se genera una multa. Además, cuando se marca una multa como pagada y se registra la fecha de devolución, se actualiza el estado del préstamo relacionado a "devuelto".

Este enfoque automatizado garantiza que el sistema sea eficiente y preciso en la gestión de préstamos y multas, eliminando la necesidad de intervención manual para actualizar estados.

La generación automática de multas asegura que los usuarios sean responsables de devolver los libros a tiempo y evita la necesidad de que el personal de la biblioteca intervenga manualmente para imponer multas.

<a name="conclusión"></a>
## Conclusión

El diseño del sistema está orientado a ofrecer una gestión eficiente y escalable de la biblioteca universitaria. Cada componente está cuidadosamente diseñado para asegurar la integridad de los datos y facilitar la administración tanto para los usuarios como para el personal de la biblioteca. La implementación de señales y métodos personalizados garantiza que el sistema responda automáticamente a cambios en los datos, reduciendo la necesidad de intervención manual y mejorando la eficiencia operativa.

Las funcionalidades implementadas en el sistema de gestión de biblioteca universitaria están diseñadas para mejorar la eficiencia y la precisión en la gestión de préstamos, multas y usuarios.

- La automatización de tareas como el cambio de estados de préstamos y la generación de multas garantiza un proceso fluido y sin errores en la gestión del sistema.
- La personalización del administrador de Django proporciona una interfaz amigable y fácil de usar para los usuarios finales, lo que facilita la navegación y la administración de datos.
- La implementación de señales (signals) en Django permite que las acciones se desencadenen automáticamente en respuesta a ciertos eventos, reduciendo la necesidad de intervención manual y mejorando la eficiencia del sistema.

En resumen, el diseño y la implementación del sistema de gestión de biblioteca universitaria se basan en principios de eficiencia, precisión y usabilidad, asegurando una experiencia óptima tanto para el personal de la biblioteca como para los usuarios finales.
