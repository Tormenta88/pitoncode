import time
import readchar
"""
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("{0}:{1}:{2}".format(int(hours),int(mins),sec))

#input("Press Enter to start")
if character == " ":
    start_time = time.time()


#input("Press Enter to stop")
if character == "b":
    end_time = time.time()


time_lapsed = end_time - start_time
time_convert(time_lapsed)
"""
character = readchar.readchar()
while character != "q":
    character = readchar.readchar()
    print(character)
    time.sleep(1)
    