def BMI(height, weight): 
        h=int(float(height))
        w=int(float(weight))
        bmi = w/(h**2) 
        
    
        if (bmi < 18.5): 
            return "Underweight and Your BMI is","{:.2f}".format(bmi),"kg/m^2."
        elif ( bmi >= 18.5 and bmi < 24.9): 
            return "Healthy and Your BMI is","{:.2f}".format(bmi),"kg/m^2."
        elif ( bmi >= 24.9 and bmi < 30): 
            return "overweight and Your BMI is","{:.2f}".format(bmi),"kg/m^2."
        else : 
            return "Suffering from Obesity and Your BMI is","{:.2f}".format(bmi),"kg/m^2."
        
    
    



