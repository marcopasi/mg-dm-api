import random

from dmp import dmp

da = dmp.dmp()

history = da.get_file_history("<unique_file_id>")

print history
