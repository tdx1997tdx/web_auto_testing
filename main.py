import pytest
import shutil

if __name__ == '__main__':
    # Get directory name
    try:
        shutil.rmtree("./report")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    pytest.main(["-vs", "--alluredir", "./report/result", "./test_case"])
