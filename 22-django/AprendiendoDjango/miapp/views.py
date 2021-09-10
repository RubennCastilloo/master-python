from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#MVC = Modelo Vista Controlador -> acciones (metodos)
#MVT = Modelo Template Vista -> acciones (metodos)

layout = """
<h1>Sitio web con Django | Ruben Castillo</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
     <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
""";

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

    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+"""<h1>Hola mundo con Django!!</h1>
    <h2>Mi nombre es Ruben Castillo</h2>""")

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('contacto', nombre="Ruben", apellidos="Castillo")

    return HttpResponse(layout+"""
        <h1>Página de mi web</h1>
        <p>Creado por Ruben Castillo</p>
    """)

def contacto(request, nombre="", apellidos=""):
    html=""
    if nombre and apellidos:
        html += "El nombre completo es:"
        html += f"<h3>{nombre} {apellidos}</h3>"
    return HttpResponse(layout+f"<h2>Contacto {nombre} {apellidos}</h2>"+html)