'''Logger with StreamHandler() and addHandler(console) are useful to display the message on console and write in log file as well.'''


import datetime
import os
import logging

""" Creating required filename """
filename = os.path.abspath(__file__).split("/")[-1].split(".py")[0] + "_" \
           + datetime.datetime.now().strftime('%m%d%y_%H%M%S')
execution_log = "/tmp/" + filename + ".log"


""" Setup logging attributes  """
logging.basicConfig(filename=execution_log, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s: %(message)s', datefmt='%m%d%y %H:%M:%S')

''' Setup logging over console '''
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
