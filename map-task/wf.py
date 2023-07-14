from flytekit import map_task, task, workflow


@task
def squared(value: int) -> int:
    return value**2


@workflow
def my_wf() -> list[int]:
    return map_task(squared)(value=list(range(10)))
