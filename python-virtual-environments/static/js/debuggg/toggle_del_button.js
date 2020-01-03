function settting_del_button()
{
    //console.log("SETTING DEL BUTTON");
    var table_log = document.getElementById("tab_logic");
    var table_len = table_log.rows.length - 1;
    //console.log("TABLE LEN : " + table_len);
    var array = table_log.getElementsByClassName("tr_item");

    for (var k = 0; k < array.length; k++)
    {
        //console.log(array[k].id);
        var tr_index = parseInt(array[k].id.replace("addr", ""));
        //console.log("TR INDEX : " + tr_index);

        var str_delbtn = 'del'+tr_index;
        //console.log("DEL INDEX : " + str_delbtn);
        var get_delbtn = document.getElementsByName(str_delbtn)[0];

        if(array.length >= 2)
        {
            //console.log("TABLE LEN >= 2 : " + array.length);
            toggle_show_del_button(get_delbtn); 
        }
        else
        {
            //console.log("TABLE LEN < 2 : " + array.length);
            toggle_hide_del_button(get_delbtn);
        }
    }
}

function toggle_del_button(del_btn)
{
    if(typeof del_btn !== "undefined")
    { 
        if(del_btn.style.display == 'block')
            del_btn.style.display = 'none';
        else
            del_btn.style.display = 'block';
    }
}

function toggle_show_del_button(del_btn)
{
    if(typeof del_btn !== "undefined")
    { del_btn.style.display = 'block'; }
}

function toggle_hide_del_button(del_btn)
{
    //console.log("HIDE BTN");
    if(typeof del_btn !== "undefined")
    { del_btn.style.display = 'none'; }
}
