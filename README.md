# Template for basic FastAPI on docker

Run locally with
`uvicorn app.main:app --host 0.0.0.0 --port 80`

Build with:
`docker build -t <dockerhub_username>/<dockerhub_project> .`

Then push to dockerhub with:
`docker push <dockerhub_username>/<dockerhub_project>`
