from flask import Flask,request

app = Flask(__name__)

@app.route('/input_url')
def input():
    data= request.args.get('x')
    return "This is my input from url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug="True")
