# Osprey

A simple todo app that allow recurring tasks to be setup.

## Deploying

When running the container, make sure to pass in the environment variables:

```bash
docker run -d -p 8000:8000 -e GH_REPO=<GitHub repo with the list YAML inside it> -e GH_TOKEN=<GitHub token for the aforementioned repo> osprey:latest
```
