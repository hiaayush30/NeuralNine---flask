from flask import Flask,request,make_response

app = Flask(__name__)

@app.route("/",methods = ['GET'])
def index():
    return "Hello World"


# dynamic urls
@app.route("/add/<int:num1>/<int:num2>")
def add(num1,num2):
    # return f"Sum:{int(num1) + int(num2)}"
    return f"Sum:{num1 + num2}\n"

# url parameters
@app.route("/hello")   #hello?name=Aayush
def greet():
    if "name" not in request.args.keys():
        return f"I see what you did there\n"
    
    if request.method == "POST":
        return "POST method not allowed for now :-)\n ",201
    
    # crafting custom response
    response = make_response(f"hello there {request.args.get("name","bob")}\n")
    response.status_code = 204
    # response.headers['content-type'] = 'application/json'
    response.content_type = 'application/json'

    # return f"hello there {request.args.get("name","bob")}\n"
    return response
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True) # debug=True similar to nodemon

# 0.0.0.0 is for localhost as well as pvt ip address