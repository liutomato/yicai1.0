import traceback

try:
    i=1/0
except :
    print(traceback.format_exc())