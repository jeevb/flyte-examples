from flytekit import task, workflow, ImageSpec

image = ImageSpec(
    name="imagespec",
    registry="us-east1-docker.pkg.dev/jeev-gcp-test/hello",
    packages=["smart-open[gcs]"],
    apt_packages=["git"],
)


@task(container_image=image)
def my_task() -> str:
    return "hello, world!"


@workflow
def my_wf() -> str:
    return my_task()
