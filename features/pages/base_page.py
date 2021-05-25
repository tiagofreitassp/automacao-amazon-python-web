from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click(context, tipoEl, el):
    if tipoEl == "ID" or tipoEl.__eq__("id"):
        context.web.find_element_by_id(el).click()
    elif tipoEl == "NAME" or tipoEl.__eq__("name"):
        context.web.find_element_by_name(el).click()
    elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
        context.web.find_element_by_xpath(el).click()
    elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
        context.web.find_element_by_class_name(el).click()
    sleep(1)

def moveToElement(context, tipoEl, el):
    sleep(1)
    if tipoEl == "ID" or tipoEl.__eq__("id"):
        elemento = context.web.find_element_by_id(el)
        context.web.execute_script("arguments[0].scrollIntoView(true);", elemento)
    elif tipoEl == "NAME" or tipoEl.__eq__("name"):
        elemento = context.web.find_element_by_name(el)
        context.web.execute_script("arguments[0].scrollIntoView(true);", elemento)
    elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
        elemento = context.web.find_element_by_xpath(el)
        context.web.execute_script("arguments[0].scrollIntoView(true);", elemento)
    elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
        elemento = context.web.find_element_by_class_name(el)
        context.web.execute_script("arguments[0].scrollIntoView(true);", elemento)
    sleep(1)

def send(context, tipoEl, el, texto):
    if tipoEl == "ID" or tipoEl.__eq__("id"):
        context.web.find_element_by_id(el).send_keys(texto)
    elif tipoEl == "NAME" or tipoEl.__eq__("name"):
        context.web.find_element_by_name(el).send_keys(texto)
    elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
        context.web.find_element_by_xpath(el).send_keys(texto)
    elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
        context.web.find_element_by_class_name(el).send_keys(texto)
    sleep(1)

def validateTextElement(context, tipoEl, el, texto):
    sleep(1)
    if tipoEl == "ID" or tipoEl.__eq__("id"):
        txt = context.web.find_element_by_id(el).text
        assert texto == txt
    elif tipoEl == "NAME" or tipoEl.__eq__("name"):
        txt = context.web.find_element_by_name(el).text
        assert texto == txt
    elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
        txt = context.web.find_element_by_xpath(el).text
        assert texto == txt
    elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
        txt = context.web.find_element_by_class_name(el).text
        assert texto == txt
    sleep(1)

def validatePageTitle(context, texto):
    sleep(1)
    assert texto == getPageTitle(context)
    sleep(1)

def getPageTitle(context):
    titulo = context.web.title
    print('Titulo da página: {}'.format(titulo))
    return titulo

def scrollDown(context, altura):
    sleep(1)
    if altura == "100" or altura.__eq__("100"):
        context.web.execute_script("window.scrollTo(0, 100)")
    elif altura == "200" or altura.__eq__("200"):
        context.web.execute_script("window.scrollTo(0, 200)")
    elif altura == "300" or altura.__eq__("300"):
        context.web.execute_script("window.scrollTo(0, 300)")
    elif altura == "400" or altura.__eq__("400"):
        context.web.execute_script("window.scrollTo(0, 400)")
    elif altura == "550" or altura.__eq__("550"):
        context.web.execute_script("window.scrollTo(0, 550)")
    sleep(1)

def scrollDownTheEndOfThePage(context):
    sleep(1)
    context.web.execute_script("window.scrollTo (0, document.body.scrollHeight)")
    sleep(1)

    def waitElementClickable(context, tipoEl, el):
        button = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dismiss')))
        button.click()

        if tipoEl == "ID" or tipoEl.__eq__("id"):
            element = WebDriverWait(context.web, 15).until(EC.element_to_be_clickable((By.id, el)))
            element.click()
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            element = WebDriverWait(context.web, 15).until(EC.element_to_be_clickable((By.name, el)))
            element.click()
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            element = WebDriverWait(context.web, 15).until(EC.element_to_be_clickable((By.xpath, el)))
            element.click()
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            element = WebDriverWait(context.web, 15).until(EC.element_to_be_clickable((By.className, el)))
            element.click()
        sleep(1)

    def checkIfElementIsVisible(context, tipoEl, el):
        sleep(1)
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            context.web.find_element_by_id(el).is_displayed()
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            context.web.find_element_by_name(el).is_displayed()
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            context.web.find_element_by_xpath(el).is_displayed()
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            context.web.find_element_by_class_name(el).is_displayed()
        sleep(1)

    def switchToFrame(context, tipoEl, el):
        sleep(3)
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            iframe = context.web.find_element_by_id(el)
            context.web.switch_to.frame(iframe)
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            iframe = context.web.find_element_by_name(el)
            context.web.switch_to.frame(iframe)
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            iframe = context.web.find_element_by_xpath(el)
            context.web.switch_to.frame(iframe)
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            iframe = context.web.find_element_by_class_name(el)
            context.web.switch_to.frame(iframe)
        sleep(1)

    def returnToWindowPrincipal(context):
        sleep(2)
        # Retorna para a janela principal (fora do iframe)
        context.web.switch_to.default_content()
        sleep(2)