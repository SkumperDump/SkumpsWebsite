import markdown
import pytest
from .. import utils

def test_mdFileToHtml(self):
    path = '../app/static/md/contact.md'
    assert utils.open_file(path)
