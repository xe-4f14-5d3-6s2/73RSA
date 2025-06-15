from algorithm import decrypt, encrypt, generate_keys
import os, platform

def clear():
  if platform.system() == "Linux":
    os.system("clear")
  else:
    os.system("cls")

def main():
  while True:
    clear()
    print("""Hola tu, ¿Qué quieres hacer?
  0 - Generar claves.
  1 - Encriptar un mensaje.
  2 - Desencriptar un mensaje.
  99 - Salir.""")

    cmd = input("> ")
    clear()
    if cmd == "99":
      exit()
    elif cmd == "0":
      clear()
      print("Generando claves...")
      e, d, n = generate_keys()
      clear()
      print(f"""Aquí están tus claves:
Clave Pública: {e}-{n}
Clave Privada: {d}-{n} (No la compartas con nadie.)""")
      input("Presiona <ENTER> para continuar... (Asegurate de haber copiado las claves).")
    elif cmd == "1":
      e, n = input("Escribe la clave de encriptación: ").split("-")
      clear()
      m = input("Escribe el mensaje que quieres encriptar: ")
      clear()
      print("Encriptando mensaje...")
      digest = encrypt(m, int(e), int(n))
      clear()
      print("Listo!")
      print(f"El mensaje encriptado es: {digest}")
      input("Presiona <ENTER> para continuar...")
    elif cmd == "2":
      c = input("Escribe el mensaje cifrado: ")
      clear()
      d, n = input("Escribe la clave de desencriptación: ").split("-")
      clear()
      print("Desencriptando mensaje...")
      message = decrypt(c, int(d), int(n))
      clear()
      print("Listo!")
      print(f"Tu mensaje desencriptado es: {message}")
      input("Presiona <ENTER> para continuar...")


if __name__ == "__main__":
  main()