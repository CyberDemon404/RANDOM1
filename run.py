import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from RANDOM64 import srj
    srj()
elif bit == '32bit':
    from RANDOM32 import srj
    srj()
