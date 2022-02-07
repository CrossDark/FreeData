import os
import re

from UNKnownDB.DB import LocalDB

with open('./setup.py', 'r+') as setup:
    setup.seek(0, 0)
    read = setup.read()
    find = re.findall('version=(.+?),', read)
    v_id = float(eval(find[0].replace('.', '')))
    setup.seek(0, 0)
    num = str(v_id + 1)
    writing = read.replace(find[0], "'" + num[0] + '.' + num[1] + '.' + num[2] + "'")
    setup.write(writing[:-1])
os.system('python3 setup.py sdist bdist_wheel')
os.system('twine upload dist/* --u CleverCreator --p Bitjop-byfbeg-3sazry')
db = LocalDB('')
db.delete_all('./dist')

                