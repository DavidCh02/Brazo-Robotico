# BRAZO ROBOTICO
#### Link Pagina web: https://davidch02.github.io/index.html
#### Link a repositorio de la pagina web: https://github.com/DavidCh02/DavidCh02.github.io.git
### Iniciativa

Este proyecto comenzó debido a una necesidad existente en nuestro campo de estudio, la acumulación de basura o afecta la estética y el ambiente del campus universitario también tiene implicaciones negativas para la salud pública y el medio ambiente. La necesidad de un sistema eficiente y semi automatizado para la recolección de residuos que es crucial para mantener un entorno limpio y sostenible.

#TeleRobot
##### Diagrama UML
![Brazo](https://github.com/DavidCh02/Brazo-Robotico/assets/166523123/d178f37d-4fa4-45cf-93cb-8307f192e7fd)


-----------------------------------------------------------------------------
### Requerimientos del sistema
- Conexión y desconexión del control remoto: El sistema debe permitir a los usuarios conectar y desconectar el control remoto de forma inalámbrica a través de Wi-Fi y Bluetooth.
- Control del brazo robótico: El sistema debe permitir a los usuarios controlar el brazo robótico para realizar tareas específicas, como mover la base, el brazo, el antebrazo y la pinza.
- Transmisión de vídeo: Si el sistema utiliza la cámara ESP32-CAM, puede ser un requerimiento transmitir vídeo en tiempo real desde la cámara a una ubicación remota.
- Análisis de residuos: Si el sistema incluye un componente de análisis de residuos, puede ser necesario registrar los residuos analizados, almacenar datos relacionados con esos residuos y proporcionar funciones para consultar y analizar esos datos.
- Medición de peso: Si el sistema incluye un sensor de peso, puede ser necesario medir y registrar el peso de los objetos colocados en una balanza.

-----------------------------------------------------------------------------
## Caso de uso
#### 1. Identificación del Caso de Uso	
**Nombre**: Recolección de Residuos con Brazo Robótico
**Actor** Principal: Usuario (operador)
**Objetivo**: Permitir al usuario controlar remotamente un brazo robótico para recoger, 					pesar y clasificar residuos en el campus universitario.
**Precondiciones**: El sistema está encendido, el brazo robótico está en estado inicial y todos los módulos (ESP32-CAM, sensores, Bluetooth) están funcionando correctamente.
**Postcondiciones**: Los residuos han sido recolectados, pesados y clasificados correctamente.
#### 2. Flujo Principal de Eventos (Camino Feliz)
##### Inicio del Sistema
El usuario enciende el brazo robótico y verifica que todos los módulos están operativos.
##### Conexión RemotaConexión Remota
El usuario se conecta al brazo robótico a través de una interfaz de control remoto utilizando Bluetooth.
##### Visualización en Tiempo Real
La cámara ESP32-CAM transmite video en tiempo real a la interfaz del usuario, permitiendo ver el área de recolección.
##### Control del Brazo Robótico
El usuario utiliza los controles de la interfaz para mover el brazo robótico hacia el residuo identificado en la transmisión de video.
##### Recolección del Objeto
El brazo robótico se posiciona sobre el residuo y utiliza su garra para recogerlo.
##### Medición del Peso
Una vez recogido, el objeto es llevado a un sensor de peso (integrado en el brazo) para medir su masa.
El peso del objeto se muestra en la interfaz del usuario.
##### Clasificación del Residuo
Basado en el peso y tipo del residuo (determinado visualmente por el usuario), el residuo es depositado en el contenedor adecuado.
##### Registro de Datos
El sistema registra la acción, incluyendo el tipo y peso del residuo recolectado.
Repetición del Proceso
El usuario repite el proceso para recoger más residuos hasta completar la tarea.
##### Desconexión y Apagado
El usuario desconecta el control remoto y apaga el sistema.
#### 3. Flujos Alternativos
##### A1: Fallo en la Conexión Remota
Condición: Si la conexión Bluetooth falla.
Acción: El sistema intentará reconectar automáticamente. Si no es posible, se notificará al usuario para intentar manualmente o revisar el módulo Bluetooth.
##### A2: Objeto No Detectado
Condición: Si el objeto no es visible claramente en la transmisión de video.
Acción: El usuario puede ajustar la posición de la cámara o iluminación para mejorar la visibilidad antes de intentar recoger el objeto nuevamente.
##### A3: Error en la Medición del PesoA3: Error en la Medición del Peso
**Condición**: Si el sensor de peso no puede medir correctamente.
Acción: El sistema notificará al usuario y pedirá que el objeto sea recolocado en el sensor o que se realice una calibración rápida del sensor de peso.
#### 4. Requisitos de Sistema
#### Hardware:
- Brazo robótico con múltiples grados de libertad.
- ESP32-CAM para transmisión de video.
- Sensor de peso (por ejemplo, HX711).
- Módulo Bluetooth para control remoto.
#### Software:
- Interfaz de control remoto para el usuario (puede ser una aplicación móvil o de escritorio).
- Algoritmos para control del brazo, procesamiento de señales de video, y medición del peso.
- Sistema de registro de datos para almacenar información sobre residuos recolectados.

------------


#### 5. Descripción de Interfaces
#### Interfaz de Usuario:
- Pantalla que muestra la transmisión de video en tiempo real.
- Controles para mover el brazo robótico (botones virtuales).
- Tabla para mostrar el peso del objeto y opciones de clasificación.
- Indicadores de estado del sistema y notificaciones de errores.
##### Interfaz de Hardware:
- Conexiones entre el ESP32-CAM, el sensor de peso, WIFI, y el módulo Bluetooth con el brazo robótico.
- Fuente de alimentación adecuada para todos los componentes.
-------------
## Capturas
![image](https://github.com/DavidCh02/Brazo-Robotico/assets/166523123/908a4441-c63d-4ca4-aa03-3c819c0bc512)
![image](https://github.com/DavidCh02/Brazo-Robotico/assets/166523123/bfdb9ec5-e06d-4aa1-aa87-175ff044222e)
![image](https://github.com/DavidCh02/Brazo-Robotico/assets/166523123/e9ea588a-3f66-4a57-9b6a-1e2936964dc4)
![image](https://github.com/DavidCh02/Brazo-Robotico/assets/166523123/2e07e837-cb01-408f-a729-70b7d7963a40)
![image](https://github.com/DavidCh02/Brazo-Robotico/assets/166523123/76073647-7242-4520-b0cb-668c4de57f55)
![image](https://github.com/DavidCh02/Brazo-Robotico/assets/166523123/f55f162e-4cee-4d64-a38f-35439d60a862)




