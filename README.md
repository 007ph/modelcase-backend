python -m nuitka run.py --onefile --output-filename=backend.exe --remove-output --disable-console   

pyinstaller build-hello.spec


flask run

waitress-serve run:app

waitress-serve --host 127.0.0.1 --port 3000 run:app




https://hellowac.github.io/uv-zh-cn/guides/projects/

uv init

uv add

uv remove

uv pip compile pyproject.toml -o requirements.txt


uv run