from flask import Flask ,render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime

# app = Flask(__name__)
import pythonMaria
import os
import json

def oldapproute():
    # @app.route('/')
    # def index():
    #     return "Flask App!"

    # @app.route("/hello/<string:name>/")
    # def hello(name):
    #     return render_template('test.html',name=name)

    # if __name__ == "__main__":
    #     app.run(host='0.0.0.0', port = 80)
    print("old app route")

def oldcode():
    # mysql = MySQL(app)

    # @app.route('/')
    # def users():
    #     cur = mysql.connection.cursor()
    #     cur.execute('''SELECT user, host FROM mysql.user''')
    #     rv = cur.fetchall()
    #     return str(rv)

    # import os from flask import send_from_directory 
    # @app.route('/favicon.ico') 
    # def favicon(): 
    #     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    # mariarows = pythonMaria.pythonMaria_Select2("Employee_ID","Employee_FirstName","employee")

    # @app.route("/mrdb/")
    # def mrdb():
    #     return render_template('inventory.html',rows=mariarows)

    # @app.route("/hello/")
    # def hello():
    #     # tempRender = tempRend.temp_Render()
    #     return tempRend.temp_Render()

    print("old code")

# template_dir = os.path.abspath('templates')
# app = Flask(__name__,template_folder=template_dir)
app = Flask(__name__) 
mysql = MySQL(app)
def users():
        cur = mysql.connection.cursor()
        cur.execute('''SELECT user, host FROM mysql.user''')
        rv = cur.fetchall() 
        return str(rv)
# app._static_folder = os.path.abspath("static")

# mariarows = pythonMaria.pythonMaria_Select2("Employee_ID","Employee_FirstName","employee")

# customer_t = pythonMaria.pythonMaria_SelectStar("customer")

@app.route('/')
@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route("/mrdb.html")
def mrdb():
    return render_template('inventory.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/tables.html')
def tables():
    return render_template('tables.html')

@app.route('/tablesEmployee.html')
def tablesEmployee():
    return render_template('tablesEmployee.html')

@app.route('/tablesCustomer.html')
def tablesCustomer():
    return render_template('tablesCustomer.html')

@app.route('/tablesProduct.html')
def tablesProduct():
    return render_template('tablesProduct.html')

product_t = pythonMaria.pythonMaria_SelectStar("product")
cpo_t = pythonMaria.pythonMaria_SelectStar("customerproductorder")
print('CPO : ' , cpo_t)

pythonMaria.pythonMaria_closeConnect()

def generate_cpo_id(quo_l_index, adding_index):
    cpo_month = cpo_t[0][1].strftime("%Y%m")
    cpo_month = cpo_month[2:]
    #print("CPO MONTH : " , cpo_month)

    cpo_id_num = int("".join(filter(str.isdigit, quo_l_index)))
    
    cpo_month += "{0:0=4d}".format(cpo_id_num)
    cpo_return_id = ('quo' + str(cpo_month))
    return cpo_return_id

#cpo_id = generate_cpo_id(str(cpo_t[len(cpo_t)-1][0]))
#print('CPO ID : ' , cpo_id)

class CPO_ID_INDEX:
    def __init__(self,lastIndex,cpoTable):
        self.lastIndex = lastIndex
        self.cpoTable = cpoTable
        self.currentIndex = gerenerate_curretnIndex(lastIndex)
    
    def gerenerate_curretnIndex(lIndex):
        cpo_month = self.cpoTable[0][1].strftime("%Y%m")
        cpo_month = cpo_month[2:]
        #print("CPO MONTH : " , cpo_month)

        cpo_id_num = int("".join(filter(str.isdigit, lIndex)))
        
        cpo_month += "{0:0=4d}".format(cpo_id_num)
        cpo_return_id = ('quo' + str(cpo_month))
        return cpo_return_id
    
    def generate_nextIndex():
        print("generate next index")


