import subprocess
import sys
import json
import datetime
import requests
import time

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

#serial_number_command = "cat /proc/cpuinfo | grep Serial | cut -d ' ' -f 2"
gpspipe="timeout 10s gpspipe -w -n 10 |  grep -m 1 speed"
p = subprocess.Popen(gpspipe, stdout = subprocess.PIPE, shell = True)
pipe = p.communicate()[0]

dateString = "%d/%m/%Y,%H:%M:%S"
waktu=json.dumps(datetime.datetime.now().strftime(dateString))

class OK(str):
      def _init_ (self, GPSpipe, time):
          self.gpspipe=GPSpipe
          self.Time=time

oke=OK([pipe,waktu])

def jdefault(o):
    return o.__dict__
print(json.dumps(oke, default=jdefault))

