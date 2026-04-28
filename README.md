# AI-Enhanced DevSecOps Pipeline on AWS EKS

This project demonstrates a prototype AI-enhanced DevSecOps pipeline using:

- Jenkins for CI/CD
- Terraform and Helm for Infrastructure as Code
- Checkov and tfsec for IaC security scanning
- Trivy for container vulnerability scanning
- XGBoost for ML-based risk classification
- AWS EKS for Kubernetes deployment

## Planned Pipeline

Code Commit -> Jenkins Pipeline -> IaC Scan -> Container Scan -> ML Risk Scoring -> Deployment to EKS -> Runtime Monitoring
