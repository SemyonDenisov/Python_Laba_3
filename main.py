import json
import argparse
from Validator.ValidatorModule import Validator, Record
import random
import pickle

# parser = argparse.ArgumentParser(description='Validator')
# parser.add_argument('indir', type=str, help='Input dir')
# parser.add_argument('outdir', type=str, help='Output dir')
# args = parser.parse_args()
# print(args.indir)
# path = str(args.indir)
path = r'C:\Users\Senya\PycharmProjects\pythonProject\107.txt'
path_to_save = r'C:\Users\Senya\PycharmProjects\Python_Laba_3\text.txt'
path_to_save_1 = r'C:\Users\Senya\PycharmProjects\Python_Laba_3\text1.pickle'
loaded_data = json.load(open(path))
records_1 = []
for item in loaded_data:
    records_1.append(Record(item))
Validator_1 = Validator(records_1)
Validator_1.validate()
Validator_1.save(path_to_save)
loaded_valid_data = json.load(open(path_to_save))
records_2 = []
for item in loaded_valid_data:
    records_2.append(Record(item))
Validator_2 = Validator(records_2)
choice_dct = {1: 'height', 2: 'snils', 3: 'passport_number', 4: 'work_experience'}
key = random.randint(1, 4)
result = Validator_2.validate_by_mergesort(choice_dct[int(key)])
records_3 = []
for item in result:
    records_3.append(Record(item))
Validator_3 = Validator(records_3)
Validator_3.save_pickle(path_to_save_1)
objects = []
with (open(path_to_save_1, "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
loaded_records = []
for rec in objects:
    loaded_records.append(rec.data)
dumps_records = []
for rec in Validator_3.return_records():
    dumps_records.append(rec.data)
print(loaded_records == dumps_records)
