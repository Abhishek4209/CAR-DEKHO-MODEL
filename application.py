# from flask import Flask, render_template, jsonify,request
# # from src.logger import logging
# # from src.pipelines.prediction_pipeline import CustomData,PredictionPipeline
# app = Flask(__name__)

# brands_models = {
#     'Maruti': ['Alto', 'Wagon R', 'Swift', 'Ciaz', 'Baleno', 'Swift Dzire', 'Ignis', 'Vitara', 'Celerio', 'Ertiga', 'Eeco', 'Dzire VXI', 'XL6', 'S-Presso', 'Dzire LXI', 'Dzire ZXI'],
#     'Hyundai': ['Grand', 'i20', 'i10', 'Venue', 'Verna', 'Creta', 'Santro', 'Elantra', 'Aura', 'Tucson'],
#     'Maruti' : ['Alto' 'Wagon R' 'Swift' 'Ciaz' 'Baleno' 'Swift Dzire' 'Ignis' 'Vitara'
#     'Celerio' 'Ertiga' 'Eeco' 'Dzire VXI' 'XL6' 'S-Presso' 'Dzire LXI'
#     'Dzire ZXI'] ,
#     'Hyundai' : ['Grand' 'i20' 'i10' 'Venue' 'Verna' 'Creta' 'Santro' 'Elantra' 'Aura'
#     'Tucson'] ,
#     'Ford' : ['Ecosport' 'Aspire' 'Figo' 'Endeavour' 'Freestyle'] ,
#     'Renault' : ['Duster' 'KWID' 'Triber'] ,
#     'Mini' : ['Cooper'] ,
#     'Mercedes-Benz' : ['C-Class' 'E-Class' 'GL-Class' 'S-Class' 'CLS' 'GLS'] ,
#     'Toyota' : ['Innova' 'Fortuner' 'Camry' 'Yaris' 'Glanza'] ,
#     'Volkswagen' : ['Vento' 'Polo'] ,
#     'Honda' : ['City' 'Amaze' 'CR-V' 'Jazz' 'Civic' 'WR-V' 'CR'] ,
#     'Mahindra' : ['Bolero' 'XUV500' 'KUV100' 'Scorpio' 'Marazzo' 'KUV' 'Thar' 'XUV300'
#     'Alturas'] ,
#     'Datsun' : ['RediGO' 'GO' 'redi-GO'] ,
#     'Tata' : ['Tiago' 'Tigor' 'Safari' 'Hexa' 'Nexon' 'Harrier' 'Altroz'] ,
#     'Kia' : ['Seltos' 'Carnival'] ,
#     'BMW' : ['5' '3' 'Z4' '6' 'X5' 'X1' '7' 'X3' 'X4'] ,
#     'Audi' : ['A4' 'A6' 'Q7' 'A8'] ,
#     'Land Rover' : ['Rover'] ,
#     'Jaguar' : ['XF' 'F-PACE' 'XE'] ,
#     'MG' : ['Hector'] ,
#     'Isuzu' : ['D-Max' 'MUX'] ,
#     'Porsche' : ['Cayenne' 'Macan' 'Panamera'] ,
#     'Skoda' : ['Rapid' 'Superb' 'Octavia'] ,
#     'Volvo' : ['S90' 'XC' 'XC90' 'XC60'] ,
#     'Lexus' : ['ES' 'NX' 'RX'] ,
#     'Jeep' : ['Wrangler' 'Compass'] ,
#     'Maserati' : ['Ghibli' 'Quattroporte'] ,
#     'Bentley' : ['Continental'] ,
#     'Nissan' : ['Kicks' 'X-Trail'] ,
#     'ISUZU' : ['MUX'] ,
#     'Ferrari' : ['GTC4Lusso'] ,
#     'Mercedes-AMG' : ['C'] ,
#     'Rolls-Royce' : ['Ghost'] ,
#     'Force' : ['Gurkha'] ,

    
# }

