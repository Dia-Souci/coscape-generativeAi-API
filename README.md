## How to run

- create a virtual env `python -m venv .venv`
- activate virtual env `.venv\Scripts\activate` (windows) or `source .venv\bin\activate` (linux)
- install requirements `pip install -r requirements.txt`
- create `.env` file using `.env.example` template
- run server `uvicorn main:app --reload` or directly run `run.sh` (linux) or `run.bat` (windows)
- check api documentation `localhost:8000/docs`

# coscape-generativeAi-API
