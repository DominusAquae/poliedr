#!/usr/bin/env -S python3 -B

from time import time
from tk_drawer import TkDrawer
from polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["ccc", "cube", "box", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        pol = Polyedr(f"data/{name}.geom")
        print(f"Площадь проекций хороших граней полиэдра : {pol.draw(tk)}")
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()