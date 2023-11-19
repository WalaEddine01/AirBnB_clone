#!/bin/bash

# Generate commit message with current timestamp
commit_msg="I made the changes on $(date +'%Y-%m-%d %H:%M:%S')"

# Add all changes to the staging area
git add .

# Commit changes with the generated message
git commit -m "$commit_msg"

# Push changes to the remote repository
git push
