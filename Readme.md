# CarDekho Model

This repository contains a dataset and model for predicting the selling price of used cars based on various features. The dataset includes information about different cars and their attributes such as brand, model, age, kilometers driven, and more.

## Table of Contents

- [Dataset](#dataset)
- [Features](#features)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The dataset contains the following features:

| Feature             | Description                                        |
|---------------------|----------------------------------------------------|
| `car_name`          | Name of the car                                    |
| `brand`             | Brand of the car                                   |
| `model`             | Model of the car                                   |
| `vehicle_age`       | Age of the vehicle in years                        |
| `km_driven`         | Kilometers driven by the vehicle                   |
| `seller_type`       | Type of seller (e.g., Individual, Dealer)          |
| `fuel_type`         | Type of fuel used by the car (e.g., Petrol, Diesel)|
| `transmission_type` | Transmission type of the car (e.g., Manual, Automatic)|
| `mileage`           | Mileage of the car in kmpl                         |
| `engine`            | Engine capacity of the car in CC                   |
| `max_power`         | Maximum power of the car in BHP                    |
| `seats`             | Number of seats in the car                         |
| `selling_price`     | Selling price of the car                           |

## Features

The main features used for predicting the selling price are:

- Car Name
- Brand
- Model
- Vehicle Age
- Kilometers Driven
- Seller Type
- Fuel Type
- Transmission Type
- Mileage
- Engine
- Max Power
- Seats

## Model

The model used for predicting the selling price is a machine learning model trained on the above features. The model aims to provide accurate predictions based on the car's attributes.

## Installation

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Usage
To use the model for predicting the selling price, follow these steps:

- Load the dataset.
- Preprocess the data.
- Train the model using the training data.
- Use the trained model to make predictions on new data.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. 