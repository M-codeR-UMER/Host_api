# 🚀 Credit Risk Classifier API

A production-ready **FastAPI** application that predicts whether a loan applicant is a **Good** or **Bad** credit risk based on structured financial and demographic data. This project demonstrates how to deploy a trained ML model behind a RESTful API interface.

---

## 🧠 Project Overview

The API takes in customer input via JSON and returns a prediction based on a **Decision Tree Classifier** trained on credit data. The model is serialized using `pickle` (`tree_Accuracy_based.pkl`) and loaded into the app during runtime.

Built with **FastAPI** — a blazing-fast, modern Python web framework — this API is ideal for deploying ML models in real-world applications.

---

## ✅ Features

- ✅ **Input validation** using `Pydantic` models (`bank.py`)
- ✅ **Model loaded dynamically** via Python’s `pickle`
- ✅ **Clean JSON endpoints** for easy integration
- ✅ **Automatic Swagger Docs** at `/docs`
- ✅ **Human-readable prediction response**

---

## 🔁 How It Works

1. 📥 The user sends a POST request with financial data in JSON format.
2. 🧰 FastAPI + Pydantic validates and parses the input.
3. 🤖 The decision tree model makes a prediction (`1` = Good, `0` = Bad).
4. 📤 The API returns a friendly response like:  
   ```json
   {"Prediction": "Good"}
