import subprocess

def uninstall(name):
    subprocess.call(['pip', 'uninstall', name])

uninstall("plotly")