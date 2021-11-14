import json
import re
import pickle

from tqdm import tqdm
from mergesrt.mergesrt import mergesort


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
            "height": r"\b1\.[5-9][0-9]|2\.[0-1][0-9]\b",
            "snils": r"\b\d{11,}\b",
            "passport_number": r"\b\d{6,}\b",
            "university": r"[a-zA-Zа-яА-ЯёЁ]",
            "work_experience": r"^([1-9]?[0-9]|4[0-9])$",
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
        dict_valid = []
        with tqdm(total=100000) as progressbar:
            for record in self.records:
                counter_valid_part = 0
                for key in record.keys():
                    if self.validate_by_key(record, key):
                        counter_valid_part += 1
                if counter_valid_part == 9:
                    self.valid_count += 1
                    dict_valid.append(record)
                else:
                    self.invalid_count += 1
                progressbar.update(1)
        self.records = dict_valid
        print(self.valid_count, self.invalid_count)
        print(self.dict_errors)

    def validate_by_mergesort(self, key):
        list_to_merge = []
        for record in self.records:
            dct = record.data
            list_to_merge.append(dct)
        list_result = mergesort(list_to_merge, key)
        return list_result

    def save(self, path):
        """
         Данная функция отвечает за сохранение валидных записей в файл
         Процесс записи в файл наглядно показывает progressbar
         """
        with open(path, 'w') as f:
            res_list = []
            for record in self.records:
                res_list.append(record.data)
            json.dump(res_list, f, ensure_ascii=False, )

    def save_pickle(self, path):
        """
         Данная функция отвечает за сохранение отсортированных записей в pickle-файл
         """
        with open(path, 'wb') as f:
            for record in self.records:
                pickle.dump(record, f)

    def return_records(self):
        return self.records


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


