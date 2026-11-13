# Comprensión Técnica: Arquitectura de Portal de Servicios

## 1. Flujo de comunicación y procesamiento web

Cuando un empleado abre su navegador web —que actúa como **cliente**— y escribe la dirección local de la aplicación (por ejemplo, `http://127.0.0.1:5000`), el navegador utiliza la **dirección IP** (`127.0.0.1`, correspondiente al equipo local) y el **puerto** (`5000`) para localizar el proceso del **servidor** donde se ejecuta nuestra aplicación. A través del protocolo **HTTP**, el navegador envía una petición inicial (**request**) de tipo GET solicitando la página principal.

En el lado del **servidor** o **backend**, la aplicación desarrollada en **Python** con el microframework **Flask** recibe esa solicitud y busca qué **ruta** (`@app.route(...)`) corresponde a la URL pedida. Una vez identificada, Flask procesa la lógica correspondiente y renderiza un **template** (archivo `.html` ubicado en la carpeta `templates/`), devolviendo al navegador una respuesta (**response**) **HTTP** con el código de estado 200 OK y el documento construido.

Al recibir la respuesta, el navegador —que representa el **frontend**— interpreta la estructura del documento en **HTML**, aplica los estilos visuales definidos en **CSS** y en el framework **Bootstrap** (como la barra de navegación, las tarjetas y el diseño responsivo) para dibujar la interfaz en pantalla. En esta interfaz, **JavaScript** (incluido mediante el bundle de Bootstrap) interviene únicamente para dar interactividad visual en el navegador, como el desplazamiento de las diapositivas del carrusel o el despliegue del menú en pantallas pequeñas, sin realizar cálculos de negocio.

Cuando el empleado navega hacia la sección de Compra, captura la cantidad de artículos y el precio unitario en el formulario y presiona el botón de calcular, el navegador empaqueta esos datos dentro del cuerpo de una nueva petición **HTTP** utilizando el método **POST** y la envía hacia la **ruta** `/compra` del **servidor**. En el **backend**, **Flask** intercepta el **request** **POST**, extrae los valores enviados desde el formulario mediante **Python**, ejecuta las operaciones aritméticas para obtener el subtotal, evalúa si aplica el descuento del 10 % y calcula el total final. Finalmente, Flask vuelve a renderizar el **template** de compra inyectando tanto los datos capturados como los resultados calculados, y envía la **response** en **HTML** de vuelta al **cliente** para que el empleado visualice el desglose en pantalla.

---

## 2. Diagrama de flujo de comunicación

```mermaid
flowchart LR
    A["Cliente (Navegador)<br/>Frontend: HTML, CSS, Bootstrap, JS"] -- "1. Request HTTP (POST /compra)<br/>Hacia IP:Puerto (127.0.0.1:5000)<br/>Datos: cantidad y precio" --> B["Servidor (Python + Flask)<br/>Backend: Ruta /compra"]
    B -- "2. Procesamiento en Python<br/>Calcula subtotal, descuento y total" --> B
    B -- "3. Response HTTP (200 OK)<br/>Renderiza template HTML con resultados" --> A