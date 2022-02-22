import os
import pandas as pd

#   Obtener paquetes
paquetes = pd.read_csv("paquetes.csv")
com = list(paquetes)

os.chdir(r"D:\Documents\Android\ADB")
os.system("adb devices")

for item in com:
    print(item +  ":")
    os.system("adb shell pm uninstall -k --user 0 "+ item)