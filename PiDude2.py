
from blinkt import set_pixel, set_brightness, show, clear


import subprocess, signal, time, sys


def signal_handler(signal, frame):
    """
    This signal handler allows us to background
    the process and send it a simple SIGINT to tell it to
    exit cleanly.
    """
    sys.exit(0)

#Start the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

set_brightness(0.5)

x = 0
while x < 50:



      subprocess.call("/home/pi/Pimoroni/blinkt/examples/wget.sh", shell=True)
      
      time.sleep(0.5)


      print "calling file"
      num_lines = sum(1 for line in open('/mnt/ramdisk/down.htm'))
      num_linespart = sum(1 for line in open('/mnt/ramdisk/part.htm'))
      print "lines counted"

      print num_lines
      print num_linespart

      if num_lines > 256:
         print "device is down and out"

         set_pixel(0, 255, 0, 0)
         set_pixel(1, 255, 0, 0)
         set_pixel(2, 255, 0, 0)
         set_pixel(3, 255, 0, 0)
         set_pixel(4, 255, 0, 0)
         set_pixel(5, 255, 0, 0)
         set_pixel(6, 255, 0, 0)
         set_pixel(7, 255, 0, 0)
         show()

      elif num_linespart > 256:
           print "device is partially down and out"

           set_pixel(0, 220, 100, 0)
           set_pixel(1, 220, 100, 0)
           set_pixel(2, 220, 100, 0)
           set_pixel(3, 220, 100, 0)
           set_pixel(4, 220, 100, 0)
           set_pixel(5, 220, 100, 0)
           set_pixel(6, 220, 100, 0)
           set_pixel(7, 220, 100, 0)
           show()
           
      elif num_linespart < 255:
           print "all devices are responding"

           set_pixel(0, 0, 40, 0)
           set_pixel(1, 0, 40, 0)
           set_pixel(2, 0, 40, 0)
           set_pixel(3, 0, 40, 0)
           set_pixel(4, 0, 40, 0)
           set_pixel(5, 0, 40, 0)
           set_pixel(6, 0, 40, 0)
           set_pixel(7, 0, 40, 0)
           show()

      else:
           print "not sure purple"

           set_pixel(0, 40, 0, 40)
           show()
           
      time.sleep(60)
      print "run again"
      time.sleep(1)
