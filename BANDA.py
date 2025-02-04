import os, sys
try:
    __import__("BANDA").security()
except Exception as e:
    exit(str(e))
