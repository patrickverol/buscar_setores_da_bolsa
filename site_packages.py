import site

print(site.getsitepackages())

import sys

for path in sys.path:
    print(path)
