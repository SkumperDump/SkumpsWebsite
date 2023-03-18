import pytest
import utils

class TestMarkdownToHtml:
    path = 'app/static/md/contact.md'
    contactStr = '* Philip Scott Wallace (he/him)\n* 3414 NW Bryce Canyon Ln\n* Bend, OR 97703\n* Call me at: [1-210-845-3963](tel:+12108453963)\n* Email me at: [philipswallace1@gmail.com](mailto:philipswallace1@gmail.com)\n* Find me on github: [https://github.com/SkumperDump](https://github.com/SkumperDump)\n'

    def test_1(self):
        assert utils.mdToStr(self.path)

    # This test will fail if contact.md is moved or changed
    def test_2(self):
        assert utils.mdToStr(self.path) == self.contactStr

    def test_3(self):
        import markdown
        assert markdown.markdown(utils.mdToStr(self.path)) == markdown.markdown(self.contactStr)
