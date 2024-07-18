#Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec

import time

def retry(x):
  def retry_interval():
    for i in range(3):
      x()
      time.sleep(3)

  return retry_interval

@retry
def retry_time():
  time_now = time.time()
  print(time_now)

retry_time()