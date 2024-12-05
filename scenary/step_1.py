from scenary.base import BaseScenary
from scenary.step2.create import StepCreate
from scenary.step2.delete import StepDelete
from scenary.step2.all import StepAll
from scenary.step2.edit import StepEdit
from scenary.step2.searche import StepSearcher


class Step1(BaseScenary):
    def make_step(self):
        match input(("Выберите действие:\n"
                    "\t[C|Д] Добавить\n"
                     "\t[D|У] Удалить\n"
                     "\t[S|Н] Найти\n"
                     "\t[A|В] Все\n"
                     "\t[E|Р] Редактировать\n"
                     "-> ")).upper():
            case "C" | "CREATE" | "ДОБАВИТЬ" | "Д":
                return StepCreate()
            case "D" | "DELETE" | "УДАЛИТЬ" | "У":
                return StepDelete()
            case "S" | "SEARCH" | "НАЙТИ" | "Н":
                return StepSearcher()
            case "A" | "ALL" | "ВСЕ" | "В":
                return StepAll()
            case "E" | "EDIT" | "РЕДАКТИРОВАТЬ" | "Р":
                return StepEdit()
            case _:
                print("Неправильный ввод")
                return self
