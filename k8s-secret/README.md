# Kubernetes Secrets


1. Start sandbox:
```
$ flytectl demo start
```

2. Create secret with:
```
$ kubectl create secret generic user-info \
    --namespace flytesnacks-development \
    --from-literal=user_secret=sosecret \
    --dry-run=client --output yaml | kubectl apply --filename -
```

3. Then run the workflow:
```
$ pyflyte run --remote task.py secret_task
```
