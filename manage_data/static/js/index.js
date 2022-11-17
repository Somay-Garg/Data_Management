function addSponsors(spon) {
  let nspons = parseInt(spon);
  let inputSponsors = document.querySelector("#inputSponsors");
  let sponsLabel = document.querySelector(".sponsors");
  
  let tmp = `<div class="sponsors">
    <label class="w-25" for="exampleFormControlInput1">Sponsor Name</label>
    <input type="text" name="sponsored_by" class = "w-30 m-1 sponsored_by_name" >
    <label class="w-25" for="exampleFormControlInput1">Sponsored Amount</label>
    <input type="number" name="spons_amount" id="" class = "w-30 m-1 spons_amt_individually" oninput = "findTotal();displaySponsors()" required>
  </div>`;

  removeSponsors();
  for (let i = 0; i < nspons; i++){
    let child = document.createElement("div");
    child.innerHTML = tmp;
    inputSponsors.append(child);
  }
}

function displaySponsors(){
  let spons_names = document.querySelectorAll(".sponsored_by_name");
  let spons_amts = document.querySelectorAll(".spons_amt_individually");
  let textarea = document.querySelector(".spons_text");
  textarea.value = "";
  let value = textarea.value;
  let spon_obj = {};
  for(let i=0;i<spons_amts.length;i++){
    let obj ={
      name:spons_names[i].value,
      amt:spons_amts[i].value
    }
    spon_obj[obj.name] = obj.amt;
  }
  textarea.value = JSON.stringify(spon_obj);
}

function updateTextArea(){
  let textarea = document.querySelector('#all_department')
  textarea.value = document.querySelector("department").value; 

}

function removeSponsors() {
  let inputSponsors = document.querySelector("#inputSponsors");
  var elements = inputSponsors.getElementsByClassName("sponsors");

  while (elements[0]) {
    elements[0].parentNode.removeChild(elements[0]);
  }
}

function findTotal() {
  let arr = document.querySelectorAll(".spons_amt_individually");
  var tot=0;
    for(var i=0;i<arr.length;i++){
        if(parseInt(arr[i].value))
            tot += parseInt(arr[i].value);
    }
    document.getElementById('total').value = tot;
}

$(document).ready(function () {
    $("select").each(function(){
        $(this).select2();
    });
});

function getSocieties(){
  $('#all_society').val($('#society').val().toString());
  console.log($('#all_society').val());
}

function getDepartments(){
  let society = $('#department').val().toString();
  if(society.includes('All')){
    society = "All"
  }
  $('#all_department').val(society);
  console.log($('#all_department').val());
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
    display_col = [];
    
    $('.display_columns').each(function(){
        if(!$(this).find('input').is(':checked')){
            col_id_arr = $(this).find('input').attr('id').split('_');
            col_name = col_id_arr[0];
            for(let i=1;i<col_id_arr.length-1;i++){
                col_name += '_'+col_id_arr[i];
            }
            display_col.push(col_name);
        }
    });

    $('#display_columns').val(display_col);
    // console.log(JSON.parse($('#filter_data').val()));
}