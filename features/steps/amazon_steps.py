from behave import given, when, then
from features.variables import amazon_var
from features.pages import base_object

v = amazon_var
p = base_object

base_url = 'https://www.amazon.com.br/'

@given(u'Que eu acessei o menu Todos - Comprar Por Categoria - Livros')
def step_impl(context):
    context.web.get(base_url)
    p.queEuAcesseiOMenuTodosComprarPorCategoriaLivros(context)

@given(u'Abrir a opcao HQs e Mangas')
def step_impl(context):
    p.abrirAOpcaoHQsEMangas(context)

@then(u'Devo validar o titulo da pagina')
def step_impl(context):
    p.devoValidarOTituloDaPagina(context)
