from features.variables import amazon_var
from features.pages import base_page

v = amazon_var
page = base_page

id = "id"
xpath = "xpath"
name = "name"
className = "class"

def queEuAcesseiOMenuTodosComprarPorCategoriaLivros(context):
    page.click(context, xpath, v.btnMenuTodos)
    page.moveToElement(context, xpath, v.txtComprarPorCategoria)
    page.click(context, xpath, v.txtComprarPorCategoria)

    page.moveToElement(context, xpath, v.btnComprarPorCategoria_VerTudo)
    page.click(context, xpath, v.btnComprarPorCategoria_VerTudo)

    page.moveToElement(context, xpath, v.btnComprarPorCategoria_Livros)
    page.click(context, xpath, v.btnComprarPorCategoria_Livros)

def abrirAOpcaoHQsEMangas(context):
    page.click(context, xpath, v.btnComprarPorCategoria_HQSMANGAS)

def devoValidarOTituloDaPagina(context):
    titulo = "Livros de HQs, Mangás, Graphic Novels, Quadrinhos | Amazon.com.br"
    page.validatePageTitle(context, titulo)