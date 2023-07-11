import ray
import time

from flytekit import task
from flytekitplugins.ray import RayJobConfig, WorkerNodeConfig


@ray.remote
def compute_squared(value: int) -> int:
    time.sleep(5)
    return value**2


@task(
    task_config=RayJobConfig(
        worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=1)],
    )
)
def ray_task(n: int) -> list[int]:
    return ray.get([compute_squared.remote(i) for i in range(n)])
