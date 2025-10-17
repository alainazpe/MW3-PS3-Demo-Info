import os
import sys
import string
import re
import struct
from datetime import datetime

fullASCII = set(string.printable[:-5]) | set("ÑñÁÉÍÓÚáéíóúÜü¡¿ÑÀÈÌÒÙàèìòù´`")
dateFormat = "%d/%m/%Y %H:%M:%S"
sumarDosHorasFecha = 7200

def read_ascii(data: bytes) -> str:
    """Lee valores en ASCII para tenerlos separados por comas """
    datos = ''.join(chr(b) if chr(b) in fullASCII else ',' for b in data)
    words = re.findall(r'\b\w+\b', datos)

    i = 0
    while i < len(words):
        if len(words[i]) >= 3:
            if ("_" in words[i][2:3] and "p" in words[i] and "m" in words[i]):
                return ("<td>"+words[i-1]+"</td><td>"+words[i]+"</td><td>"+words[i+1]+"</td><td>"+datetime.utcfromtimestamp(struct.unpack('>I', data[(datos.find((words[i+1])) + len((words[i+1])) + 55):(datos.find((words[i+1])) + len((words[i+1])) + 55)+4])[0] + sumarDosHorasFecha).strftime(dateFormat)+"</td></tr>")
            i += 1
        else:
            i += 1
def main():
    if len(sys.argv) < 2:
        print(f"Uso: {sys.argv[0]} <carpeta>")
        sys.exit(1)
    print("<table><thead><th>Fichero</th><th>Modo</th><th>Mapa</th><th>Jugador</th><th>Fecha</th></thead><tbody>")

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        sys.exit(1)

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if not os.path.isfile(filepath):
            continue

        try:
            with open(filepath, "rb") as f:
                f.seek(-0xE0BF, os.SEEK_END)
                data = f.read()
        except OSError as e:
            continue
        except ValueError:
            with open(filepath, "rb") as f:
                data = f.read()
        print("<tr><td>",filename,"</td>",read_ascii(data))
    print("</tbody></table>")

if __name__ == "__main__":
    main()