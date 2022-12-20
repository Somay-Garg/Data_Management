function addSponsors(spon) {
  let nspons = parseInt(spon);
  let inputSponsors = document.querySelector("#insertSponsDets");
  let sponsLabel = document.querySelector(".sponsors");
  let tmp = `
  <div class="sponsors" >
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Sponsor Name</label>
     <input type="text" name="sponsored_by" style="height:32px; border-radius: 4px;" class = "w-30 m-1 sponsored_by_name">
    </div>
    <div class="form-group  align-center float-child">  
     <label class=" w-25 spon_amt required_asterisk" style="width:153px;"  for="exampleFormControlInput1">Sponsored Amount</label>
     <input type="number" name="spons_amount" id="" style="height:32px; border-radius: 4px;" class = "w-30 m-1 spons_amt_individually" oninput = "findTotal();displaySponsors()" required>
    </div>
  <div>`;

  $("#insertSponsDets").html('');

  for (let i = 0; i < nspons; i++) {
    let child = document.createElement("div");
    // child.setAttribute("class",'sponsors')
    child.innerHTML = tmp;
    // insertAfter(child, document.querySelector("#sponsors"));
    inputSponsors.appendChild(child);
  }
}

function addColumns(cols) {
  let ncols = parseInt(cols);
  if(ncols >14){
    // alert("Not more than 14 columns are allowed");
    return false;
  }
  let inputColumns = document.querySelector("#inputColumns");
  let template = `
    <div class = "field_columns" style = "display: flex; margin-bottom: 20px; width: 78%; align-items: center;  justify-content: center;">
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Field:</label>
      <select class="fill-columns" class="w-30 m-1" oninput="getFields()" onmouseover = "disableFields(this,'fill-columns')" style = "height: 30px;border-radius: 4px;">
          <option value="-1">Select Values</option>
          <option value="event_name">Event Name</option>
          <option value="type_of_event">Type of Event</option>
          <option value="Audience">Audience</option>
          <option value="Societies">Societies</option>
          <option value="Departments">Departments</option>
          <option value="Organized_by">Organized By</option>
          <option value="Conducted_by">Conducted By</option>
          <option value="sponsors_details">Sponsors Details</option>
          <option value="total_sponsored_amt">Total Sponsored Amount</option>
          <option value="start_date">Start Date</option>
          <option value="end_date">End Date</option>
          <option value="no_of_participants">No of Participants</option>
          <option value="upload_attendance">Download Attendance</option>
          <option value="upload_report">Download Report</option>
      </select>
    </div>    
  `;

  // console.log(ncols)
  removeChildren(document.getElementsByClassName("field_columns"));
  for (let i = 0; i < ncols; i++) {
    let child = document.createElement("div");
    child.style = 'display: inline-block;width: 40%; margin-left: 98px;box-sizing: border-box;';
    child.innerHTML = template;
    inputColumns.append(child);
  }
  
}



function disableFields(field){
  var arr = [];
   $(".fill-columns").each(function(){
    let val  = $(this).val();
    // console.log(val);
    if(val != '-1'){
      arr.push(val)
    }
   });
  //  console.log(arr);

   let options = field.querySelectorAll('option');
   for(let i=0;i<options.length;i++){
    
    if(arr.includes(options[i].value)){
      // console.log('disabled'+options[i].value)
      options[i].disabled = true;
    }else{
      if(options[i].disabled){
        options[i].disabled = false;
      }
    }
   }
}

function getFields() {
  let area = document.querySelector("#fillColumns");
  let cols = document.querySelectorAll(".fill-columns");
  area.value = "";
  let arr = ["id"];
  for (let i = 0; i < cols.length; i++) {
    arr.push(cols[i].value);
  }
  area.value = arr
}

function insertAfter(newNode, existingNode) {
  existingNode.parentNode.insertBefore(newNode, existingNode.nextSibling);
}

