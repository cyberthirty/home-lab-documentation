#!/bin/bash

# Decode passwords
password1=$(echo 'Qm9iIC0gIVBAJCRXMHJEITEyMw==' | base64 --decode)
password2=$(echo 'QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk' | base64 --decode)

# ANSI color codes
GREEN='\033[0;32m'
DC='\033[0m' # Default Color or reset to default

# Output passwords with color
echo -e "${GREEN}Password 1 is ${GREEN}$password1"
echo -e "${GREEN}Password 2 is ${GREEN}$password2"
echo -e "${DC}" # Reset to default color
