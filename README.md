**Steps to run the project**

**For first time**

python3 -m venv solara-env

pip install solara

source solar-env/bin/activate

solara run ./multipage-demo




**For upcoming run**

source solar-env/bin/activate

solara run ./multipage-demo




**Kill port if required**

kill -9 $(lsof -ti:8765)
