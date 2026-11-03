import logging

logging.basicConfig(level=logging.DEBUG)

x = 30
y = 40

logging.debug("Values: %s, %s", x, y)
print(x + y)
