import re
import json
import os

from flask import Flask ,render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime
from html.parser import HTMLParser
from pythonMaria import pythonMaria

app = Flask(__name__) 
mysql = MySQL(app)
ptMaria = pythonMaria()

product_t = ptMaria.pythonMaria_SelectStar("product")
cpo_t = ptMaria.pythonMaria_SelectStar("customerproductorder")
quo_t = ptMaria.pythonMaria_SelectStar("quotation")
cpoANDpro_t = ptMaria.pythonmaria_innerjoin_cpoANDpro()
print('CPO and PRO : ' , cpoANDpro_t)

ptMaria.pythonMaria_closeConnect()

def generate_cpo_id(quo_l_index, adding_index):
    cpo_month = cpo_t[0][1].strftime("%Y%m")
    cpo_month = cpo_month[2:]
    cpo_id_num = int("".join(filter(str.isdigit, quo_l_index)))
    
    cpo_month += "{0:0=4d}".format(cpo_id_num)
    cpo_return_id = ('quo' + str(cpo_month))
    return cpo_return_id

class CPO_ID_INDEX:
    def __init__(self,cpoTable):
        self.cpoTable = cpoTable
        self.cpoYearMonth = ''
        cpoLastID = cpoTable[len(self.cpoTable)-1][0][-4:] if len(self.cpoTable) > 0 else 0
        self.currentIndex = int(cpoLastID)
        self.cpoID = self.gerenerate_currentID() 
    
    def gerenerate_currentID(self):
        return_id = ''
        self.cpoYearMonth = self.cpoTable[0][1].strftime("%Y%m")[2:] if len(self.cpoTable) > 0 else datetime.now().strftime("%Y%m")[2:]
        generate_id = (self.cpoYearMonth + "{0:0=4d}".format(self.currentIndex))
        return_id = ('quo' + str(generate_id))
        return return_id
    
    def generate_nextIndex(self):
        self.currentIndex += 1
        return_next_id = self.gerenerate_currentID()
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
            quo_number = p_data['quo_num']
        elif 'quo_ttl' in p_data:
            quo_total = float(p_data['quo_ttl'])
            quo_vatprice = float(p_data['quo_vat'])
            quo_nettotal = float(p_data['quo_net'])
    
    print("INSERT PRODUCT LEN : ", len(insert_product))
    for in_data in insert_product:
        test_data = [test_id,test_date,in_data[0],in_data[1],in_data[2],test_clerk,test_cust]
        print("DATA TO INSERT : " , test_data)
        ptMaria.pythonmaria_insert_customerorder(test_data)
        test_data = []

    #quo_id,quo_date,quo_total,quo_vat,quo_net,cpo_id
    quo_data = [test_id,test_date,quo_total,quo_vatprice,quo_nettotal,test_id]
    print("QUO TO INSERT : " , quo_data)
    ptMaria.pythonmaria_insert_quotation(quo_data)

    quo_t = quo_t = ptMaria.pythonMaria_SelectStar("quotation")
    print('UPDATE QUO : ' , quo_t)

@app.route('/')
@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/tablesEmployee.html')
def tablesEmployee():
    return render_template('underconstruction.html')

@app.route('/tablesCustomer.html')
def tablesCustomer():
    return render_template('underconstruction.html')

@app.route('/tablesProduct.html')
def tablesProduct():
    return render_template('underconstruction.html')

@app.route('/tablesSelling.html', methods=["GET", "POST"]) 
def tablesSelling():
    if request.method == 'POST':
        the_json = request.form.getlist('savechange')
        test_insert_data(the_json)

    return render_template('tablesSelling.html',t_product=product_t,t_quotation = quo_t)

@app.route('/tablesPurchasing.html') 
def tablesPurchasing():
    return render_template('underconstruction.html')

@app.route('/404.html')
def err404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(port=88,debug=True)

def oldroute():
    print("OLD ROUTE")
    # @app.route('/blank.html')
    # def blank():
    #     return render_template('blank.html')

    # @app.route('/buttons.html')
    # def buttons():
    #     return render_template('buttons.html')

    # @app.route('/cards.html')
    # def cards():
    #     return render_template('cardstest.html')

    # @app.route('/charts.html')
    # def charts():
    #     return render_template('charts.html')

    # @app.route('/forgot-password.html')
    # def forgot_password():
    #     return render_template('forgot-password.html')

    # @app.route('/utilities-animation.html')
    # def utilities_animation():
    #     return render_template('utilities-animation.html')

    # @app.route('/utilities-border.html')
    # def utilities_border():
    #     return render_template('utilities-border.html')

    # @app.route('/utilities-color.html')
    # def utilities_color():
    #     return render_template('utilities-color.html')

    # @app.route('/utilities-other.html')
    # def utilities_other():
    #     return render_template('utilities-other.html')

    # @app.route("/mrdb.html")
    # def mrdb():
    #     return render_template('inventory.html')

    # @app.route('/register.html')
    # def register():
    #     return render_template('register.html')

    # @app.route('/tables.html')
    # def tables():
    #     return render_template('tables.html')

    # @app.route('/tablesAccountant.html') 
    # def tablesAccountant():
    #     return render_template('tablesAccountant.html')

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


