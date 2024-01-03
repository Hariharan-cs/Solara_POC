**Steps to run the project**

Clone the project and go inside the project file called **Solara_POC**

**For first time**

1. python3 -m venv solara-env

2. source solara-env/bin/activate

3. pip install -r requirements.txt

4. export OPENAI_API_KEY=OPENAI_API_KEY

5. solara run ./multipage-demo




**For upcoming run**

1. source solar-env/bin/activate

2. solara run ./multipage-demo




**Kill port if required**

1. kill -9 $(lsof -ti:8765)
