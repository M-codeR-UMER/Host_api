# Credit-Risk-Classifier API

A RESTful API built with **FastAPI** for predicting bank credit risk using a pre-trained machine learning model. This project demonstrates how to deploy a machine learning model as an API to serve predictions based on user inputs.

---

## Project Overview

This API takes structured bank customer data as input and returns a prediction indicating whether the applicant is a "Good" or "Bad" credit risk. It leverages a pre-trained decision tree model (`tree_Accuracy_based.pkl`) loaded using `pickle`.

The API is developed using **FastAPI**, which is modern, fast, and asynchronous—ideal for production-ready ML model deployment.

---

## Features

- It validates input data using Pydantic models (`bank.py`).  
- It uses a serialized machine learning model (`pickle` file).
- Simple JSON interface for sending data and receiving predictions.

---

## How It Works

-The API receives JSON input representing customer financial and demographic details.
-Pydantic validates and parses the input data automatically.
-The FastAPI endpoint extracts feature values and passes them to the pre-loaded ML model.
-The model predicts credit risk (1 for good, 0 for bad).
-The API returns a JSON response with a human-readable prediction.

---

## Tech Stack

1.Python 3.8+
2.FastAPI – High-performance web framework for building APIs
3.Uvicorn – ASGI server for running FastAPI apps
4.scikit-learn – Machine learning model serialization and inference
5.Pydantic – Data validation and settings management using Python type annotations
6.Pandas & NumPy – Data manipulation and numerical operations

---
