from flask import Flask ,render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime
import re
from html.parser import HTMLParser
import json

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
#print('CPO : ' , cpo_t)

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
    def __init__(self,cpoTable):
        self.cpoTable = cpoTable
        self.cpoYearMonth = ''
        cpoLastID = cpoTable[len(self.cpoTable)-1][0][-4:] if len(self.cpoTable) > 0 else 0
        #print("CPO QUO LAST 4 DIGITS : " , )
        #self.currentIndex = int(list(filter(str.isdigit, cpoTable[len(cpoTable)-1][0][-4:]))[0])
        self.currentIndex = int(cpoLastID)
        self.cpoID = self.gerenerate_currentID() 
    
    def gerenerate_currentID(self):
        return_id = ''

        #print("CPO CURRENT INDEX : " , self.currentIndex)
        self.cpoYearMonth = self.cpoTable[0][1].strftime("%Y%m")[2:] if len(self.cpoTable) > 0 else datetime.now().strftime("%Y%m")[2:]
        #print("CPO MONTH : " , self.cpoYearMonth)
        
        generate_id = (self.cpoYearMonth + "{0:0=4d}".format(self.currentIndex))
        return_id = ('quo' + str(generate_id))
        print("CPO RETURN ID : " , return_id)
        return return_id
    
    def generate_nextIndex(self):
        self.currentIndex += 1
        return_next_id = self.gerenerate_currentID()
        print("generate next index : " , return_next_id)
        return return_next_id

my_cpo_index = CPO_ID_INDEX(cpo_t)
cpo_id = my_cpo_index.cpoID

def test_insert_data(json_data):
    #co_id,co_date,pro_name,co_quantity,co_vat,cl_id,cus_name

    for string_json in json_data:
        json_load = json.loads(string_json)
    
    test_id = my_cpo_index.generate_nextIndex()
    print("JSON LOAD LEN : ", len(json_load))

    insert_product = []
    for p_data in json_load:
        print("P DATA  : " , p_data)
        if 'co_code' in p_data :
            test_name = p_data['co_code']
            test_quan = int(p_data['co_amount'])
            test_vat = float(p_data['co_vat'])
            insert_product.append([test_name,test_quan,test_vat])
        elif 'cus_name' in p_data:
            test_clerk = "clerk_dummy"
            test_cust = p_data['cus_name']
            #datetime_now = datetime.now()
            test_date = p_data['quo_date']
    
    print("INSERT PRODUCT LEN : ", len(insert_product))
    for in_data in insert_product:
        test_data = [test_id,test_date,in_data[0],in_data[1],in_data[2],test_clerk,test_cust]
        print("DATA TO INSERT : " , test_data)
        pythonMaria.pythonmaria_insert_customerorder(test_data)
        test_data = []


    #for att in dir(string_data):
    #    print (att, getattr(string_data,att))
    #print("TYPE : " , type(string_data))
    #print(dir(string_data))
    #print(getattr(string_data))

    # product_data = string_data.split(",")
    # print("CHECK PR DATA : " , product_data)

    # #test_id = cpo_id
    # test_id = my_cpo_index.generate_nextIndex()

    # for x in range(0, len(product_data), 6):
        
    #     datetime_now = datetime.now()
    #     test_date = datetime_now
    #     test_name = product_data[x+0]
    #     #print("PRODUCT [3] : " , product_data[3])
    #     #print(type(product_data[3]))
    #     test_quan = int(float(product_data[x+3]))
    #     test_vat = float(product_data[x+4])
    #     test_clerk = "clerk_dummy"
    #     test_cust = "customer_dummy"

    #     test_data = [test_id,test_date,test_name,test_quan,test_vat,test_clerk,test_cust]
    #     print(test_data)
    #     pythonMaria.pythonmaria_insert_customerorder(test_data)
    #     test_data = []
    
    #quo_data = 
    #pythonMaria.pythonmaria_insert_quotation(quo_data)

# @app.route('/tablesSelling.html')
# def tablesSelling():
#     return render_template('tablesSelling.html',t_product=product_t)

@app.route('/tablesSelling.html', methods=["GET", "POST"]) 
def tablesSelling():

    if request.method == 'POST':
        #print ("REQUEST DATA : " , request.data)
        #print("KEYS : " , request.form.keys)
        the_json = request.form.getlist('savechange')
        print("THE JSON : " , the_json)
        print("THE JSON LEN : " , len(the_json))
        print("TYPE OF THE JSON : " , type(the_json))
        # the_dict = request.form.to_dict()
        # print("THE DICT : " , the_dict)
        # print("THE DICT LEN : " , len(the_dict))
        # print("TYPE OF THE DICT : " , type(the_dict))
        #this template simply prints it out and all that I get is b"
        test_insert_data(the_json)
        #return redirect(url_for('tablesSelling'))

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