function displaySponsors() {
  let spons_names = document.querySelectorAll(".sponsored_by_name");
  console.log(spons_names);
  let spons_amts = document.querySelectorAll(".spons_amt_individually");
  console.log(spons_amts);
  let textarea = document.querySelector(".spons_text");
  textarea.value = "";
  let value = textarea.value;
  let spon_obj = {};
  for (let i = 0; i < spons_amts.length; i++) {
    let obj = {
      name: spons_names[i].value,
      amt: spons_amts[i].value,
    };
    spon_obj[obj.name] = obj.amt;
  }
  textarea.value = JSON.stringify(spon_obj);
}

function removeChildren(elements) {
  while (elements[0]) {
    elements[0].parentNode.removeChild(elements[0]);
  }
}

function findTotal() {
  let arr = document.querySelectorAll(".spons_amt_individually");
  var tot = 0;
  for (var i = 0; i < arr.length; i++) {
    if (parseInt(arr[i].value)) tot += parseInt(arr[i].value);
  }
  document.getElementById("total").value = tot;
}

$(document).ready(function () {
  $("select").each(function () {
    $(this).select2();
  });

  //disabled future dates
  $(function () {
    if(document.getElementsByClassName('event').length > 0){
        var dtToday = new Date();

        var month = dtToday.getMonth() + 1;
        var day = dtToday.getDate();
        var year = dtToday.getFullYear();

        if (month < 10) month = "0" + month.toString();
        if (day < 10) day = "0" + day.toString();

        var maxDate = year + "-" + month + "-" + day;
        $(".datesettup").attr("max", maxDate);
    }
  });
  // end date set
  $(function () {
    if(document.getElementsByClassName('event').length > 0){
        let fieldvalue = document.querySelector("#end-date-setter").innerHTML;
        // Nov. 19, 2022

        let values = fieldvalue.split(" ");

        let mon = values[0].substring(0, 3);
        let month1 = "JanFebMarAprMayJunJulAugSepOctNovDec".indexOf(mon) / 3 + 1;

        let day_ = values[1].split(",")[0];
        let year_ = values[2];

        if (month1 < 10) month1 = "0" + month1.toString();
        if (day_ < 10) day_ = "0" + day_.toString();

        let datePattern = year_ + "-" + month1 + "-" + day_;
        console.log(datePattern);
        document.getElementById("end_date").value = datePattern;
    }
  });
  // strt date set
  $(function () {
    if(document.getElementsByClassName('event').length > 0){
        let fieldvalue = document.querySelector("#start-date-setter").innerHTML;
        // Nov. 19, 2022

        let values = fieldvalue.split(" ");

        let mon = values[0].substring(0, 3);
        let month1 = "JanFebMarAprMayJunJulAugSepOctNovDec".indexOf(mon) / 3 + 1;

        let day_ = values[1].split(",")[0];
        let year_ = values[2];

        if (month1 < 10) month1 = "0" + month1.toString();
        if (day_ < 10) day_ = "0" + day_.toString();

        let datePattern = year_ + "-" + month1 + "-" + day_;
        console.log(datePattern);

        document.getElementById("start_date").value = datePattern;
    }
  });

  // societyOPtions
  $(function () {
    if(document.getElementsByClassName('event').length > 0){
        let selectedvalues = document
        .querySelector("#all_society")
        .value.split(",");
        let options = document.querySelectorAll("#society > *");
        // console.log(options)

        for (let i = 0; i < options.length; i++) {
        let optionvalue = options[i].value;
        // console.log(optionvalue)
        for (let j = 0; j < selectedvalues.length; j++) {
            let selectedValue = selectedvalues[j];
            // console.log("selected value ====         "+selectedValue)
            if (selectedValue == optionvalue) {
            // console.log("matched")
            // console.log(options[i])
            options[i].setAttribute("selected", "true");
            }
        }
        }
        // this.selectedValues = []
        getSocieties();
    }
    });
 
  //departments option
  $(function () {
    if(document.getElementsByClassName('event').length > 0){
      let selectedValues = document
        .querySelector("#all_department")
        .value.split(",");
      let options = document.querySelectorAll("#department > *");
      // console.log(options)

      for (let i = 0; i < options.length; i++) {
        let optionvalue = options[i].value;
        // console.log(optionvalue)
        for (let j = 0; j < selectedValues.length; j++) {
          let selectedValue = selectedValues[j];
          // console.log("selected value ====         "+selectedValue)
          if (selectedValue == optionvalue) {
            // console.log("matched")
            // console.log(options[i])
            options[i].setAttribute("selected", "true");
            options[i].click();
          }
        }
      }
      getDepartments();
    }
  });

  $(function () {
    if(document.getElementsByClassName('event').length > 0){
        let spondataJSON = document.querySelector("#sponDets").value;
        // console.log(spondataJSON);
        let parentDiv = document.querySelector("#insertSponsDets");
        let sponData = JSON.parse(spondataJSON);
        console.log(sponData);
        let arr = Object.entries(sponData);
        console.log(arr);
        for (let i = 0; i < arr.length; i++) {
            let sponName = arr[i][0];
            let sponAmt = arr[i][1];
            let template = ` <div class="sponsors" >
            <div class="form-group  align-center float-child">
            <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Sponsor Name</label>
            <input type="text" name="sponsored_by" style="height:32px; border-radius: 4px;" class = "w-30 m-1 sponsored_by_name" oninput = "findTotal();displaySponsors()" value = ${sponName} >
            </div>
            <div class="form-group  align-center float-child">  
            <label class=" w-25 spon_amt required_asterisk" style="width:153px;"  for="exampleFormControlInput1">Sponsored Amount</label>
            <input type="number" name="spons_amount" id="" style="height:32px; border-radius: 4px;" class = "w-30 m-1 spons_amt_individually" oninput = "findTotal();displaySponsors()"  value =${sponAmt} required>
            </div>
            <div>`
            let child = document.createElement("div");
            child.innerHTML = template;
            parentDiv.appendChild(child);
        }
    }
  });
});


