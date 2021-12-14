import glob
import os.path

files = glob.glob("*.mp4")
  for x in files:
    if not os.path.isdir(x):
      filename = os.path.splitext(x) 
    try:
      os.rename(x,filename[0] + '.mp3')
    except:
      pass
