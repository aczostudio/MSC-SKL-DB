$(document).ready(function() 
{
    $("#add_row").on("click", function() 
    {

        var data = maria_product;
        //console.log("PRODUCT DATA"+ data); 
        //console.log("PRODUCT DATA : " + Object.values(data));
        var table_log = document.getElementById("tab_logic");
        var array = table_log.getElementsByClassName("tr_item");

        for (var i = 0; i < array.length; i++)
        {
            //console.log(array[i].id);
            var tr_index = parseInt(array[i].id.replace("addr", ""));
            //console.log("TR INDEX : " + tr_index);

            update_db_row(data, tr_index);
        }

        //var index = (table_log.rows.length - 2);
        // console.log("SET DB NEW ROW : " + table_index);
        
    });
});

function update_db_row (product_data, table_index)
{
    var str_table   = 'addr'+table_index;
    var str_code    = 'productcode'+table_index;
    var str_desc    = 'productdesc'+table_index;
    var str_price   = 'price'+table_index;
    var str_amount  = 'amount'+table_index;
    var str_vat     = 'vat'+table_index;
    var str_total   = 'totalprice'+table_index;
    //console.log("STR PRODUCT : " + str_code);
    var table       = document.getElementById(str_table);
    var chile_td    = table.getElementsByTagName("td");
    var code        = document.getElementsByName(str_code)[0];
    //var desc  = chile_td[1];
    var desc        = document.getElementsByName(str_desc)[0];
    //var pric  = chile_td[2];
    var pric        = document.getElementsByName(str_price)[0];
    var amoun       = document.getElementsByName(str_amount)[0];
    var vat         = document.getElementsByName(str_vat)[0];
    //var total_p = chile_td[5];
    var total_p     = document.getElementsByName(str_total)[0];
    

    //add_product_option(product_data,code);
    //set_db_product(product_data, sl_product,td_desc,tx_price,tx_totalprice,input_amount,sl_vat);
    
    if (code.length == 0) 
    {
        console.log("CODE IF 1");
        code.options.length = 0;
        for (i = 0; i <= product_data.length; i++)
        {
            if(!!product_data[i])
            {
                // console.log(Object.values(product_data[i]));
                code.add(new Option(product_data[i][0]));
            }
        }
        console.log("CODE OPT INDEX : " + code.selectedIndex);
        code.selectedIndex = 0;
    }
    else if(!code.selectedIndex || code.selectedIndex >= 0)
    {
        //console.log("CODE IF 2");
    }
    else
    {
        //console.log("CODE IF 3");
        code.selectedIndex = 0;
    }

    
    //console.log("DESC VAL : " + desc.value );
    if(!desc.value || desc.value == product_data[0][1]){desc.value = product_data[0][1];}
    //desc.disabled = true;
    //console.log("PRIC VAL : " + pric.value );
    if(!pric.value || pric.value == product_data[0][2]){pric.value = product_data[0][2];}
    //pric.disabled = true;
    //code.selectedIndex = "0";
    if(!amoun.value){amoun.value = 0;}
    if(vat.selectedIndex !== 1){vat.selectedIndex = "0";}

    code.onchange = function()
    {
        // console.log("ON CHANGE!");
        var options = code.selectedIndex;
        // console.log(options);
        desc.value = product_data[options][1];
        pric.value = product_data[options][2];
        if(!!(amoun) && !!(pric))
        {
            var ctotal = 0.0 + (+(pric.value) * +(amoun.value));
            // console.log("VALUES PRIC : " + pric.value);
            // console.log("VALUES AMOUN : " + amoun.value);
            var cVat = 1.0 + +(vat.value);
            // console.log("VALUES VAT : " + vat.value);
            var total_vat = (ctotal*cVat).toFixed(2);
            // console.log("TOTAL VAT : " + total_vat);
            total_p.value = total_vat;
        }
        else
        {
            console.log("INPUT AMOUNT OR TX PRICE NULL");
        }
    }

    amoun.onchange = function()
    {
        var ctotal = 0.0 + (+(pric.value) * +(amoun.value));
            // console.log("VALUES PRIC : " + pric.value);
            // console.log("VALUES AMOUN : " + amoun.value);
            var cVat = 1.0 + +(vat.value);
            // console.log("VALUES VAT : " + vat.value);
            var total_vat = (ctotal*cVat).toFixed(2);
            // console.log("TOTAL VAT : " + total_vat);
            total_p.value = total_vat;
    }

    vat.onchange = function()
    {
        var ctotal = 0.0 + (+(pric.value) * +(amoun.value));
            // console.log("VALUES PRIC : " + pric.value);
            // console.log("VALUES AMOUN : " + amoun.value);
            var cVat = 1.0 + +(vat.value);
            // console.log("VALUES VAT : " + vat.value);
            var total_vat = (ctotal*cVat).toFixed(2);
            // console.log("TOTAL VAT : " + total_vat);
            total_p.value = total_vat;
    }
    settting_del_button();
}
