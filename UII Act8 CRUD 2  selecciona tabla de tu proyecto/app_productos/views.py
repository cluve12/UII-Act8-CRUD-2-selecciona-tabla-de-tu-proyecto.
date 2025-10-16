from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

def index(request):
    productos = Producto.objects.all()
    return render(request, 'app_productos/listar_productos.html', {'productos': productos})

def ver_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'app_productos/ver_producto.html', {'producto': producto})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        disponible = 'disponible' in request.POST
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            disponible=disponible
        )
        return redirect('inicio')
    return render(request, 'app_productos/agregar_producto.html')

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.descripcion = request.POST['descripcion']
        producto.disponible = 'disponible' in request.POST
        producto.save()
        return redirect('inicio')
    return render(request, 'app_productos/editar_producto.html', {'producto': producto})

def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')
    return render(request, 'app_productos/borrar_producto.html', {'producto': producto})