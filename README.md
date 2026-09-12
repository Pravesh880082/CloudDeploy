# 🚀 CloudDeploy — Cloud-Native DevOps Deployment Platform

> A production-style DevOps project that automates application testing, Docker image creation, AWS deployment, and Kubernetes-based application delivery using GitHub Actions, Terraform, Docker, AWS EC2, and K3s.

![DevOps](https://img.shields.io/badge/DevOps-Automation-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-K3s-326CE5)
![Terraform](https://img.shields.io/badge/Terraform-Infrastructure-7B42BC)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF)
![Python](https://img.shields.io/badge/Python-3.12-yellow)

---

## 📌 Project Overview

**CloudDeploy** is a cloud-native DevOps deployment platform designed to demonstrate an automated software delivery workflow.

The project takes an application from source code in GitHub and automatically:

1. Runs automated tests
2. Builds a Docker image
3. Transfers the image to an AWS EC2 server
4. Imports the image into K3s
5. Updates the Kubernetes deployment
6. Performs a rolling deployment
7. Verifies that the application is healthy

The project demonstrates practical knowledge of **CI/CD, containerization, infrastructure as code, cloud computing, Linux, and Kubernetes deployment**.

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │       GitHub        │
                         │   Source Code Repo  │
                         └──────────┬──────────┘
                                    │
                                    │ git push
                                    ▼
                         ┌─────────────────────┐
                         │   GitHub Actions    │
                         │      CI/CD          │
                         └──────────┬──────────┘
                                    │
                         ┌──────────▼──────────┐
                         │   Automated Tests    │
                         │       Pytest         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Docker Build     │
                         │  Container Image     │
                         └──────────┬──────────┘
                                    │
                                    │ SSH / SCP
                                    ▼
                 ┌────────────────────────────────────┐
                 │             AWS EC2                 │
                 │          Ubuntu Server              │
                 │                                     │
                 │        ┌──────────────────┐         │
                 │        │   K3s Kubernetes │         │
                 │        │                  │         │
                 │        │  ┌────────────┐  │         │
                 │        │  │ CloudDeploy│  │         │
                 │        │  │    Pod 1   │  │         │
                 │        │  └────────────┘  │         │
                 │        │                  │         │
                 │        │  ┌────────────┐  │         │
                 │        │  │ CloudDeploy│  │         │
                 │        │  │    Pod 2   │  │         │
                 │        │  └────────────┘  │         │
                 │        │                  │         │
                 │        └────────┬─────────┘         │
                 │                 │                   │
                 │          NodePort :30080            │
                 └─────────────────┼────────────────────┘
                                   │
                                   ▼
                            🌐 Live Application
```

---

## 🔄 CI/CD Pipeline

The complete deployment workflow is:

```text
Developer
   │
   │ git push
   ▼
GitHub
   │
   ▼
GitHub Actions
   │
   ├── Run Pytest
   │
   ├── Build Docker Image
   │
   ├── Save Docker Image
   │
   ├── Upload Image to EC2
   │
   ├── Import Image into K3s
   │
   ├── Update Kubernetes Deployment
   │
   ├── Rolling Update
   │
   └── Verify Application Health
   │
   ▼
Live CloudDeploy Application
```

---

## 🛠️ Technology Stack

| Technology           | Purpose                       |
| -------------------- | ----------------------------- |
| **Python / Flask**   | Web application               |
| **Pytest**           | Automated testing             |
| **Docker**           | Application containerization  |
| **Kubernetes / K3s** | Container orchestration       |
| **AWS EC2**          | Cloud compute infrastructure  |
| **Terraform**        | Infrastructure as Code        |
| **GitHub Actions**   | CI/CD automation              |
| **Ubuntu Linux**     | Server operating system       |
| **Git & GitHub**     | Version control               |
| **PowerShell**       | Local development environment |

---

## ✨ Key Features

### 🔹 Automated Testing

Pytest is used to validate the application before deployment.

Tests cover:

* Home page
* Health endpoint
* Status endpoint
* Version endpoint

---

### 🔹 Docker Containerization

The Flask application is packaged into a lightweight Docker image.

The container:

* Uses Python 3.12
* Installs application dependencies
* Runs as a non-root user
* Exposes port `5000`
* Provides a consistent runtime environment

---

### 🔹 Kubernetes Deployment

The application runs on **K3s Kubernetes** with:

* 2 replicas
* RollingUpdate strategy
* Resource requests and limits
* Readiness probe
* Liveness probe
* ConfigMap
* Secret
* Kubernetes Service

---

### 🔹 AWS Infrastructure

The application is deployed on an AWS EC2 Ubuntu server.

Terraform is used to manage infrastructure configuration including the EC2 environment and networking/security configuration.

---

### 🔹 CI/CD Automation

GitHub Actions automatically executes the deployment workflow after a push to the `main` branch.

This removes the need to manually:

* Build the Docker image
* Copy the image to the server
* Update Kubernetes
* Check deployment status

---

## 🌐 Application Endpoints

### Home

```text
http://<EC2-IP>:30080/
```

### Health Check

```text
http://<EC2-IP>:30080/health
```

Example response:

```json
{
  "service": "CloudDeploy",
  "status": "healthy",
  "version": "1.0.0"
}
```

### Application Status

```text
http://<EC2-IP>:30080/api/status
```

Example:

```json
{
  "application": "CloudDeploy",
  "version": "1.0.0",
  "environment": "kubernetes",
  "status": "operational"
}
```

### Version

```text
http://<EC2-IP>:30080/api/version
```

---

## 📁 Project Structure

```text
CloudDeploy/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── tests/
│   └── test_app.py
│
├── k8s/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── ...
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🐳 Docker

Build the application image:

```bash
docker build -t clouddeploy:1.0.0 .
```

Run the container:

```bash
docker run -p 5000:5000 clouddeploy:1.0.0
```

Open:

```text
http://localhost:5000
```

---

## ☸️ Kubernetes

Create the namespace:

```bash
kubectl apply -f k8s/namespace.yaml
```

Apply configuration:

```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
```

Deploy the application:

```bash
kubectl apply -f k8s/deployment.yaml
```

Create the service:

```bash
kubectl apply -f k8s/service.yaml
```

Check pods:

```bash
kubectl get pods -n clouddeploy
```

Check deployment:

```bash
kubectl get deployment -n clouddeploy
```

Check service:

```bash
kubectl get service -n clouddeploy
```

---

## 🏗️ Terraform

Terraform is used to provision the AWS infrastructure required by the project.

Initialize Terraform:

```bash
terraform init
```

Check the infrastructure plan:

```bash
terraform plan
```

Apply the infrastructure:

```bash
terraform apply
```

Destroy the infrastructure when it is no longer required:

```bash
terraform destroy
```

> ⚠️ Review AWS resources and costs before applying or destroying infrastructure.

---

## 🔐 Security

The project follows several basic security practices:

* Docker container runs as a non-root user
* Sensitive files are excluded using `.gitignore`
* SSH private keys are stored in GitHub Actions Secrets
* Kubernetes secrets are not committed as real production credentials
* GitHub Actions handles deployment credentials through encrypted secrets

> The Kubernetes secret included in this portfolio project is a demonstration secret and should not be used for production credentials.

---

## 📸 Project Screenshots

### 1. CloudDeploy Application

*Add screenshot here.*

```text
docs/screenshots/clouddeploy-home.png
```

### 2. GitHub Actions Pipeline

*Add successful CI/CD workflow screenshot here.*

```text
docs/screenshots/github-actions.png
```

### 3. AWS EC2

*Add EC2 instance screenshot here.*

```text
docs/screenshots/aws-ec2.png
```

### 4. Kubernetes Pods

*Add Kubernetes pods screenshot here.*

```text
docs/screenshots/kubernetes-pods.png
```

### 5. Kubernetes Service

*Add Kubernetes service screenshot here.*

```text
docs/screenshots/kubernetes-service.png
```

### 6. Terraform

*Add Terraform infrastructure screenshot here.*

```text
docs/screenshots/terraform.png
```

---

## 📊 Kubernetes Deployment Verification

Example:

```bash
sudo k3s kubectl get pods -n clouddeploy
```

Expected result:

```text
NAME                           READY   STATUS    RESTARTS
clouddeploy-xxxxxxxxxx-xxxxx   1/1     Running   0
clouddeploy-xxxxxxxxxx-xxxxx   1/1     Running   0
```

Deployment:

```bash
sudo k3s kubectl get deployment -n clouddeploy
```

Expected:

```text
NAME          READY   UP-TO-DATE   AVAILABLE
clouddeploy   2/2     2            2
```

Health check:

```bash
curl http://localhost:30080/health
```

Expected:

```json
{
  "service": "CloudDeploy",
  "status": "healthy",
  "version": "1.0.0"
}
```

---

## 🎯 What This Project Demonstrates

This project demonstrates practical experience with:

* Linux server administration
* AWS EC2
* Infrastructure as Code
* Terraform
* Docker
* Containerization
* Kubernetes
* K3s
* Kubernetes Deployments
* Kubernetes Services
* ConfigMaps
* Secrets
* Health checks
* Rolling deployments
* Git
* GitHub
* GitHub Actions
* CI/CD pipelines
* Automated testing
* Cloud deployment
* Basic DevOps security practices

---

## 🚀 Future Improvements

Possible future improvements include:

* Push Docker images to Amazon ECR
* Use an AWS Application Load Balancer
* Add HTTPS with SSL/TLS
* Add Prometheus and Grafana monitoring
* Add centralized logging
* Add Helm charts
* Add Kubernetes Horizontal Pod Autoscaling
* Add Argo CD for GitOps
* Add automated rollback
* Use AWS IAM roles instead of long-lived SSH credentials
* Move from a single EC2/K3s node to a production-grade Kubernetes cluster

---

## 💡 Why I Built This

I built CloudDeploy to move beyond theoretical DevOps learning and understand how a real application can move from source code to a cloud environment through an automated deployment pipeline.

The project helped me gain hands-on experience with:

**Git → CI/CD → Docker → AWS → Kubernetes → Automated Deployment**

---

## 👨‍💻 Author

**Pravesh Kumar**

Aspiring DevOps / Cloud Engineer

GitHub:
https://github.com/Pravesh880082

---

## ⭐ Project Highlights

```text
✓ Automated testing
✓ Dockerized Flask application
✓ AWS EC2 deployment
✓ Terraform infrastructure
✓ K3s Kubernetes cluster
✓ 2 Kubernetes replicas
✓ Health monitoring endpoints
✓ GitHub Actions CI/CD
✓ Automated Kubernetes deployment
✓ Rolling updates
```

---

## 📜 License

This project is created for educational, portfolio, and learning purposes.
