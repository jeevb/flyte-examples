import ray
import time

from flytekit import task, Resources
from flytekitplugins.ray import RayJobConfig, WorkerNodeConfig


@ray.remote
def compute_squared(value: int) -> int:
    print(f"Computing squared of {value}...")
    time.sleep(5)
    result = value**2
    print(f"Computed squared of {value}: {result}")
    return result


@task(
    limits=Resources(cpu="1", mem="1Gi"),
    task_config=RayJobConfig(
        worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=1)],
    ),
)
def ray_task(n: int) -> list[int]:
    return ray.get([compute_squared.remote(i) for i in range(n)])
