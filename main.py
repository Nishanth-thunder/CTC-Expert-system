from flask import Flask
from flask import render_template,request
app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def form():
    a=""
    b=""
    c=""
    d=""
    e=""
    f=""
    g=""
    r=""
    points=0
    if request.method =='POST' and 'name' in request.form:
        a = request.form.get('name')
        b = request.form.get('trek')
        c = request.form.get('exp')
        d = request.form.get('done')
        e = request.form.get('forest')
        f = request.form.get('swim')
        g = request.form.get('medi')
        if b.upper()=="YES":
            points=points+1
        if c.upper()=="YES":
            points=points+1
        if d.upper()=="YES":
            points=points+1
        if e.upper()=="YES":
            points=points+1
        if f.upper()=="YES":
            points=points+1
        if g.upper()=="NO":
            points=points+1
        if c.upper()=="YES" and f.upper()=="NO":
            points=points-1

        if g.upper()=="YES":
            r="KINDLY TREAT THE MEDICAL ISSUE AND APPLY...THANK YOU!"
        elif points==6:
            r="CONGRATS!YOU WILL BE CALLED FOR INTERVIEW SOON!!"
        elif points<=1:
            r="SORRY! YOU ARE REJECTED... WISHES FROM CTC FOR MORE OPPORTUNITIES"
        elif points > 0 and points < 6:
            r = "KINDLY SEND YOUR TREKKING PHOTOS TO dn6832@gmail.com.... WE WILL SEND THE RESPONSE SOON"
    return render_template("index.html",a=a,r=r)


app.run()











