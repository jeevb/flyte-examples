# Usage

1. Update Flyte sandbox config at `~/.flyte/sandbox/config.yaml` to include:
```
> cat ~/.flyte/sandbox/config.yaml
plugins:
  k8s:
    default-pod-template-name: default
```

2. Start a new sandbox:
```
flytectl demo start
```
or reload an existing one:
```
flytectl demo reload
```

3. Apply pod template:
```
kubectl --context flyte-sandbox apply -f pod_template.yaml
```

4. Register workflow:
```
pyflyte register --image demo=cr.flyte.org/flyteorg/flytekit:py3.10-1.7.0 wf.py
```

5. Launch the workflow from console.
