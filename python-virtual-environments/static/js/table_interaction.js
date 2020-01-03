function totalprice_cal_vat(price,amount,vat)
{
    var total = 0.0 + (+(price) * +(amount));
    var cVat = 1.0 + +(vat);
    var total_vat = (total*cVat).toFixed(2);

    return total_vat;
}

function add_product_option(db_product, option_product)
{
    if (option_product.length > 0) {
        x.remove(x.length-1);
    }

    for (i = 0; i <= db_product.length; i++)
    {
        if(!!db_product[i])
        {
            //console.log(Object.values(db_product[i]));
            option_product.add(new Option(db_product[i][0]));
        }
    }
}

function set_db_product(db_product, sl_product,td_desc,tx_price,tx_totalprice,input_amount,sl_vat)
{
    td_desc.value = db_product[0][1];
    td_desc.disabled = true;
    tx_price.value = db_product[0][2];
    tx_price.disabled = true;
    tx_totalprice.disabled = true;

    sl_product.onchange = function()
    {
        console.log("ON CHANGE!");
        var sl_options = sl_product.selectedIndex;
        console.log(sl_options);
        td_desc.value = db_product[sl_options][1];
        tx_price.value = db_product[sl_options][2];
        if(!!(input_amount) && !!(tx_price))
        {
            tx_totalprice.value = totalprice_cal_vat(input_amount.value,tx_price.value,sl_vat.value);
        }
        else
        {
            console.log("INPUT AMOUNT OR TX PRICE NULL");
        }
    }

    input_amount.onchange = function()
    {
        tx_totalprice.value = totalprice_cal_vat(input_amount.value,tx_price.value,sl_vat.value);
    }

    sl_vat.onchange = function()
    {
        tx_totalprice.value = totalprice_cal_vat(input_amount.value,tx_price.value,sl_vat.value);
    }
}
