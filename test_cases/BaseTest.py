from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    pass

    def generate_random_email(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "ujjwal" + time_stamp + "gmail.com"