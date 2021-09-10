from django.shortcuts import render, HttpResponse

# Create your views here.
#MVC = Modelo Vista Controlador -> acciones (metodos)
#MVT = Modelo Template Vista -> acciones (metodos)

def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    
    html += "</ul>"

    return HttpResponse(html)

def hola_mundo(request):
    return HttpResponse("""<h1>Hola mundo con Django!!</h1>
    <h2>Mi nombre es Ruben Castillo</h2>""")

def pagina(request):
    return HttpResponse("""
        <h1>Página de mi web</h1>
        <p>Creado por Ruben Castillo</p>
    """)