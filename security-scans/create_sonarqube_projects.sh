#!/usr/bin/env bash

# SonarQube server details and credentials
SONAR_URL="http://localhost:9000"
ADMIN_USER="admin"

# Array of repository names
REPO_NAMES=(
    "anki-flashcards" "aws-python-scripts" "aws-security-checks" "aws-terraform-personal" "cloud-custodian"
    "configs" "docker-containers" "docker-website"
    "quizlet" "reviews-website" "security-routines"
    "transcription" "williseed-bot" "wireguard-server" "wordlesolver"
)

for NAME in "${REPO_NAMES[@]}"; do
  PROJECT_KEY=$(echo "$NAME" | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')
  curl -X POST -u "$ADMIN_USER":"$ADMIN_PASSWORD" "$SONAR_URL/api/projects/create?name=$NAME&project=$PROJECT_KEY"
  echo "Created project: $NAME"
done

