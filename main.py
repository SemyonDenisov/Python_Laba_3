import json
import re
import argparse

from tqdm import tqdm


class Validator:
    """
    Класс Валидатор
    """

    def __init__(self, records):
        """
               Данная функция инициализирует объект класса Record
               Parameters
               ----------
               records : коллекция объектов класса Record
                Attributes:
                ----------
                self.pattern - dict в котором хранятся паттерны для валидации объекта класса Record
                self.dict_errors - dict в котором хранятся число невалидных записей по типам ошибок
                self.valid_count - число валидных записей
                self.invalid_count - число невалидных записей
                self.dict_valid - dict для хранения валидных записей
               """
        self.records = records
        self.pattern = {
            "email": r'^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$',
            "height": r"[1-2].\d{2}",
            "snils": r"\d{11}",
            "passport_number": r"\d{6}",
            "university": r"[a-zA-Zа-яА-ЯёЁ]",
            "work_experience": r"[^a-zA-Zа-яА-ЯёЁ]",
            "political_views": r"[а-яА-ЯёЁ]",
            "worldview": r"[a-zA-Zа-яА-ЯёЁ]",
            "address": r".*?"}
        self.dict_errors = {
            "email": 0,
            "height": 0,
            "snils": 0,
            "passport_number": 0,
            "university": 0,
            "work_experience": 0,
            "political_views": 0,
            "worldview": 0,
            "address": 0}
        self.valid_count: int = 0
        self.invalid_count: int = 0
        self.dict_valid = []

    def validate_by_key(self, record, key: str) -> bool:
        """
          Данная функция инициализирует объект класса Record
          Parameters
          ----------
          record : объект класса Record
          key: ключ по которому будет происходить валидация
           Returns
           -------
           bool:True - если record валиден, False - если record не валиден
          """
        if re.match(self.pattern[key], str(record.data[key])):
            return True
        else:
            self.dict_errors[key] += 1
            return False

    def validate(self):
        """
          Данная функция отвечает за процесс валидации коллекции записей
          Считает количество валидных и невалидных записей а также ведет подсчет невалидных записей по типам ошибок
          Процесс валидации наглядно пока   зывает progressbar
          """
        with tqdm(total=100000) as progressbar:
            for record in self.records:
                counter_valid_part = 0
                for key in record.keys():
                    if self.validate_by_key(record, key):
                        counter_valid_part += 1
                if counter_valid_part == 9:
                    self.valid_count += 1
                    self.dict_valid.append(record)
                else:
                    self.invalid_count += 1
                progressbar.update(1)
        print(self.valid_count, self.invalid_count)
        print(self.dict_errors)

    def save(self):
        """
         Данная функция отвечает за сохранение валидных записей в файл
         Процесс записи в файл наглядно показывает progressbar
         """
        f = open('text.txt', 'w')
        f.write('[' + '\n')
        for record in tqdm(self.dict_valid):
            f.write('\t{' + '\n')
            for key in record.keys():
                f.write('\t\t' + '"' + str(key) + '"' + ': ' +
                        '"' + str(record.data[key]) + '"' + '\n')
            f.write('\t},' + '\n')
        f.write(']')


class Record:
    """
    Класс Запись
    """

    def __init__(self, dct: dict):
        """
         Данная функция инициализирует объект класса Record
         Parameters
         ----------
         dct : dict
           данный dict будет скопирован в объект класаа Record
         """
        self.data = dct

    def keys(self) -> list:
        """
            Данная функция возвращает list состящий из ключей объекта класса Record
            Returns
            -------
            data.keys() - list состящий из ключей объекта класса Record
            """
        return list(self.data.keys())

    def data(self, key):
        """
        Данная функция возвращает значение Record по ключу key
        Returns
        -------
        data[key] - значение Record по ключу key
        """
        return self.data[key]


parser = argparse.ArgumentParser(description='Validator')
parser.add_argument('indir', type=str, help='Input dir')
parser.add_argument('outdir', type=str, help='Output dir')
args = parser.parse_args()
print(args.indir)
path = str(args.indir)
loaded_data = json.load(open(path))
records_1 = []
for item in loaded_data:
    records_1.append(Record(item))
Validator_1 = Validator(records_1)
Validator_1.validate()
Validator_1.save()
