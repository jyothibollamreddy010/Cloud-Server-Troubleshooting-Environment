# Cloud Server RL Environment

## Description

This project simulates a cloud server recovery environment where an agent learns to bring a failed server back to a running state.

## Environment

* Initial state: "Server Down"
* Actions:

  * "check_logs" → finds issue
  * "restart" → fixes server
* Goal: Reach "Server Running"

## API Endpoints

* POST /reset → Reset environment
* POST /step → Take action
* GET /state → Get current state

## Setup

* Built using FastAPI
* Deployed using Docker on Hugging Face Spaces

## Files

* app.py → API implementation
* environment.py → RL environment
* inference.py → baseline script
* Dockerfile → container setup

## Output

Returns state, reward, and done flag based on actions.