# car_details = {
#     'Maruti Alto' : ( ['Petrol' 'CNG'] , [5, 4] ),
#     'Hyundai Grand' : ( ['Petrol' 'Diesel' 'CNG'] , [5] ),
#     'Hyundai i20' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Ford Ecosport' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Maruti Wagon R' : ( ['Petrol' 'CNG' 'LPG'] , [5] ),
#     'Hyundai i10' : ( ['Petrol' 'LPG'] , [5] ),
#     'Hyundai Venue' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Maruti Swift' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Hyundai Verna' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Renault Duster' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Mini Cooper' : ( ['Petrol' 'Diesel'] , [5 ,4] ),
#     'Maruti Ciaz' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Mercedes-Benz C-Class' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Toyota Innova' : ( ['Diesel' 'Petrol' 'CNG'] , [8, 7] ),
#     'Maruti Baleno' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Maruti Swift Dzire' : ( ['Petrol' 'Diesel' 'CNG'] , [5] ),
#     'Volkswagen Vento' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Hyundai Creta' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Honda City' : ( ['Petrol' 'Diesel' 'CNG'] , [5 ,0] ),
#     'Mahindra Bolero' : ( ['Diesel'] , [7, 9, 8] ),
#     'Toyota Fortuner' : ( ['Diesel' 'Petrol'] , [7] ),
#     'Renault KWID' : ( ['Petrol'] , [5] ),
#     'Honda Amaze' : ( ['Petrol' 'Diesel' 'CNG'] , [5] ),
#     'Hyundai Santro' : ( ['Petrol' 'CNG' 'LPG'] , [5] ),
#     'Mahindra XUV500' : ( ['Diesel'] , [7] ),
#     'Mahindra KUV100' : ( ['Petrol' 'Diesel'] , [5 ,6] ),
#     'Maruti Ignis' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Datsun RediGO' : ( ['Petrol'] , [5] ),
#     'Mahindra Scorpio' : ( ['Diesel'] , [7, 8 ,5, 9] ),
#     'Mahindra Marazzo' : ( ['Diesel'] , [7, 8] ),
#     'Ford Aspire' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Ford Figo' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Maruti Vitara' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Tata Tiago' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Volkswagen Polo' : ( ['Petrol' 'Diesel'] , [5, 4] ),
#     'Kia Seltos' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Maruti Celerio' : ( ['Petrol' 'CNG' 'Diesel'] , [5] ),
#     'Datsun GO' : ( ['Petrol'] , [7 ,5] ),
#     'BMW 5' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Honda CR-V' : ( ['Petrol' 'Diesel'] , [5 ,7] ),
#     'Ford Endeavour' : ( ['Diesel'] , [7] ),
#     'Mahindra KUV' : ( ['Diesel' 'Petrol' 'CNG'] , [5, 6] ),
#     'Honda Jazz' : ( ['Petrol' 'Diesel'] , [5] ),
#     'BMW 3' : ( ['Diesel' 'Petrol'] , [5 ,4] ),
#     'Audi A4' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Tata Tigor' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Maruti Ertiga' : ( ['Diesel' 'Petrol' 'CNG'] , [7] ),
#     'Tata Safari' : ( ['Diesel' 'Petrol'] , [7, 5] ),
#     'Mahindra Thar' : ( ['Diesel'] , [6 ,7] ),
#     'Tata Hexa' : ( ['Diesel'] , [7] ),
#     'Land Rover Rover' : ( ['Petrol' 'Diesel'] , [5 ,4, 7, 6] ),
#     'Maruti Eeco' : ( ['Petrol' 'CNG'] , [5 ,7] ),
#     'Audi A6' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Mercedes-Benz E-Class' : ( ['Petrol' 'Diesel'] , [5, 2] ),
#     'Audi Q7' : ( ['Diesel'] , [7] ),
#     'BMW Z4' : ( ['Petrol'] , [2] ),
#     'BMW 6' : ( ['Petrol' 'Diesel'] , [4] ),
#     'Jaguar XF' : ( ['Diesel' 'Petrol'] , [5] ),
#     'BMW X5' : ( ['Diesel'] , [5, 7] ),
#     'MG Hector' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Honda Civic' : ( ['Petrol'] , [5] ),
#     'Isuzu D-Max' : ( ['Diesel'] , [5] ),
#     'Porsche Cayenne' : ( ['Diesel' 'Petrol'] , [5] ),
#     'BMW X1' : ( ['Diesel'] , [5] ),
#     'Skoda Rapid' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Ford Freestyle' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Skoda Superb' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Tata Nexon' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Mahindra XUV300' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Maruti Dzire VXI' : ( ['Petrol'] , [5] ),
#     'Volvo S90' : ( ['Diesel'] , [5] ),
#     'Honda WR-V' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Maruti XL6' : ( ['Petrol'] , [6] ),
#     'Renault Triber' : ( ['Petrol'] , [7] ),
#     'Lexus ES' : ( ['Petrol'] , [5] ),
#     'Jeep Wrangler' : ( ['Petrol'] , [5] ),
#     'Toyota Camry' : ( ['Petrol' 'Electric'] , [5] ),
#     'Hyundai Elantra' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Toyota Yaris' : ( ['Petrol'] , [5] ),
#     'Mercedes-Benz GL-Class' : ( ['Diesel' 'Petrol'] , [7 ,5] ),
#     'BMW 7' : ( ['Diesel' 'Petrol'] , [4,5] ),
#     'Maruti S-Presso' : ( ['Petrol'] , [5] ),
#     'Maruti Dzire LXI' : ( ['Petrol'] , [5] ),
#     'Hyundai Aura' : ( ['Petrol'] , [5] ),
#     'Volvo XC' : ( ['Diesel'] , [7] ),
#     'Maserati Ghibli' : ( ['Diesel'] , [5] ),
#     'Bentley Continental' : ( ['Petrol'] , [4, 5] ),
#     'Honda CR' : ( ['Petrol'] , [5] ),
#     'Nissan Kicks' : ( ['Petrol' 'Diesel'] , [5, 0] ),
#     'Mercedes-Benz S-Class' : ( ['Diesel' 'Petrol'] , [5 ,4] ),
#     'Hyundai Tucson' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Tata Harrier' : ( ['Diesel'] , [5] ),
#     'BMW X3' : ( ['Diesel'] , [5] ),
#     'Skoda Octavia' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Jeep Compass' : ( ['Petrol' 'Diesel'] , [5] ),
#     'Mercedes-Benz CLS' : ( ['Diesel' 'Petrol'] , [4 ,5] ),
#     'Datsun redi-GO' : ( ['Petrol'] , [5] ),
#     'Toyota Glanza' : ( ['Petrol'] , [5] ),
#     'Porsche Macan' : ( ['Petrol'] , [5] ),
#     'BMW X4' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Maruti Dzire ZXI' : ( ['Petrol'] , [5] ),
#     'Volvo XC90' : ( ['Diesel'] , [7] ),
#     'Jaguar F-PACE' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Audi A8' : ( ['Diesel' 'Petrol'] , [5, 4] ),
#     'ISUZU MUX' : ( ['Diesel'] , [7] ),
#     'Ferrari GTC4Lusso' : ( ['Petrol'] , [4] ),
#     'Mercedes-Benz GLS' : ( ['Diesel' 'Petrol'] , [7] ),
#     'Nissan X-Trail' : ( ['Diesel'] , [5] ),
#     'Jaguar XE' : ( ['Diesel' 'Petrol'] , [5] ),
#     'Volvo XC60' : ( ['Diesel'] , [5] ),
#     'Porsche Panamera' : ( ['Petrol' 'Diesel'] , [4] ),
#     'Mahindra Alturas' : ( ['Diesel'] , [7] ),
#     'Tata Altroz' : ( ['Petrol'] , [5] ),
#     'Lexus NX' : ( ['Petrol'] , [5] ),
#     'Kia Carnival' : ( ['Diesel'] , [9, 7] ),
#     'Mercedes-AMG C' : ( ['Petrol'] , [5] ),
#     'Lexus RX' : ( ['Petrol'] , [5] ),
#     'Rolls-Royce Ghost' : ( ['Petrol'] , [4] ),
#     'Maserati Quattroporte' : ( ['Diesel'] , [5] ),
#     'Isuzu MUX' : ( ['Diesel'] , [7] ),
#     'Force Gurkha' : ( ['Diesel'] , [5] )

