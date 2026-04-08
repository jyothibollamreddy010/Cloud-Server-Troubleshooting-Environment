# 🚀 Cloud Server Environment

This project implements a cloud-based environment using FastAPI, designed to simulate and interact with an environment through API calls.

It was built as part of a deployment-focused workflow, integrating backend logic, API design, and containerized deployment.

---

## ⚙️ What this project does

The system allows users to:
•⁠  ⁠Reset the environment
•⁠  ⁠Perform actions (step execution)
•⁠  ⁠Retrieve the current state

All interactions are handled through REST APIs.

---

## 🔌 API Endpoints

•⁠  ⁠POST /reset → Resets the environment  
•⁠  ⁠POST /step → Performs an action and returns state, reward, done  
•⁠  ⁠GET /state → Returns current environment state  

---

## 🏗️ Architecture

•⁠  ⁠app.py → Core FastAPI application  
•⁠  ⁠environment.py → Environment logic  
•⁠  ⁠inference.py → Execution handling  
•⁠  ⁠server/app.py → Deployment entry point  
•⁠  ⁠Dockerfile → Container setup  

---

## 🚀 Deployment

•⁠  ⁠Deployed using Docker  
•⁠  ⁠Hosted on Hugging Face Spaces  
•⁠  ⁠Supports multi-mode deployment validation  

---

## 💡 Key Highlights

•⁠  ⁠Built complete API system using FastAPI  
•⁠  ⁠Structured project for scalable deployment  
•⁠  ⁠Implemented Docker-based environment  
•⁠  ⁠Solved real deployment issues (entrypoints, validation, config)

---

## ▶️ Run Locally

uvicorn app:app --reload

---

## 🌐 Live Deployment

Available via Hugging Face Space
