from scenary.base import BaseScenary
from scenary.step2.create import StepCreate


class Step1(BaseScenary):
    def make_step(self):
        while True:
            match input(f"Добавить/Удалить/Найти/Все/Редактировать [C/D/S/A/E]: ").upper():
                case "C" | "CREATE" | "ДОБАВИТЬ" | "Д":
                    return StepCreate()
                case "D" | "DELETE" | "УДАЛИТЬ" | "У":
                    ...
                case "S" | "SEARCH" | "НАЙТИ" | "Н":
                    ...
                case "A" | "ALL" | "ВСЕ" | "В":
                    ...
                case "E" | "EDIT" | "РЕДАКТИРОВАТЬ" | "Р":
                    ...

            print("Неправильный ввод")
