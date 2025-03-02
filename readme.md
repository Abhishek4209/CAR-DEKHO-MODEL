# Car Dekho Price Prediction Model

![alt text](static/img/car.png)
This project involves the development of a machine learning model to predict the selling prices of cars using various input features. The model is built using Python and leverages several key machine learning techniques to deliver accurate predictions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Car Dekho Price Prediction Model is designed to assist users in estimating the market value of a used car. By inputting relevant details about the car, the model predicts a fair selling price. The primary goal is to provide an efficient tool for both car sellers and buyers to understand the market better.

## Features

- **Multi-feature Input**: Accepts various car features like age, mileage, fuel type, transmission, etc.
- **Accurate Predictions**: Uses advanced machine learning algorithms for high prediction accuracy.
- **User-Friendly Interface**: Simple web form for easy interaction.
- **Scalable**: Can be extended to include more features or updated data.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Abhishek4209/car-dekho-price-prediction.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd car-dekho-price-prediction
    ```

3. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the model, you can run the Flask application and interact with the web form:

1. **Start the Flask server:**

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

3. **Input the car features** into the form and click on "Predict" to get the estimated selling price.

## Model Details

- **Algorithms Used**: The model uses a combination of linear regression, decision trees, and random forest algorithms to predict car prices.
- **Feature Engineering**: Several car features like age, mileage, fuel type, transmission type, and more were used in the model.
- **Data Preprocessing**: Data cleaning, normalization, and feature selection were performed to enhance the model's performance.

## Results

The model has been tested on various datasets and has shown a high level of accuracy in predicting car prices. Below are some metrics:


- **R-squared Score**:  92.152

## Contributing

If you would like to contribute to this project, please follow these steps:

1. **Fork the repository** on GitHub.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -m 'Add new feature'`).
4. **Push to the branch** (`git push origin feature-branch`).
5. **Submit a pull request**.

