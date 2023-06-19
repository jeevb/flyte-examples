from flytekit import task, workflow


@task
def my_task() -> str:
    return "hello, world!"


@workflow
def my_wf() -> str:
    return my_task()
