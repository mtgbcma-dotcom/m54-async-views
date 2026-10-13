import asyncio
from time import perf_counter

import httpx


async def verificar():
    url = "http://127.0.0.1:8000/contador/?segundos=3"

    try:
        async with httpx.AsyncClient(timeout=20, trust_env=False) as cliente:
            inicio = perf_counter()
            respostas = await asyncio.gather(
                cliente.get(url),
                cliente.get(url),
            )
            duracao = perf_counter() - inicio

            for numero, resposta in enumerate(respostas, start=1):
                resposta.raise_for_status()
                if "Contagem concluída" not in resposta.text:
                    raise RuntimeError("A resposta não contém o resultado do contador.")
                print(f"Requisição {numero}: HTTP {resposta.status_code}")

            print(f"Tempo total das duas requisições: {duracao:.2f} segundos")
            print("Cada contagem espera 3 segundos. Com execução concorrente, o total tende a ficar próximo de 3 segundos, em vez de 6.")
    except httpx.HTTPError as erro:
        print(f"Não foi possível concluir a verificação: {erro}")
        print("Confira se o servidor Uvicorn está rodando em http://127.0.0.1:8000/.")
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(verificar())
