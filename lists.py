#!/usr/bin/env python3
# by lgarciaorozco6@gmail.com
# License GNU/GPL
# 30/10/23

# Posiciones especificas
import numpy as np

l = [12,34,56,78,90]

print(l[3],l[-3],l[:3],l[-5:],l[::2])

arr = np.array(l)
print(f'Array: {arr}')
