import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import OMD32
elif bit=='32bit':
    import OLD64
