#!/usr/bin/python3
#from models import storage
#from models.base_model import BaseModel

#all_objs = storage.all()
#print("-- Reloaded objects --")
#for obj_id in all_objs.keys():
#    obj = all_objs[obj_id]
#    print(obj)

#print("-- Create a new object --")
#my_model = BaseModel()
#my_model.name = "My_First_Model"
#my_model.my_number = 89
#my_model.save()
#print(my_model)

#!/usr/bin/python3
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

fs = FileStorage()
file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass
try:
    os.remove(file_path)
except:
    pass
try:
    fs._FileStorage__objects.clear()
except:
    pass
ids = []

# First create
for i in range(1):
    bm = BaseModel()
    bm.updated_at = datetime.utcnow()
    fs.new(bm)
    ids.append(bm.id)

try:
    os.remove(file_path)
except:
    pass
fs.save()
try:
    fs._FileStorage__objects.clear()
except:
    pass
fs.reload()

all_reloaded = fs.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload 1")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing 1 {}".format(id))

from models import storage
storage.reload()

# Second create
for i in range(2):
    bm = BaseModel()
    bm.save()
    ids.append(bm.id)
try:
    os.remove(file_path)
except:
    pass
storage.save()
try:
    fs._FileStorage__objects.clear()
except:
    pass
storage.reload()

all_reloaded = storage.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload 2")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing 2 {}".format(id))

try:
    os.remove(file_path)
except Exception as e:
    pass
