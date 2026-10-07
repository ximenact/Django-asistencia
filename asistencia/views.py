from django.shortcuts import render, redirect, get_object_or_404
from .models import asistencia as Asistencia


def crear(request):
    if request.method == 'POST':
        registro = Asistencia(
            tipo_documento=request.POST["tipo_documento"],
            documento=request.POST["documento"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            whatsapp=request.POST["whatsapp"],
            fecha=request.POST["fecha"],
            asistio=request.POST.get("asistio") == "on",
        )

        registro.save()

        return redirect("listar")

    return render(request, "formulario.html")


def listar(request):
    asistencias = Asistencia.objects.all()

    return render(
        request,
        "lista.html",
        {"asistencia": asistencias}
    )


# VER
def detalle(request, id):
    registro = get_object_or_404(Asistencia, id=id)

    return render(
        request,
        "detalle.html",
        {"asistencia": registro}
    )


def editar(request, id):
    registro = get_object_or_404(Asistencia, id=id)

    if request.method == "POST":

        registro.tipo_documento = request.POST["tipo_documento"]
        registro.documento = request.POST["documento"]
        registro.nombre = request.POST["nombre"]
        registro.apellido = request.POST["apellido"]
        registro.whatsapp = request.POST["whatsapp"]
        registro.fecha = request.POST["fecha"]
        registro.asistio = request.POST.get("asistio") == "on"

        registro.save()

        return redirect("listar")

    return render(
        request,
        "formulario.html",
        {"asistencia": registro}
    )


def eliminar(request, id):
    registro = get_object_or_404(Asistencia, id=id)

    registro.delete()

    return redirect("listar")