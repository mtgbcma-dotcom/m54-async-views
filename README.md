# Contador de tempo com Django

Atividade do módulo 54 do curso Full Stack Python da EBAC.

Criei um projeto Django com uma view assíncrona para contar o tempo.
A duração pode ser escolhida entre 1 e 10 segundos. A view aguarda um segundo
em cada etapa com asyncio.sleep, registra o tempo acumulado e mostra o resultado
no navegador ao terminar.

Usei perf_counter para medir o intervalo da contagem. O servidor Uvicorn
executa a aplicação pela interface ASGI.

## Executar no Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe -m uvicorn config.asgi:application --reload
```

Página inicial: http://127.0.0.1:8000/

Contagem de 3 segundos: http://127.0.0.1:8000/contador/?segundos=3

## Verificação de concorrência

Com o servidor rodando, abra outro terminal na pasta do projeto:

```powershell
.\.venv\Scripts\python.exe verificar_concorrencia.py
```

O script utiliza HTTPX e asyncio.gather para enviar duas requisições de
3 segundos simultaneamente. O tempo total tende a ficar próximo de 3 segundos,
em vez de 6. A duração exata depende da máquina e da carga do servidor.

## Organização

- contador/views.py: página inicial e view assíncrona contador_tempo.
- contador/urls.py: endereços das páginas.
- config/asgi.py: entrada ASGI.
- templates/: estrutura e páginas de início e resultado.
- verificar_concorrencia.py: chamadas simultâneas com HTTPX.

A espera da contagem usa await asyncio.sleep, que permite ao event loop
executar outras tarefas enquanto aguarda. A resposta HTML é enviada após a
contagem terminar. Não há atualização ao vivo de cada segundo no navegador.

Branch da atividade: async-views.
