# Ray + Flyte Example

## Usage

1. Enable the Ray Flyte plugin on the sandbox, by adding the following block to `~/.flyte/sandbox/config.yaml`:
```
plugins:
  ray:
    shutdownAfterJobFinishes: true
    ttlSecondsAfterFinished: 60
tasks:
  task-plugins:
    default-for-task-types:
      container: container
      container_array: k8s-array
      sidecar: sidecar
      ray: ray
    enabled-plugins:
    - container
    - sidecar
    - k8s-array
    - ray
```

2. Start the sandbox:
```
$ flytectl demo start
```

3. Install KubeRay:
```
$ helm repo add kuberay https://ray-project.github.io/kuberay-helm/
$ helm install kuberay-operator kuberay/kuberay-operator --version 0.5.2 --namespace ray-system --create-namespace
$ kubectl rollout status deploy/kuberay-operator -n ray-system -w
```

4. Run the Ray task:
```
$ pyflyte run --remote --image=localhost:30000/ray-example:latest task.py ray_task --n=5
```

5. Teardown the sandbox:
```
$ flytectl demo teardown -v
```
