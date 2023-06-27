import json
import os
from flytekit import task, workflow


@task
def parse_json() -> dict:
    path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(path) as f:
        return json.load(f)


@workflow
def parse_json_wf() -> dict:
    return parse_json()
