from re import A
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

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

    # html = """
    #     <h1>Inicio</h1>
    #     <p>Años hasta el 2050:</p>
    #     <ul>
    # """
    # year = 2021
    # while year <= 2050:
    #     if year % 2 == 0:
    #         html += f"<li>{str(year)}</li>"
    #     year += 1
    
    # html += "</ul>"

    year = 2021
    hasta = range(year, 2051)

    nombre = "Ruben"
    lenguajes = ['Javascript', 'Python', 'PHP', 'C']
    # lenguajes = []

    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta desde la vista',
        'nombre': nombre,
        'lenguajes' : lenguajes,
        'years': hasta
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('contacto', nombre="Ruben", apellidos="Castillo")

    lista = ['Python', 'Javascript', 'PHP', 'C']

    return render(request, 'pagina.html', {
        'texto': '',
        'lista': lista
    })

def contacto(request, nombre="", apellidos=""):
    html=""
    if nombre and apellidos:
        html += "El nombre completo es:"
        html += f"<h3>{nombre} {apellidos}</h3>"
    # return HttpResponse(layout+f"<h2>Contacto {nombre} {apellidos}</h2>"+html)
    return render(request, 'contacto.html', {
        'nombre': nombre,
        'apellidos': apellidos,
        'title': 'Contacto'
    })

def sesion(request):
    nombre = 'Ruben'
    apellido = 'Castillo'
    return render(request, 'sesion.html', {
        'nombre': nombre,
        'apellido': apellido,
        'title': f"{nombre} {apellido}"
    })

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()

        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido guardar el articulo</h2>")


    # return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

def create_article(request):

    return render(request, 'create_article.html')

def create_full_article(request):

    if request.method == "POST":
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']


            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            #Crear mensaje flash (sesión que solo se muestra una vez)
            messages.success(request, f"Has creado correctamente el articulo {articulo.id}")

            return redirect("articulos")
    

    formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })

def articulo(request):
    try:
        articulo = Article.objects.get(title="Titulo de Prueba", public=False)
        response = f"Articulo: {articulo.title}"
    except:
        response = "Articulo no encontrado"


    return HttpResponse(response)

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado: {articulo.title} - {articulo.content}")

def articulos(request):
    # articulos = Article.objects.order_by('id')[0:2]
    articulos = Article.objects.all()

    # articulos = Article.objects.filter(title__contains="articulo")

    #AND
    # articulos = Article.objects.filter(id__lte=5, title__contains="articulo")

    #OR
    # articulos = Article.objects.filter(
    #     Q(title__contains = "2") | Q(title__contains = "3")
    # )

    # articulos = Article.objects.filter(
    #     title="Articulo vacio"
    # ).exclude(
    #     public=False
    # )

    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo vacio' AND public='1'")

    return render(request, 'articulos.html', {
        'articulos': articulos
    })


def borrar_articulo(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')