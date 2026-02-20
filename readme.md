# Airflow Platform (GitOps + Kubernetes)

This repository defines a GitOps-managed Apache Airflow platform deployed on Kubernetes and synchronized via Argo CD.

The platform emphasizes reproducibility, separation of concerns, and safe DAG development workflows.

---

## 📐 Architecture Overview

### Key Characteristics

- Airflow is deployed to Kubernetes from `/gitops` and managed by **Argo CD**
- Core Airflow components run in their own namespace
- Postgres is deployed separately from `/postgres` and managed independently by **Argo CD**
- Airflow is layered on Helm for customization and stability
- Developers can build a local single-container image to test DAGs before merging

---

## 📂 Repository Structure

```
.
├── dags/                   # Airflow Dag Definition Files
├── gitops/                 # Argo CD applications for Airflow
├── postgres/               # Argo CD application for Postgres
├── single_container_build/ # Local Airflow image for DAG testing
└── README.md
```


## 🚀 Deployment Model

### 1. Airflow via GitOps

**Location:** `/gitops`  
**Managed by:** Argo CD  
**Namespace:** `airflow` (example)

Airflow deployments are defined declaratively and synchronized by Argo CD.

#### Benefits

- Git is the source of truth
- Auditable infrastructure changes
- Deterministic cluster state
- Easy rollback

---

### 2. Postgres Separation

**Location:** `/postgres`  
**Managed by:** Argo CD  
**Namespace:** `postgres` (separate from Airflow)

#### Why separate Postgres?

- Independent lifecycle and upgrades
- Reduced blast radius
- Backup and restore isolation
- Avoids tight coupling with Airflow Helm chart

---

### 3. Helm Layering Strategy

Airflow is deployed using Helm with custom overlays.

#### Why Helm layering?

- Bitnami Postgres integration broke compatibility
- External Postgres management is required
- Default Celery workers are not desired
- Greater control over executor behavior and scaling

#### Customizations include

- External Postgres connection
- Executor configuration
- Worker model overrides
- Resource tuning

---

## ⚙️ Executor Choice: KubernetesExecutor

### Reasons

- Pod Isolation
- Ability to Orchestrate any container based workload

---

## 🧪 Local DAG Testing

Developers can test DAGs locally using the single-container build.

### Location

`/single_container_build`

### Purpose

- Build a single Docker image with DAGs baked in
- Run Airflow locally to validate DAG behavior
- Catch dependency/import errors before merge

### Example

```bash
docker build -t my_image_name -f ./single_container_build/Dockerfile ./
docker run -p 8080:8080 my_image_name
```

### ⚠️ Important Notes

- Behavior may differ from Kubernetes runtime
- DAGs cannot execute on the k3s cluster until merged
- Argo CD must sync changes before cluster execution
- Local runs use a simplified environment

---

## 🔄 Developer Workflow

1. Create a feature branch.
2. Build and run the local single-container Airflow image (/single_container_build).
3. Validate DAG behavior in the Airflow UI. 
4. Commit DAG changes.
5. Push the branch and open a PR.
6. Build and push the production Airflow image to Docker Hub, tagged with a unique identifier (e.g., the Git commit SHA).
7. Update /gitops/airflow/values.yaml to reference that new image tag.
8. Commit the values.yaml change to the same PR (or a separate “release” PR).
9. Merge PR to main.
10. Argo CD syncs and deploys by reconciling the previous tag → new tag declared in Git.
11. Airflow pods restart with the new image and the DAGs become available/runnable in Kubernetes.

Make sure to use immutable tags: SHA values
---
