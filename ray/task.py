import time

import ray
from flytekit import ImageSpec, Resources, task
from flytekitplugins.ray import RayJobConfig, WorkerNodeConfig

image = ImageSpec(
    name="imagespec",
    registry="us-east1-docker.pkg.dev/dogfood-gcp-dataplane/flytesnacks/flyte-examples-ray",
    packages=["flytekitplugins-ray", "pydantic<2"],
)


@ray.remote
def compute_squared(value: int) -> int:
    result = value * value
    print(f"{value} * {value} = {result}")
    time.sleep(30)
    return result


@task(
    environment={"RAY_DEDUP_LOGS": "0"},
    limits=Resources(cpu="1", mem="1Gi"),
    task_config=RayJobConfig(
        worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=1)],
    ),
    container_image=image,
)
def ray_task(n: int) -> list[int]:
    return ray.get([compute_squared.remote(i) for i in range(n)])
