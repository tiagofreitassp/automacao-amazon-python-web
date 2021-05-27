from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
	#context.web = webdriver.Chrome('./drivers/chromedriver')
	context.web = webdriver.Chrome(ChromeDriverManager().install())
	context.web.maximize_window()
	context.web.implicitly_wait(15)

def after_step(context, step):
	print('Teste finalizado')
	 
def after_all(context):
	context.web.quit()
	print('Execução encerrada!')