import pickle 

with open('/home/parvez/crop_prediction/crop_recommendation/model.sav', 'rb') as f:
    model = pickle.load(f)

with open('/home/parvez/crop_prediction/crop_recommendation/crop_list.pkl', 'rb') as f:
    crop_list = pickle.load(f)

with open('/home/parvez/crop_prediction/crop_recommendation/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def get_prediction(prd_list):
    prd_list = scaler.transform(prd_list)
    print(prd_list)
    prediction = model.predict(prd_list)
    return crop_list[prediction.item()].capitalize()