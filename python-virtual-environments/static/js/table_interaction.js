function totalprice_cal_vat(price,amount,vat)
{
    var total_vat = 0.0;
    var trans_price = price.replace(/,/g,'');
    console.log("amount : " + amount);
    console.log("price : " + parseInt(trans_price));
    console.log("vat : " + vat);
    var total = (parseInt(trans_price) * parseInt(amount));
    console.log("total : " + total);
    var cVat = 1.0 + (parseFloat(vat));
    var price_vat = (total * vat);
    total_vat = (total * cVat);

    // return {
    //     "t":total,
    //     "v":(total * vat),
    //     "n":total_vat
    //    };
    // console.log("T : " + total);
    // console.log("V : " + price_vat);
    // console.log("N : " + total_vat);
    // return [total,price_vat,total_vat];
    return total_vat;
}

function updating_net_vat()
{
    var post_net = 0.0;
    var post_vat = 0.0;

    var table_r = document.getElementById("tab_logic");
    // console.log(table_r.rows.length);
    //console.log(table_r.rows[1].cells);
    for (var i = 1; i < table_r.rows.length; ++i)
    {
        var f_pric = 'price'+(i-1);
        var fd_price = document.getElementsByName(f_pric)[0].value;

        var f_amoun = 'amount'+(i-1);
        var fd_amoun = document.getElementsByName(f_amoun)[0].value;

        cal_net = (parseFloat(fd_price.replace(/,/g,''))) * (parseFloat(fd_amoun.replace(/,/g,'')));
        post_net = (parseFloat(post_net)) + (parseFloat(cal_net));

        var f_vat = 'vat'+(i-1);
        var fd_vat = document.getElementsByName(f_vat)[0].value;

        cal_vat = cal_net * (parseFloat(fd_vat.replace(/,/g,'')));
        post_vat = (parseFloat(post_vat)) + (+parseFloat(cal_vat));
    }

    document.getElementsByName("pricetotal0")[0].value = (post_net).toLocaleString('en-US', {minimumFractionDigits: 2});

    document.getElementsByName("vattotal0")[0].value = (post_vat).toLocaleString('en-US', {minimumFractionDigits: 2});

    document.getElementsByName("nettotal0")[0].value = (post_net + post_vat).toLocaleString('en-US', {minimumFractionDigits: 2});
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

function updating_price_textfield(a,p,v,text_field)
{
    // console.log("UPDATE PRICE TX FIELD");
    // var return_result = totalprice_cal_vat(a,p,v);
    // console.log("T : " + return_result[0]);
    // console.log("V : " + return_result[1]);
    // console.log("N : " + return_result[2]);
    // text_field.value = return_result[2];
    // updating_net_vat(return_result[0],return_result[1]);
    var cal_price = 0.0;
    cal_price = totalprice_cal_vat(p,a,v);
    console.log("CAL PRICE : " + cal_price);
    text_field.value = (cal_price).toLocaleString('en-US', {minimumFractionDigits: 2});
    updating_net_vat();
}

function set_db_product(db_product, sl_product,td_desc,tx_price,tx_totalprice,input_amount,sl_vat)
{
    td_desc.value = db_product[0][1];
    // td_desc.disabled = true;
    tx_price.value = (parseFloat(db_product[0][2])).toLocaleString('en-US', {minimumFractionDigits: 2});
    // tx_price.disabled = true;
    // tx_totalprice.disabled = true;

    sl_product.onchange = function()
    {
        // console.log("PRODUCT ON CHANGE");
        //console.log("ON CHANGE!");
        var sl_options = sl_product.selectedIndex;
        //console.log(sl_options);
        td_desc.value = db_product[sl_options][1];
        tx_price.value = (parseFloat(db_product[sl_options][2])).toLocaleString('en-US', {minimumFractionDigits: 2});
        if(!!(input_amount) && !!(tx_price))
        {
            updating_price_textfield(input_amount.value,tx_price.value,sl_vat.value,tx_totalprice);
            // return_result = totalprice_cal_vat(input_amount.value,tx_price.value,sl_vat.value);
            // tx_totalprice.value = return_result[2];
            // updating_net_vat(return_result[0],return_result[1]);
        }
        else
        {
            console.log("INPUT AMOUNT OR TX PRICE NULL");
        }
    }

    input_amount.onchange = function()
    {
        // console.log("AMOUNT ON CHANGE");
        // console.log("T : " + input_amount.value);
        // console.log("V : " + tx_price.value);
        // console.log("N : " + sl_vat.value);
        updating_price_textfield(input_amount.value,tx_price.value,sl_vat.value,tx_totalprice);
        // return_result = totalprice_cal_vat(input_amount.value,tx_price.value,sl_vat.value);
        // tx_totalprice.value = return_result[2];
        // updating_net_vat(return_result[0],return_result[1]);
    }

    sl_vat.onchange = function()
    {
        // console.log("VAT ON CHANGE");
        // console.log("T : " + input_amount.value);
        // console.log("V : " + tx_price.value);
        // console.log("N : " + sl_vat.value);
        updating_price_textfield(input_amount.value,tx_price.value,sl_vat.value,tx_totalprice);
        // return_result = totalprice_cal_vat(input_amount.value,tx_price.value,sl_vat.value);
        // tx_totalprice.value = return_result[2];
        // updating_net_vat(return_result[0],return_result[1]);
    }
}