function getSocieties() {
  $("#all_society").val($("#society").val().toString());
  console.log($("#all_society").val());
}

function getDepartments() {
  let society = $("#department").val().toString();
  if (society.includes("All")) {
    society = "All";
  }
  $("#all_department").val(society);
  console.log($("#all_department").val());
}

function hide_show_table(col_name) {
  var checkbox_val = document.getElementById(col_name).value;
  if (checkbox_val == "hide") {
    var all_col = document.getElementsByClassName(col_name);
    for (var i = 0; i < all_col.length; i++) {
      all_col[i].style.display = "none";
    }
    document.getElementById(col_name + "_head").style.display = "none";
    document.getElementById(col_name).value = "show";
  } else {
    var all_col = document.getElementsByClassName(col_name);
    for (var i = 0; i < all_col.length; i++) {
      all_col[i].style.display = "table-cell";
    }
    document.getElementById(col_name + "_head").style.display = "table-cell";
    document.getElementById(col_name).value = "hide";
  }
  display_col = [];

  $(".display_columns").each(function () {
    if (!$(this).find("input").is(":checked")) {
      // console.log("heloooooo");
      col_id_arr = $(this).find("input").attr("id").split("_");
      col_name = col_id_arr[0];
      for (let i = 1; i < col_id_arr.length - 1; i++) {
        col_name += "_" + col_id_arr[i];
      }
      display_col.push(col_name);
    }
  });
  // console.log(display_col);
  $("#display_columns").val(display_col);
}

function updateAttendanceFileValue() {
  let textarea = document.querySelector("#upload_attendance_area");
  let inputval = document.querySelector("#attendance_div").childNodes[0].value;
  console.log(inputval);
  textarea.value = inputval;
}

function showTable(){
  $("#table-fields").removeClass("d-none");
}

