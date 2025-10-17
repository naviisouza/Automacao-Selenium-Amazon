from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")
        self.first_result = (By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
        self.add_to_cart_button = (By.ID, "add-to-cart-button")
        self.cart_icon = (By.ID, "nav-cart")

    def buscar_livro(self, nome_livro):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(nome_livro)
        self.driver.find_element(*self.search_button).click()

    def clicar_primeiro_resultado(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_result)
        )
        self.driver.find_element(*self.first_result).click()

    def adicionar_ao_carrinho(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.add_to_cart_button)
            )
            botao = self.driver.find_element(*self.add_to_cart_button)
            if botao.is_displayed() and botao.is_enabled():
                botao.click()
            else:
                print("Botão 'Adicionar ao carrinho' não está disponível.")
        except Exception as e:
            print("Erro ao adicionar ao carrinho:", e)

    def abrir_carrinho(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        )
        self.driver.find_element(*self.cart_icon).click()
