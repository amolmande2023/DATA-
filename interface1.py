from flask import Flask,render_template,jsonify,request
from utils1 import JobPlacement
import traceback
import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route('/predict_charges', methods = ['GET','POST']) 
def predict_charges():
    try:
        if request.method == "POST":
            data = request.form.get

            print("User Data is :",data)
            gender   = data("gender")
            ssc_percentage   = eval(data("ssc_percentage"))
            ssc_board      = data('ssc_board')
            hsc_percentage = eval(data("hsc_percentage"))
            hsc_board   = data("hsc_board")
            hsc_subject = data("hsc_subject")
            degree_percentage   = eval(data("degree_percentage"))
            undergrad_degree   = data("undergrad_degree")
            work_experience   = data("work_experience")
            emp_test_percentage   = eval(data("emp_test_percentage"))
            specialisation   = data("specialisation")
            mba_percent   = eval(data("mba_percent"))
            
            job_placement = JobPlacement(gender,ssc_percentage,ssc_board,hsc_percentage,hsc_board,hsc_subject,degree_percentage,undergrad_degree,work_experience,emp_test_percentage,specialisation,mba_percent)
            charges = job_placement.get_pridected_price()
            if charges == 1:
                return render_template("index1.html", prediction = "Placed")
            else:
                return render_template("index1.html", prediction = "Not Placed")
    
        else:
            data = request.args.get

            print("User Data is :",data)
            gender   = data("gender")
            ssc_percentage   = eval(data("ssc_percentage"))
            ssc_board      = data('ssc_board')
            hsc_percentage = eval(data("hsc_percentage"))
            hsc_board   = data("hsc_board")
            hsc_subject = data("hsc_subject")
            degree_percentage   = eval(data("degree_percentage"))
            undergrad_degree   = data("undergrad_degree")
            work_experience   = data("work_experience")
            emp_test_percentage   = eval(data("emp_test_percentage"))
            specialisation   = data("specialisation")
            mba_percent   = eval(data("mba_percent"))
            
            job_placement = JobPlacement(gender,ssc_percentage,ssc_board,hsc_percentage,hsc_board,hsc_subject,degree_percentage,undergrad_degree,work_experience,emp_test_percentage,specialisation,mba_percent)
            charges = job_placement.get_pridected_price()
            if charges == 1:
                return render_template("index1.html", prediction ="Placed")
            else:
                return render_template("index1.html", prediction = "Not Placed")
    except:
        print(traceback.print_exc())
        return jsonify({"Message" : "Unsuccessful"})            

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config.Port_Number,debug=True)  

            