// function deleteRow(id){
//   console.log(document.URL);
//   let url = document.URL.split("/")
//   console.log(url);
//   let newurl = url[0]+'//'+url[2]+'/deleteEvent';
//   console.log(newurl);
//   // let redirectingUrl = url[0]+'//'+url[2]+'/display_columns'
//   // window.location.href = redirectingUrl;
//   // urlobj = '{% url deleteEvent %}'
//   $.ajax({
//     url : newurl,
//     method :"POST",
//     data : { "id" : id},
//     success : function(response){
//       let data = JSON.parse(response)
//       if(data.success ){
//         $("#event_row_id_"+id).addClass('d-none')
//       }
//       console.log(data.success)
//     }
//   })
// }

function submitHiddenForm(id){  
  let columns = document.querySelector("#columns_dets").value;
  // console.log(id);
  // console.log(columns);
  let template = `<input name = "id_details" class = "d-none" value = "${id}"/> <textarea name="passingColumns" class="d-none" id = 'passingColumns'>`+ columns +
    `</textarea>`;
  console.log(template);
  let child = document.createElement("div");
  child.innerHTML = template;
  document.querySelector("#insertForm").appendChild(child)
  $("#columnsDataform").submit();
  // document.querySelector("#columnsDataform").submit()
}

function fillDefaultValues(){
  if($("#min_amount").length > 0 && $("#min_amount").val() == ''){
    $("#min_amount").val('0');
    console.log($("#min_amount").val('0'));
  }

  if($('#max_amount').length> 0 &&  $("#max_amount").val() == ''){
    $("#max_amount").val('1000000000');
    console.log($("#max_amount").val('1000000000'));
  }

  

}


//////////////////////////////// students //////////////////////////////////////////


function addStudentColumns(cols){
  let ncols = parseInt(cols);
  if(ncols >17){
    // alert("Not more than 14 columns are allowed");
    return false;
  }
  let inputColumns = document.querySelector("#insert_student_Fields");
  let template = `
    <div class = "field_student_columns" style = "display: flex; margin-bottom: 20px; width: 78%; align-items: center;  justify-content: center;">
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Field:</label>
      <select class="fill-columns" class="w-30 m-1" oninput="getFields()" onmouseover = "disableFields(this)" style = "height: 30px;border-radius: 4px;">
          <option value="-1">Select Values</option>
          <option value="name">Student Name</option>
          <option value="eroll_no">Enrollment No.</option>
          <option value="semester">Semester</option>
          <option value="Departments">Departments</option>
          <option value="Class">Class</option>
          <option value="organized_by">Organized By</option>
          <option value="mobile_no">Mobile Number</option>
          <option value="mail_id">E-mail Id</option>
          <option value="event_name">Event Name</option>
          <option value="event_type">Type of Event</option>
          <option value="event_date">Event Date</option>
          <option value="host_institute">Host Institute</option>
          <option value="team_size">Team Size</option>
          <option value="level">Level of Competition</option>
          <option value="date_of_award">Award Date</option>
          <option value="upload_proof">Award Proof</option>
      </select>
    </div>    
  `;

  // console.log(ncols)
  removeChildren(document.getElementsByClassName("field_student_columns"));
  for (let i = 0; i < ncols; i++) {
    let child = document.createElement("div");
    child.style = 'display: inline-block;width: 40%; margin-left: 98px;box-sizing: border-box;';
    child.innerHTML = template;
    inputColumns.append(child);
  }
  
}


function triggerAlert(){
  console.log("heiiiii");
//   alert('added successfully')
//   $('#students_table').addClass('alert')
  
}

function restrictLength(val,len){
    let value = parseInt(val);
    if(value>len){
        return false;
    }
}

function phoneno(){          
    $('#phone').keypress(function(e) {
        var a = [];
        var k = e.which;

        for (i = 48; i < 58; i++)
            a.push(i);

        if (!(a.indexOf(k)>=0))
            e.preventDefault();
    });
}

