import pickle
from flask import Flask, render_template, request
import numpy as np
from Helpers.helpers import *

"""
 <label for="radio-6" class="radio-label">
"""

app = Flask(__name__,  template_folder='Templates')


model = pickle.load(open("app_df xgbmodel.pkl", 'rb'))

@app.route('/', methods = ['GET'])
def home():
    return render_template('apply.html')

@app.route('/predict', methods=['GET'])
def predict():
    all_data = request.args

    CNT_CHILDREN = int(all_data['CNT_CHILDREN'])
    AGE = int(all_data['AGE'])
    AMT_ANNUITY = int(all_data['AMT_ANNUITY'])
    AMT_CREDIT = int(all_data['AMT_CREDIT'])
    AMT_INCOME_TOTAL = int(all_data['AMT_INCOME_TOTAL'])
    AMT_GOODS_PRICE = int(all_data['AMT_GOODS_PRICE'])
    AMT_REQ_CREDIT_BUREAU_YEAR = int(all_data['AMT_REQ_CREDIT_BUREAU_YEAR'])
    CNT_FAM_MEMBERS = int(all_data['CNT_FAM_MEMBERS'])
    MONTHS_ID_PUBLISH = int(all_data['MONTHS_ID_PUBLISH'])
    NAME_EDUCATION_TYPE = int(all_data['NAME_EDUCATION_TYPE'])
    NAME_FAMILY_STATUS = int(all_data['NAME_FAMILY_STATUS'])
    NAME_HOUSING_TYPE = int(all_data['NAME_HOUSING_TYPE'])
    NAME_INCOME_TYPE = int(all_data['NAME_INCOME_TYPE'])
    NAME_TYPE_SUITE = int(all_data['NAME_TYPE_SUITE'])
    OCCUPATION_TYPE = int(all_data['OCCUPATION_TYPE'])
    REGION_RATING_CLIENT = int(all_data['REGION_RATING_CLIENT'])
    YRS_EMPLOYED = int(all_data['YRS_EMPLOYED'])

    features = [CNT_CHILDREN, AMT_INCOME_TOTAL, AMT_CREDIT, AMT_ANNUITY, AMT_GOODS_PRICE,NAME_TYPE_SUITE, NAME_INCOME_TYPE,
          NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, AGE, MONTHS_ID_PUBLISH, OCCUPATION_TYPE, CNT_FAM_MEMBERS,
          REGION_RATING_CLIENT, AMT_REQ_CREDIT_BUREAU_YEAR, YRS_EMPLOYED]

    contract_type = NAME_CONTRACT_TYPE[all_data['NAME_CONTRACT_TYPE']]
    gender = CODE_GENDER[all_data['Gender']]
    own_car = FLAG_OWN_CAR[all_data['FLAG_OWN_CAR']]
    own_realty = FLAG_OWN_REALTY[all_data['FLAG_OWN_REALTY']]
    
    features +=contract_type+gender+own_car+own_realty

    predict= model.predict(np.array([features]))
    
    #predictions = model.predict(features)
    #output = round(predictions[0],2)
    '''if output == 0:
        
        return render_template("apply.html", prediction_text= f"The client is {output}, Regular Payer")
    else:
        return render_template('apply.html', prediction_text= f"The client is {output}, Defaulter")'''
    if predict == 0:
        return render_template('prediction.html', prediction = predict, prediction_text = 'Client is Regular payer')
        #return f'Client is Regular payer{str(predict)}'
    else:
        return render_template('prediction.html', prediction = predict, prediction_text = 'Client is Defaulter')
        # return f'Client is Defaulter{str(predict)}'
        

if __name__ == '__main__':
    
    app.run(debug= True)













