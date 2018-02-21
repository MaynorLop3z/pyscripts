import threading
import psutil

def printit():
  threading.Timer(1.0, printit).start()
  print(psutil.cpu_percent(interval=1))

printit()