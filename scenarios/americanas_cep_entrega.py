
import unittest

from selenium.webdriver.common.keys import Keys

from webclient import webclient


class TestLoginMagalu(unittest.TestCase):

    def setUp(self):
        webclient.get('https://www.americanas.com.br/produto/4944366093?pfm_carac=camiseta&pfm_index=9&pfm_page=search&pfm_pos=grid&pfm_type=search_page&offerId=625fee8e87c00289c21da0b7&tamanho=10&cor=Verde&tecido=Dry&condition=NEW')

    def test_cep_acre(self):
        cep = webclient.find_element_by_name('cep')
        cep.send_keys('69950-000')
        cep.send_keys(Keys.ENTER)

    # def tearDown(self):
    #     self.login.clear()

    # def test_valida_email_invalido(self):
    #     self.login.send_keys('asdf')
    #     self.login.send_keys(Keys.TAB)

    #     webclient.wait_element_by_css_selector('.FormGroup-errorMessage')

    #     self.assertEqual('O e-mail não foi digitado corretamente.', webclient.find_element_by_css_selector('.FormGroup-errorMessage').text)

    # def test_valida_email_duplicado(self):
    #     self.login.send_keys('rreimberg@gmail.com')
    #     self.login.send_keys(Keys.ENTER)

    #     webclient.wait_element_by_css_selector('.FormGroup-errorMessage')

    #     self.assertEqual('Já existe uma conta com esse e-mail.', webclient.find_element_by_css_selector('.FormGroup-errorMessage').text)
