# k8s-lab-app

Part of a homelab Kubernetes platform. The app lives in this repo, everything about how it runs in the cluster lives in [k8s-lab-gitops](https://github.com/ivana-koceva/k8s-lab-gitops).

Pushing to `main` builds the image, scans it, pushes it to GHCR, and updates the gitops repo. ArgoCD picks up the change and deploys it. You don't interact with the cluster directly.



## Pipeline

```
test → build → scan → push → update-gitops
```

On a pull request, only `test`, `build`, and `scan` run. Nothing gets pushed to the registry until the PR merges.

On a push to `main`, the full pipeline runs. The `push` job captures the image digest and the `update-gitops` job writes it into `k8s-lab-gitops/workloads/flask-demo/values.yaml`. ArgoCD does the rest.



## Setup

One secret needs to exist in this repo before the pipeline works:

**`GITOPS_PAT`** — a fine-grained personal access token with Contents read/write on `k8s-lab-gitops`. Add it under Settings → Secrets and variables → Actions.

GHCR authentication is handled automatically via `GITHUB_TOKEN`. Make sure the package is set to public after the first push, otherwise k3s can't pull it without an image pull secret.



## Repository structure

```
k8s-lab-app/
├── src/
│   └── app.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── .github/
    └── workflows/
        └── ci.yaml
```


## Related repos

| Repo | What it does |
|------|-------------|
| [k8s-infra](https://github.com/yourusername/k8s-infra) | Provisions the VM and bootstraps the cluster |
| [k8s-lab-gitops](https://github.com/yourusername/k8s-lab-gitops) | Helm charts, ArgoCD Applications, per-app values |
| **k8s-lab-app** | This repo |
