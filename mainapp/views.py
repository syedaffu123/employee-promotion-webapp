from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'projectapp/index.html')
def predict(request):
    return render(request,'projectapp/predict.html')
def predictions(request):
    return render(request,'projectapp/predictions.html')

def about(request):
    return render(request,'projectapp/info.html')


def getPredictions(a,b,c,d,e,f,g,h,i,j,k,l,m):
    import joblib
    model = joblib.load('C:/Users/syeda/OneDrive/Desktop/Internship-ML/internship/epromotion/mainapp/trained_model.joblib')
    prediction = model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m]])
    
    if prediction == 0:
        return "No Promotion"
    elif prediction == 1:
        return "Promotion"
    else:
        return "error"

def result(request):
    a = int(request.GET['empid'])
    b = int(request.GET['age'])
    c= int(request.GET['gender'])
    d = int(request.GET['education'])
    e = int(request.GET['department'])
    f= int(request.GET['region'])
    g = int(request.GET['recruitment'])
    i = int(request.GET['rating'])
    h = int(request.GET['training'])
    j = int(request.GET['score'])
    k = int(request.GET['service'])
    l = int(request.GET['kpi'])
    m = int(request.GET['award'])

    result = getPredictions(a,b,c,d,e,f,g,h,i,j,k,l,m)

    return render(request, 'projectapp/result.html', {'result':result})
        
