from cms.test.js_testcases import BaseJavascriptTestCase


class JavascriptTestCase(BaseJavascriptTestCase):
    def test_01_insert_into_url(self):
        files = [self._get_file_path('js', 'tools.js')]
        base_snippet = "insert_into_url('%s', '%s', '%s')"
        tests = [
            ('http://www.mysite.com', 'edit', '', 'http://www.mysite.com?edit'),
            ('http://www.mysite.com?hello=world', 'edit', '',
             'http://www.mysite.com?hello=world&edit'),
            ('http://www.mysite.com?hello=world&goodbye=universe', 'edit', '',
             'http://www.mysite.com?hello=world&goodbye=universe&edit'),
            ('http://www.mysite.com#myanchor', 'edit', '',
             'http://www.mysite.com?edit#myanchor'),
            ('http://www.mysite.com?hello=world#myanchor', 'edit', '',
             'http://www.mysite.com?hello=world&edit#myanchor'),
            ('http://www.mysite.com?hello=world&goodbye=universe#myanchor',
             'edit', '',
             'http://www.mysite.com?hello=world&goodbye=universe&edit#myanchor'),
            ('http://www.mysite.com', 'edit', 'on', 'http://www.mysite.com?edit=on'),
            ('http://www.mysite.com?hello=world', 'edit', 'on',
             'http://www.mysite.com?hello=world&edit=on'),
            ('http://www.mysite.com?hello=world&goodbye=universe', 'edit', 'on',
             'http://www.mysite.com?hello=world&goodbye=universe&edit=on'),
            ('http://www.mysite.com#myanchor', 'edit', 'on',
             'http://www.mysite.com?edit=on#myanchor'),
            ('http://www.mysite.com?hello=world#myanchor', 'edit', 'on',
             'http://www.mysite.com?hello=world&edit=on#myanchor'),
            ('http://www.mysite.com?hello=world&goodbye=universe#myanchor',
             'edit', 'on',
             'http://www.mysite.com?hello=world&goodbye=universe&edit=on#myanchor'),
        ]
        for arg1, arg2, arg3, expected in tests:
            output = self._run_javascript(files, base_snippet % (arg1, arg2, arg3))
            self.assertEqual(output, expected)