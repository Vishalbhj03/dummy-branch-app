# Branch Loan API – DevOps Assignment

This repository contains a Flask-based Loan API and the DevOps work I did to make it **production-ready**:

- Docker containerization (API + Postgres + Nginx with HTTPS)
- Multi-environment setup (dev / staging / prod) using Docker Compose
- CI/CD pipeline with GitHub Actions (tests → build → security scan → push)
- Basic observability: health checks, structured logs, and metrics (Prometheus + Grafana)

---

## 1. How to run the application locally

## 1.1 Prerequisites

Install on your machine:

- Docker
- Docker Compose
- Git
- OpenSSL (usually already available on Linux/macOS)

## 1.2 Clone the repository

```bash
git clone https://github.com/Vishalbhj03/dummy-branch-app.git
cd dummy-branch-app
