function add_sponsors(spon){
    spon = parseInt(spon);
    var spon_node = $('.clone_sponsors').find('input').clone();
    spon_node.prop("disabled",false);
    if(spon==0||isNaN(spon)){
        spon=1;
    }
    $('.actual_sponsors').html('');
    $('.actual_sponsors').append($('.clone_sponsors').find('label').clone());
    var sponsors = $('.actual_sponsors');
    for(var i=0;i<spon;i++){
        sponsors.append(spon_node.clone());
    }
    console.log(spon_node[0]);
}

function hide_show_table(col_name)
{
    var checkbox_val=document.getElementById(col_name).value;
    if(checkbox_val=="hide")
    {
        var all_col=document.getElementsByClassName(col_name);
        for(var i=0;i<all_col.length;i++)
        {
            all_col[i].style.display="none";
        }
        document.getElementById(col_name+"_head").style.display="none";
        document.getElementById(col_name).value="show";
    }

    else
    {
        var all_col=document.getElementsByClassName(col_name);
        for(var i=0;i<all_col.length;i++)
        {
            all_col[i].style.display="table-cell";
        }
        document.getElementById(col_name+"_head").style.display="table-cell";
        document.getElementById(col_name).value="hide";
    }
}