import os
import sys
import time

os.system ("ps -elf | grep 'python antrian01.py' | awk '{print $4}' | xargs sudo kill")
os.system ("ps -elf | grep 'python /home/pi/dataku/antrian/antrian01.py' | awk '{print $4}' | xargs sudo kill")

#os.system ("ps -elf | grep 'python buttonmatrix2.py' | awk '{print $4}' | xargs sudo kill")
os.system ("ps -elf | grep 'python /home/pi/dataku/antrian/data_lama/buttonmatrix2.py' | awk '{print $4}' | xargs sudo kill")

os.system ("python /home/pi/dataku/antrian/data_lama/buttonmatrix2.py")
os.system ("python /home/pi/dataku/antrian/antrian01.py")
#retss arial

