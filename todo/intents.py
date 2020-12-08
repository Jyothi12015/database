name=''
weight=''
height=''
def get_intent(data):
    global name
    global weight
    global height
    m=data['message'].lower()
    if data['key']=="name":
        name=m
        return "next"
    if data['key']=='Weight':
        weight=m
        return "bmiheight"
    if data['key']=='height':
        height=m
        return "bmi"
    
    if any(x in m for x in ["game","play","snake"]):
        return "game"
    elif any(x in m for x in ["calculate","bmi"]):
        return "bmiweight"
    else:
        return "echo"

def handle(data):
    global name
    global height
    global weight
    from flask import render_template
    intent = get_intent(data)
    if intent =='game' :
        return render_template('gameafter.html',  question={'key': '','text':''})
    elif intent=='bmi' :
        from .bmi import BMI
        str=BMI(height, weight)
        return render_template('messages/afterbmi.html',str=str, question={'key': '','text':''})
    elif intent == 'bmiweight':
        return render_template('messages/bmi.html',question={'key':'Weight','text':'Enter the weight in kgs'})
    elif intent == 'bmiheight':
        return render_template('messages/bmi.html',question={'key':'height','text':'Enter the height in meters'})
    elif intent=='next':
         return render_template('messages/greet.html',name=name,question={'key':'Request','text':'What would you like to do with me'})
    else:
        return render_template('messages/extra.html',data=data ,  question={'key': '','text':''})