import pytest

#para ma call nato ang driver
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass