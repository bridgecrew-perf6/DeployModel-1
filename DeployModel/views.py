from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, "home.html")

def result(request):

    model = joblib.load('model3.sav') 

    param = []
    
    param.append(request.GET['ftp_yes_no'])
    param.append(request.GET['ne_yes_no'])
    param.append(request.GET['ce_yes_no'])
    param.append(request.GET['cpe_yes_no'])
    param.append(request.GET['nce_yes_no'])
    param.append(request.GET['ce2_yes_no'])
    param.append(request.GET['ap_yes_no'])
    param.append(request.GET['rba_yes_no'])
    param.append(request.GET['se_yes_no'])
    param.append(request.GET['hd_yes_no'])
    param.append(request.GET['wv_yes_no'])
    param.append(request.GET['sh_yes_no'])
    wage_level = request.GET['Wagelevel']
    if(wage_level == "Level I") : param.extend(['1','0','0','0'])
    elif(wage_level == "Level II") : param.extend(['0','1','0','0'])
    elif(wage_level == "Level III") : param.extend(['0','0','1','0'])
    elif(wage_level == "Level IV") : param.extend(['0','0','0','1'])
    statutary = request.GET['statutary']
    if(statutary == "Degree"): param.extend(['0','1','0'])
    elif(statutary == "Wage"): param.extend(['0','0','1'])
    elif(statutary == "Both"): param.extend(['1','0','0'])
    public_dis = request.GET['Publicdis']
    if(public_dis == "Place of Business"): param.extend(['0','1','0'])
    elif(public_dis == "Place of Employment"): param.extend(['0','0','1'])
    elif(public_dis == "Both"): param.extend(['1','0','0'])


    


    for i in range(len(param)):
        if(param[i] == 'Yes'):
            param[i] = '1'
        elif(param[i] == "No"):
            param[i] = '0'

    ans = model.predict([param])
    if(ans[0] == 0):
        ans = "Withdrawn"
        return render(request,"withdrawn.html", {'ans': ans})
    else:
        ans = "Certified"
        return render(request,"certified.html", {'ans': ans})


