# Security Scripts and Procedures

This repository hosts a collection of Ansible playbooks, shell scripts, and documentation designed to automate security measures and system updates for Ubuntu servers.

## Repository Contents

### `update_system_packages.yaml`
Automates system package updates. It updates and upgrades APT and snap packages, including pip.

### `configure_ufw.yaml`
Configures Uncomplicated Firewall (UFW) rules. It starts by clearing all existing rules.

### `perform_os_security_scan.yaml`
Starts the `nessusd` service, runs `clamscan`, and performs a `lynis audit`. The scan is executed as a non-root user.

### `security_procedures.org`
An Org file outlining manual procedures for security updates and maintenance. Serves as a quick reference.

### `create_sonarqube_projects.sh`
A script to automate the creation of SonarQube projects, eliminating manual setup.

### `update_venv_pip_packages.yaml`
Upgrades all pip packages within a specified virtual environment.

### `security-scans-results`
This folder contains the files with the security scan results every time a scan is run.

### `perform_sonarqube_scan.yaml`
Configures and executes scans with SonarQube for code quality and security vulnerabilities.

### `secret_detection.org`
An Org file detailing our secret detection setup and procedures.

### Additional Files
- `.pre-commit-config.yaml` and `.secrets.baseline`: These files are integral to our pre-commit hooks and secret detection mechanisms, ensuring code quality and security.
