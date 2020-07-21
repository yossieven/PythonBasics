# set up a hook to be able to check if a test has failed
import logging
import subprocess
import sys

import pytest
from pytest_reportportal import RPLogger, RPLogHandler


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


# @pytest.fixture(scope="session")
# def rp_logger(request):
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)
#     # Create handler for Report Portal if the service has been
#     # configured and started.
#     if hasattr(request.node.config, 'py_test_service'):
#         # Import Report Portal logger and handler to the test module.
#         logging.setLoggerClass(RPLogger)
#         rp_handler = RPLogHandler(request.node.config.py_test_service)
#         # Add additional handlers if it is necessary
#         console_handler = logging.StreamHandler(sys.stdout)
#         console_handler.setLevel(logging.INFO)
#         logger.addHandler(console_handler)
#     else:
#         rp_handler = logging.StreamHandler(sys.stdout)
#     # Set INFO level for Report Portal handler.
#     rp_handler.setLevel(logging.INFO)
#     return logger


@pytest.fixture(scope="session", autouse=True)
def report_allure(request):
    yield
    p = subprocess.Popen('powershell.exe allure serve C:\\Users\\yosefev\\IdeaProjects\\TheBasics\\Sellenium\\my_allure_results',
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    print(error)
    print("\n")
    print(output)
