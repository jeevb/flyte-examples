from flytekit import Resources, task, workflow


@task(
    requests=Resources(cpu="100m", mem="100Mi", ephemeral_storage="200Mi", gpu="1"),
)
def my_task() -> str:
    return "hello, world!"


@workflow
def my_wf() -> str:
    return my_task()
