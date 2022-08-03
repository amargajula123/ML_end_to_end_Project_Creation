from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
        return "this is my first deployment using triggers and docker with the hepl of git hub"
   

 
if __name__=="__main__":
    app.run(debug=True)