__doc__ = "Przykładowa dokumentacja tego pliku"

import os


def function():
    file_name = os.path.basename(__file__)
    print(f"Hello from module '{__package__}' in file named: '{file_name}'")
