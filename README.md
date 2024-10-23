# WebApp de Recopilación de Precios de Alquiler
## Python | Flask

Esta es una aplicación web desarrollada en Python que permite a los usuarios introducir su dirección de correo electrónico y el precio que pagan por el alquiler. La aplicación recopila estos datos y, a partir de ellos, calcula la media del precio de alquiler. Una vez enviados los datos, los usuarios reciben un correo electrónico con la información ingresada y la media calculada.

**Tecnologías Utilizadas**

Flask: Framework web ligero utilizado para crear la aplicación web.
Flask-SQLAlchemy: ORM utilizado para interactuar con la base de datos PostgreSQL.
PostgreSQL: Sistema de gestión de bases de datos utilizado para almacenar los datos de los usuarios.
SMTP: Protocolo utilizado para enviar correos electrónicos a los usuarios con los resultados de la encuesta.

**Características**

Recopilación de precios de alquiler: Los usuarios pueden ingresar su correo electrónico y el precio que pagan por el alquiler.
Cálculo de la media del precio: Se calcula automáticamente el precio promedio de alquiler a partir de todos los datos ingresados en la aplicación.
Envío de correos electrónicos: Los usuarios reciben un correo con el precio ingresado y la media calculada. Se utiliza el protocolo SMTP para enviar estos correos.
Validación de duplicados: Evita que una misma dirección de correo electrónico envíe múltiples entradas.

### Puedes acceder a la web y participar en la encustra desde este enlace [PriceCollectorApp](https://juanbrenes.pythonanywhere.com/)
