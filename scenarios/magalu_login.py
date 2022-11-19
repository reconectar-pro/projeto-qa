
import unittest

from selenium.webdriver.common.keys import Keys

from webclient import webclient


class TestLoginMagalu(unittest.TestCase):

    def setUp(self):
        webclient.get('https://sacola.magazineluiza.com.br/#/cliente/login/?next=https%3A//www.magazineluiza.com.br/&origin=magazineluiza')
        self.login = webclient.find_element_by_css_selector('.SignupBox input')

    def tearDown(self):
        self.login.clear()

    def test_valida_email_invalido(self):
        self.login.send_keys('asdf')
        self.login.send_keys(Keys.TAB)

        webclient.wait_element_by_css_selector('.FormGroup-errorMessage')

        self.assertEqual('O e-mail não foi digitado corretamente.', webclient.find_element_by_css_selector('.FormGroup-errorMessage').text)

    def test_valida_email_duplicado(self):
        self.login.send_keys('rreimberg@gmail.com')
        self.login.send_keys(Keys.ENTER)

        webclient.wait_element_by_css_selector('.FormGroup-errorMessage')

        self.assertEqual('Já existe uma conta com esse e-mail.', webclient.find_element_by_css_selector('.FormGroup-errorMessage').text)
