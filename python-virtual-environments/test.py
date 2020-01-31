import json

the_json = []
the_json.append('{"co_code":"BA-CYLN-HWAYAN","co_desc":"BA Cylinder brand Hwayan","co_price":10000,"co_amount":"1","co_vat":"0.07","co_total":10700},{"co_code":"FE-AF-20L","co_desc":"Foam AFFF 3% Size:20Ltrs.","co_price":5500,"co_amount":"02","co_vat":"0","co_total":11000}')
dump_data = []
print("THE JSON : " , the_json)
print("THE JSON LEN : " , len(the_json))
print("TYPE OF THE JSON : " , type(the_json))

for j_d in the_json:
    print("J_D : " , j_d)
    print("J_D TYPE : " , type(j_d))
    data_to_load = "["
    data_to_load += j_d
    data_to_load += "]"
    test_load = json.loads(data_to_load)

    print("TEST LOAD : " , test_load)
    print("TEST LOAD TYPE : " , type(test_load))
    #dump_data.append(j_d)

print("DUMP DATA : " , dump_data)
print("DUMP DATA TYPE : " , type(dump_data))

#load_data = json.loads(dump_data)
