import traceback

try:
    result = 10 / 0
except Exception:
    traceback.print_exc()
