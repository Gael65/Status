import psutil, os

while True:
    procesosPython = 0

    for proceso in psutil.process_iter():
        if proceso.name().lower() == "python.exe":
            procesosPython += 1
    
    if procesosPython == 1: #solamente se esta ejecutando status.py
        print("Aplicacion principal cerrada. Abriendo de nuevo...")
        os.system("python main.py")
