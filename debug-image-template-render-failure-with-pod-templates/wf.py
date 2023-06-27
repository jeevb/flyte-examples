import os
from flytekit import task, workflow


@task(container_image="{{.image.demo.fqn}}:{{.image.demo.version}}")
def my_task() -> str:
    value = os.environ["FOO"]
    return f"hello, {value}!"


@workflow
def my_wf() -> str:
    return my_task()