def test_insert_data(string_data):
    #co_id,co_date,pro_name,co_quantity,co_vat,cl_id,cus_name
    
    cpo_id = generate_cpo_id(str(cpo_t[len(cpo_t)-1][0]) , 0)
    print('CPO ID : ' , cpo_id)

    product_data = string_data.split(",")
    print("CHECK PR DATA : " , product_data)
    for x in range(0, len(product_data), 6):
        test_id = cpo_id
        now = datetime.now()
        test_date = now.strftime("%m/%d/%Y")
        test_name = product_data[0]
        #print("PRODUCT [3] : " , product_data[3])
        #print(type(product_data[3]))
        test_quan = int(float(product_data[3]))
        test_vat = float(product_data[4])
        test_clerk = "clerk_dummy"
        test_cust = "customer_dummy"

        test_data = [test_id,test_date,test_name,test_quan,test_vat,test_clerk,test_cust]

        pythonMaria.pythonmaria_insert_customerorder(test_data)
    
    #quo_data = 
    #pythonMaria.pythonmaria_insert_quotation(quo_data)

    

@app.route('/tablesSelling.html', methods=["GET", "POST"]) 
def tablesSelling():
    # if request.method == "POST":
    #     print (request.data)
    #     the_json = request.form.get('on_submit_co', None)
    #     #this template simply prints it out and all that I get is b"
    #     print (the_json)
    #     the_data = request.form['on_submit_co']
    #     print (the_data)
    #     return 'success'

    if request.method == 'POST':
        print (request.data)
        the_json = request.form.get('savechange', None)
        #this template simply prints it out and all that I get is b"
        print (the_json)
        test_insert_data(the_json)
        return redirect(url_for('tablesSelling'))

    return render_template('tablesSelling.html',t_product=product_t)

def old_Post():
    # @app.route('/postmethod', methods = ['POST'])
    # def get_post_javascript_data():
    #     jsdata = request.form['javascript_data']
    #     return json.loads(jsdata)[0]

    # @app.route('/test', methods=['GET', 'POST'])
    # def test():
    #     if request.method == 'POST':
    #         print (request.data)
    #         the_json = request.form.get('savechange', None)
    #         #this template simply prints it out and all that I get is b"
    #         print (the_json)
    #         return redirect(url_for('tablesSelling'))

    # @app.route('/tablesSelling.html', methods = ["POST"])
    # def tablesSelling_SubmitForm():
    #     if request.method == "POST":
    #         in_data = request.form['insert_data[]']
    #         print(in_data)
    #         print(type(in_data))
    #         if  not in_data:
    #             return redirect(url_for('tablesSelling'))
    #         else:
    #             return 'in_data failue'
    #     else:
    #         return 'post failue'
            
    #     if not (request.form.getlist('insert_data[]')) :
    #         print("GET POSTED")
    #         in_data = request.form.getlist('insert_data[]')
    #         print(in_data)
    #         print(type(in_data))
    #         db_tosave = request.form.get('savechange')
    #         if db_tosave is not None:
    #             desc = request.form['productcode0']
    #             print(desc)
    #             print(type(desc))
                
    #             # pythonMaria.pythonmaria_insert_customerorder(insert_data)
    #         return 'success' # redirect(url_for('tablesSelling'))
    return None

@app.route('/tablesPurchasing.html') 
def tablesPurchasing():
    return render_template('tablesPurchasing.html')

@app.route('/tablesAccountant.html') 
def tablesAccountant():
    return render_template('tablesAccountant.html')

@app.route('/404.html')
def err404():
    return render_template('404.html')

@app.route('/blank.html')
def blank():
    return render_template('blank.html')

@app.route('/buttons.html')
def buttons():
    return render_template('buttons.html')

@app.route('/cards.html')
def cards():
    return render_template('cardstest.html')

@app.route('/charts.html')
def charts():
    return render_template('charts.html')

@app.route('/forgot-password.html')
def forgot_password():
    return render_template('forgot-password.html')

@app.route('/utilities-animation.html')
def utilities_animation():
    return render_template('utilities-animation.html')

@app.route('/utilities-border.html')
def utilities_border():
    return render_template('utilities-border.html')

@app.route('/utilities-color.html')
def utilities_color():
    return render_template('utilities-color.html')

@app.route('/utilities-other.html')
def utilities_other():
    return render_template('utilities-other.html')

if __name__ == '__main__':
    app.run(port=80,debug=True)
