import os, sys
try:
    __import__("somo").security()
except Exception as e:
    exit(str(e))
