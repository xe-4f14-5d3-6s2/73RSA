# Cifrado RSA con Python

¡Hola! Este es mi proyecto de cifrado RSA hecho en Python. ¡Es genial para entender como funciona la seguridad en linea! Aquí puedes generar tus propias claves, encriptar mensajes y luego desencriptarlos.

## Lo que puedes hacer aquí

* **Generar Claves RSA:** Crea tu par de claves: una pública (para compartir) y una privada (¡esa es solo para ti, es super secreta!)
* **Cifrar Mensajes:** ¿Quieres enviar un mensaje secreto? ¡Usa la clave pública de alguien y listo!
* **Decifrar Mensajes:** Si alguien te envió algo encriptado, ¡usa tu clave privada para leerlo!
* **Es fácil de usar:** Todo se maneja desde la consola ¡Súper simple!

## ¡Manos a la obra!

### Lo que necesitas:

Solo Python 3.x ¡Eso es todo!

### ¡A usarlo!

1. **!Primero dale una estrella al repositorio!**

2. **Clona el proyecto:**
```bash
git clone https//github.com/xe-4f14-5d3-6s2/73RSA.git
cd 74RSA
```

3. **Crea un environment de Python:**
```bash
python3 -m venv env
source env/bin/activate
```

4. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

5. **Ejecuta el programa:**
```bash
python main.py
```

6. **¡Sigue el menú!**

El programa te irá diciendo que hacer. ¡Es muy intuitivo!

* **Generar claves (`0`):** Te dará tus dos claves. ¡Asegúrate de guardar bien la privada!
* **Cifrar un mensaje (`1`):** Necesitas la clave pública de la persona a la que quieres enviar el mensaje (el número "e" y el "n" separados por un guión).
* **Descifrar un mensaje (`2`):** ¡Usa tu clave privada (el número "d" y el "n" separados por un guión) para ver que mensaje te mandaron!

## ¿Que hay dentro?

* `main.py`: Es el cerebro del programa, maneja lo que ves y lo que haces.
* `algorithm.py`: Aquí está toda la magia de RSA: cómo se hacen las claves, como se encripta y desencripta, etc...
* `requirements.txt`: La lista de lo que necesitas instalar.

## ¿Con qué está hecho?

* **Python**
* **Numpy**: Ayuda a que las matemáticas del programa sean más rápidas. ¡especialmente con los números primos!

## ¿Quieres ayudar?
¡Claro que si puedes! Si tienes ideas para mejorar esto, o encuentras algún error, ¡no dudes en abrir un *issue* o enviar un *pull request*! ¡Toda ayuda es bienvenida!

## Licencia
Este proyecto tiene una licencia MIT. Si quieres saber los detalles, echa un vistazo al archivo `LICENSE`

Hecho con <3 por **[Xe] 4f¹⁴ 5d³ 6s²**