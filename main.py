from scenary.base import BaseScenary
from scenary.step_1 import Step1


class Command:
    step: list[BaseScenary]

    def run(self):
        self._set_default()
        while self.step:
            try:
                self._run()
            except Exception:
                self.step.pop()

    def _set_default(self):
        self.step = [Step1()]

    def _run(self):
        if (step := self.step[-1].make_step()) not in self.step:
            self.step.append(step)
        if step is None:
            self._set_default()


Command().run()
