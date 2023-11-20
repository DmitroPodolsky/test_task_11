import re
from telethon.tl.types import Message, User
from abc import ABC, abstractmethod


class CapchaSolver(ABC):
    """Abstract base class for captcha solvers"""

    @abstractmethod
    async def solve_capcha(self, capcha_message: Message, user: User) -> None:
        """This function detects captcha type and solves it if nessessary, should be overriden in child classes
        :capcha_message: Message object with captcha
        :user: User object of user who got captcha
        :returns: None
        """
        pass


class ShieldyCapchaSolver(CapchaSolver):
    """Class for solving captcha from Shieldy bot"""

    async def solve_capcha(self, capcha_message: Message, user: User) -> None:
        if (
            f"{user.first_name} {user.last_name}" in capcha_message.message
            or user.username in capcha_message.message
        ):
            # Check if it's a math captcha and solve it if it is
            task = re.search(r"(\(\d\s?\+\s?\d\)).*", capcha_message.message)
            if task:
                task_str = task.group(1)
                task_str = task_str.replace(" ", "").replace("(", "").replace(")", "")
                task_list = task_str.split("+")
                task_list = [int(i) for i in task_list]
                result = sum(task_list)
                await capcha_message.reply(str(result))
            # Here should be code for solving other types of captcha, possibly by splitting this function into several functions for each type of captcha
            # This is a solid chunk of work, and though it's out of scope of this test task, it's subject to be paid for if you want to do it


class RosaCapchaSolver(CapchaSolver):
    """Class for solving captcha from Rosa bot"""

    async def solve_capcha(self, capcha_message: Message, user: User) -> None:
        """This function detects captcha type and solves it if nessessary
        :capcha_message: Message object with captcha
        :user: User object of user who got captcha
        :returns: None
        """
        if (
            user.first_name in capcha_message.message
            or user.last_name in capcha_message.message
            or user.username in capcha_message.message
        ):
            # Check if it's a button captcha and solve it if it is
            CAPTCHA_BUTTON_STRING = "не бот"
            for button_row in capcha_message.buttons:
                for button in button_row:
                    if CAPTCHA_BUTTON_STRING in button.text.lower():
                        await button.click()
                        break
            # Here should be code for solving other types of captcha, possibly by splitting this function into several functions for each type of captcha
            # This is a solid chunk of work, and though it's out of scope of this test task, it's subject to be paid for if you want to do it


handlers_bots = {
    771096498: ShieldyCapchaSolver(),
    609517172: RosaCapchaSolver(),
}  # Dictionary of bots and their captcha solvers, replaces the database of bots, as it's not needed for this task
