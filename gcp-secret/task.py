from flytekit import Secret, current_context, task

SECRET_GROUP = "mainsecret"
SECRET_GROUP_VERSION = "1"


@task(
    secret_requests=[
        Secret(group=SECRET_GROUP, group_version=SECRET_GROUP_VERSION),
    ],
)
def my_task() -> str:
    return current_context().secrets.get(
        SECRET_GROUP, group_version=SECRET_GROUP_VERSION
    )
