from scenary.base import BaseScenary
from scenary.step_1 import Step1


class Command:
    step: BaseScenary = Step1()


    def run(self):
        while self.step:
            self.step = self.step.make_step()

Command().run()
