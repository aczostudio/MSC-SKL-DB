function update_quo_table(table_id, quo_data,toggle_table)
{
    var table_top = document.getElementById(table_id);
    var table_bod = table_top.getElementsByTagName('tbody')[0];

    var btn = document.createElement('button');
    btn.setAttribute('type'         , 'button');
    btn.setAttribute('class'        , 'accordion-toggle');
    btn.setAttribute('data-toggle'  , 'collapse');
    btn.setAttribute('data-target'  , toggle_table);
    btn.innerHTML += (' <i class = "fas fa-plus"></i>');

    var row = "";
    row += '<tr>' + 
    '<td>' + quo_data[0] + '</td>' + 
    '<td>' + quo_data[1].replace(" 00:00:00 GMT","") + '</td>' + 
    '<td>' + quo_data[2] + '</td>' + 
    '<td>' + quo_data[3] + '</td>' + 
    '<td>' + quo_data[4] + '</td>' + 
    '<td>' + quo_data[5] + '</td>' + 
    '</tr>';

    table_bod.innerHTML += row;
    var last_row = table_top.rows[table_top.rows.length-1];
    var last_cell = last_row.insertCell(0);
    last_cell.appendChild(btn);
}