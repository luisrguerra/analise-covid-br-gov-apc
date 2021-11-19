def diretorioAtual():
    #trocar diretório atual para a pasta do programa
    import os
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

diretorioAtual()

import subprocess
subprocess.call("pip install --upgrade pip")
subprocess.call("pip uninstall -r requirements.txt")