# }

# @app.route('/')
# def index():
#     brands = list(brands_models.keys())
#     return render_template('index.html', brands=brands)

# @app.route('/models/<brand>')
# def get_models(brand):
#     models = brands_models.get(brand)
#     return jsonify(models)

# @app.route('/car_details/<brand>/<model>')
# def get_car_details(brand, model):
#     car_name = f"{brand} {model}"
#     details = car_details.get(car_name, ([], []))
#     fuel_types, seats = details
#     return jsonify({'fuel_types': fuel_types, 'seats': seats})

# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0')    

from flask import Flask,render_template,request
# from src.logger import logging
# from src.pipelines.prediction_pipeline import CustomData,PredictionPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def prediction():
    if request.method == 'GET':
        return render_template('index.html')


#     else: 
#         data=CustomData(
#         car_name=(request.form.get('car_name')),
#         brand=(request.form.get('brand')),
#         model=(request.form.get('model')),
#         vehicle_age=int(request.form.get('vehicle_age')),
#         km_driven=int(request.form.get('km_driven')),
#         seller_type=(request.form.get('seller_type')),
#         fuel_type=(request.form.get('fuel_type')),
#         transmission_type=(request.form.get('transmission_type')),
#         mileage=float(request.form.get('mileage')),
#         engine=int(request.form.get('engine')),
#         max_power=float(request.form.get('max_power')),
#         seats=int(request.form.get('seats'))
#         )
#         logging.info(data)
#         final_new_data=data.get_data_as_dataframe()
#         logging.info(final_new_data)
#         predict_pipeline=PredictionPipeline()
#         pred=predict_pipeline.predict(final_new_data)
#         result=round(pred[0])
#         return render_template('result.html',prediction=result)



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)