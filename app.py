from flask import Flask,render_template,request
import joblib
from pymongo import MongoClient

model_file_path = "./models/randomforest.lb"
#model_file_path =  r'C:\Users\Ranjit\Desktop\15 July\customer_satifaction\models\logisticregre.lb'
model =  joblib.load(model_file_path)

connection_string="mongodb+srv://abhipsasri8183:fccv5v9jXuJIs4W6@cluster1.b94xm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client=MongoClient(connection_string)
database=client['Customer'] #-->database
collection=database["CustomerData"] #table create or collection

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/output')
def output():
    return render_template('output.html')


@app.route('/userdata')#http://127.0.0.1:5000/userdata
def userdata():
    return render_template('project.html')

@app.route('/predict',methods=['GET','POST'])
def  predict(): 
    if request.method == 'POST':
        age = int(request.form['age'])
        flight_distance  = int(request.form['flight_distance'])
        inflight_entertainment  = int(request.form['inflight_entertainment'])
        baggage_handling  = int(request.form['baggage_handling'])
        cleanliness  = int(request.form['cleanliness'])
        departure_delay  = int(request.form['departure_delay'])
        arrival_delay  = int(request.form['arrival_delay'])
        gender  = int(request.form['gender'])
        customer_type  = int(request.form['customer_type'])
        travel_type  = int(request.form['travel_type'])
        class_type  = request.form['class_type']

        economy = 0 
        economy_plus = 0
        if class_type == "ECO": 
            economy = 1
        elif class_type == "ECO_PLUS": 
            economy_plus = 1 


        UNSEEN_DATA = [[age,flight_distance,inflight_entertainment,baggage_handling,cleanliness,
                        departure_delay,arrival_delay,gender,customer_type,travel_type,economy,economy_plus]]
        PREDICTION = model.predict(UNSEEN_DATA)[0]
        # print(PREDICTION)

        # X_train variables  
        # Age	Flight Distance	Inflight entertainment	Baggage handling	Cleanliness	Departure Delay in Minutes
        # 	Arrival Delay in Minutes	Gender_Male	Customer Type_disloyal Customer	Type of Travel_Personal Travel	
        # Class_Eco	Class_Eco Plus
        label_dict = {0:'Disatisfied',1:'Satisfied'}
        # return label_dict[PREDICTION]
        data={'age':age,'flight_distance':flight_distance,'inflight_entertainment':inflight_entertainment,'baggage_handling':baggage_handling,'cleanliness':cleanliness,
              'departure_delay':departure_delay,'arrival_delay':arrival_delay,'gender':gender,'customer_type':customer_type,'travel_type':travel_type,'class_type':class_type}
        data_id=collection.insert_one(data).inserted_id
        print("your data is inserted into the database:",data_id)
        return render_template('output.html',output=label_dict[PREDICTION])

if __name__=="__main__":
    app.run(debug=True)