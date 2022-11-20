function addSponsors(spon) {
  let nspons = parseInt(spon);
  let inputSponsors = document.querySelector("#inputSponsors");
  let sponsLabel = document.querySelector(".sponsors");
  
  let tmp = `<div class="sponsors">
    <label class="col-2 col-form-label required_asterisk" for="exampleFormControlInput1">Sponsor Name</label>
    <input type="text" name="sponsored_by" class = "w-30 m-1 sponsored_by_name" >
    <label class="col-2 col-form-label required_asterisk" for="exampleFormControlInput1">Sponsored Amount</label>
    <input type="number" name="spons_amount" id="" class = "w-30 m-1 spons_amt_individually" oninput = "findTotal();displaySponsors()" required>
  </div>`;

  removeSponsors();
  for (let i = 0; i < nspons; i++){
    let child = document.createElement("div");
    child.innerHTML = tmp;
    insertAfter(child,document.querySelector("#sponsors"))
    // inputSponsors.append(child);
  }
}
function insertAfter(newNode, existingNode) {
  existingNode.parentNode.insertBefore(newNode, existingNode.nextSibling);
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

  $(function(){
    var dtToday = new Date();
  
    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
  
    if(month < 10)
        month = '0' + month.toString();
    if(day < 10)
        day = '0' + day.toString();
  
    var maxDate = year + '-' + month + '-' + day;    
    $('.datesettup').attr('max', maxDate);    
  });
  
  $(function(){
    let fieldvalue = document.querySelector("#end-date-setter").innerHTML
    // Nov. 19, 2022
    
    let mon = fieldvalue.substring(0,3)
    let month1 = "JanFebMarAprMayJunJulAugSepOctNovDec".indexOf(mon) / 3 + 1 
    
    let day_ =  fieldvalue.substring(5,7)
    let year_ =  fieldvalue.substring(9)
    let datePattern = year_ + '-' + month1 + '-' + day_;    
    console.log(datePattern)

    document.getElementById('end_date').value = datePattern
  });

    $(function(){
      let fieldvalue = document.querySelector("#start-date-setter").innerHTML
    // Nov. 19, 2022
    
    let mon = fieldvalue.substring(0,3)
    let month1 = "JanFebMarAprMayJunJulAugSepOctNovDec".indexOf(mon) / 3 + 1 
    
    let day_ =  fieldvalue.substring(5,7)
    let year_ =  fieldvalue.substring(9)
    let datePattern = year_ + '-' + month1 + '-' + day_;    
    console.log(datePattern)

    document.getElementById('start_date').value = datePattern
    });

    $(function(){
      let selectedValues = document.querySelector("#all_society").value.split(",");
      let options = document.querySelectorAll("#society > *")
      // console.log(options)
      
      for(let i=0;i<options.length;i++){
        let optionvalue = options[i].value
        // console.log(optionvalue)
        for(let j=0;j<selectedValues.length;j++){
          let selectedValue = selectedValues[j] 
          // console.log("selected value ====         "+selectedValue)
          if(selectedValue == optionvalue){ 
            // console.log("matched")
            // console.log(options[i])
            options[i].setAttribute("selected","true")
          }
        }        
      }
      getSocieties()
    });


    $(function(){
      let selectedValues = document.querySelector("#all_department").value.split(",");
      let options = document.querySelectorAll("#department > *")
      // console.log(options)
      
      for(let i=0;i<options.length;i++){
        let optionvalue = options[i].value
        // console.log(optionvalue)
        for(let j=0;j<selectedValues.length;j++){
          let selectedValue = selectedValues[j] 
          // console.log("selected value ====         "+selectedValue)
          if(selectedValue == optionvalue){ 
            // console.log("matched")
            // console.log(options[i])
            options[i].setAttribute("selected","true")
            options[i].click()
          }
        }        
      }
      getDepartments()

    });

  $(function(){
      let spondataJSON = document.querySelector("#sponDets").value;
      // console.log(spondataJSON);
      let parentDiv = document.querySelector("#inputSponsors");
      let sponData = JSON.parse(spondataJSON)
      console.log(sponData);
      let arr = Object.entries(sponData)
      console.log(arr);
      for(let i=0;i<arr.length;i++){
        let sponName = arr[i][0];
        let sponAmt = arr[i][1];
        let template = `<div class="sponsors">
        <label class="col-2 col-form-label required_asterisk" for="exampleFormControlInput1">Sponsor Name</label>
        <input type="text" name="sponsored_by" class = "w-30 m-1 sponsored_by_name" value = ${sponName} >
        <label class="col-2 col-form-label required_asterisk" for="exampleFormControlInput1">Sponsored Amount</label>
        <input type="number" name="spons_amount" id="" class = "w-30 m-1 spons_amt_individually" oninput = "findTotal();displaySponsors()" value =${sponAmt} required></div>`
        let child = document.createElement("div");
        child.innerHTML = template;
        parentDiv.appendChild(child)
      }
     
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
          // console.log("heloooooo");
            col_id_arr = $(this).find('input').attr('id').split('_');
            col_name = col_id_arr[0];
            for(let i=1;i<col_id_arr.length-1;i++){
                col_name += '_'+col_id_arr[i];
            }
            display_col.push(col_name);
        }
    });
    // console.log(display_col);
    $('#display_columns').val(display_col);
}

function updateAttendanceFileValue(){
  let textarea = document.querySelector("#upload_attendance_area")
  let inputval = document.querySelector("#attendance_div").childNodes[0].value
  console.log(inputval)
  textarea.value = inputval
}
