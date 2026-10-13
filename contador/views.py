import asyncio
from time import perf_counter

from asgiref.sync import sync_to_async
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET


def inicio(request):
    return render(request, "inicio.html")


@require_GET
async def contador_tempo(request):
    try:
        segundos = int(request.GET.get("segundos", "3"))
    except ValueError:
        return HttpResponseBadRequest("Informe um número inteiro entre 1 e 10.")

    if not 1 <= segundos <= 10:
        return HttpResponseBadRequest("Informe um número inteiro entre 1 e 10.")

    inicio_contagem = perf_counter()
    registros = []

    for segundo in range(1, segundos + 1):
        await asyncio.sleep(1)
        registros.append({
            "segundo": segundo,
            "tempo": perf_counter() - inicio_contagem,
        })

    tempo_total = perf_counter() - inicio_contagem
    contexto = {
        "segundos": segundos,
        "tempo_total": tempo_total,
        "registros": registros,
    }
    return await sync_to_async(render, thread_sensitive=True)(
        request, "resultado.html", contexto
    )
