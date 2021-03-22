"""Script to seed database."""

import os
import json
from random import choice, randint
import crud
import model
import server


# os.system('dropdb ')
# os.system('createdb ')

model.connect_to_db(server.app)
model.db.create_all()