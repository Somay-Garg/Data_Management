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

function uploadPDF(){
  $("input[type='file']").each(function(){
    $(this).on('change',function(){
      myFile = $(this).val();
        console.log(myFile);
      var upld = myFile.split('.').pop();
      if(upld=='pdf'){
        // alert("File uploaded is pdf")
      }else{
        alert("Only PDF are allowed")
        $(this).val('');
      }

    });
  });
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
      <select class="fill-columns" class="w-30 m-1" oninput="getFields()" onmouseover = "disableFields(this)" style = "height: 30px;border-radius: 4px;">
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
          <option value="upload_attendance">Upload Attendance</option>
          <option value="upload_report">Upload Report</option>
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
  // console.log(spons_names);
  let spons_amts = document.querySelectorAll(".spons_amt_individually");
  // console.log(spons_amts);
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

  // upload pdf only 
    uploadPDF();
  // Report sidebar start
    $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
    });
  // Report sidebar end

    // ---------------Placement code start----------
      // Code for years
  const date = new Date();
  const year = date.getFullYear();
  for (let i = 0; i <= 50; i++) {
    const option = document.createElement('option');
    option.textContent = year - i;
    $('#select_year').append(option);
  }
  for (let i = 1; i <= 100; i++) {
    const option = document.createElement('option');
    option.textContent = year + i;
    $('#select_year').append(option);
  }
  passout_year = parseInt($('#hidden_passout').val());
  if(!isNaN(passout_year)){
    $('#select_year').val(passout_year);
  }

  // Code for countries
  if(document.getElementById('high_edu_country')){
    console.log($('#high_edu_country').val());
    addCountryNames($('#high_edu_country').val());
  }
  if(document.getElementById('entrepre_country')){
    addCountryNames($('#entrepre_country').val());
  }

  $("#message-alert").fadeTo(2000, 500).slideUp(500, function() {
    $("#message-alert").slideUp(500);
  });

  // ---------------Placement code end----------
 
  //Infrastructure onload code starts---------------------------------------------------------------------------------------
  const infradate = new Date();
    const infrayear = infradate.getFullYear();
    for (let i = 0; i <= 50; i++) {
      const option = document.createElement('option');
      option.textContent = infrayear - i;
      $('.backYears').append(option);
    }
    for_year = parseInt($('#hidden_for_yr').val());
    if(!isNaN(for_year)){
      $('#select_for_year').val(for_year);
    }
    estb_year = parseInt($('#hidden_estb_yr').val());
    if(!isNaN(estb_year)){
      $('#select_estb_year').val(estb_year);
    }
    passout_year = parseInt($('#hidden_passout_yr').val());
    if(!isNaN(estb_year)){
      $('#select_passout_year').val(passout_year);
    }
    naac_year = parseInt($('#hidden_NAAC_accr_yr').val());
    if(!isNaN(estb_year)){
      $('#select_NAAC_accr_year').val(naac_year);
    }
    for (let i = 0; i <= 50; i++) {
      const option = document.createElement('option');
      option.textContent = infrayear + i;
      $('.futureYears').append(option);
    }
    aicte_valid_year = parseInt($('#hidden_AICTE_valid_yr').val());
    if(!isNaN(estb_year)){
      $('#select_AICTE_valid_year').val(aicte_valid_year);
    }
    nacc_valid_year = parseInt($('#hidden_NAAC_valid_yr').val());
    if(!isNaN(estb_year)){
      $('#select_NAAC_valid_year').val(nacc_valid_year);
    }
    nba_valid_year = parseInt($('#hidden_NBA_valid_yr').val());
    if(!isNaN(estb_year)){
      $('#select_NBA_valid_year').val(nba_valid_year);
    }
  
  $(function () {
    
      let clubdataJSON = document.querySelector("#clubDets").value;
      let clubData = JSON.parse(clubdataJSON);
      let arr = Object.entries(clubData);
      for (let i = 0; i < arr.length; i++) {
          let clubName = arr[i][0];
          let clubType = arr[i][1];
          let template = `<br>
          <fieldset class="border border-2 p-3 societies" id="">
        <legend class="float-none w-auto">Society - ${i+1} Details</legend>
        <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Name of Society</label>
     <input type="text" name="name_of_society" style="height:32px; border-radius: 4px;" class = "w-30 m-1 society_name" value=${clubName} required oninput="displaySocieties()">
    </div>
    <div class="form-group align-center float-child">
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Type of society</label>
      <select class="w-30 m-1 society_type" required name="type_of_society" class="form-control" oninput="displaySocieties()" >
      <option value="Technical" ${clubType=='Technical'?'selected':''} >Technical</option>
      <option value="Non-Technical" ${clubType=='Non-Technical'?'selected':''} >Non-Technical</option>
      </select>
    </div>
      </fieldset>`;   
        $('#InsertClubsDets').append(template);
      }  
    }
  );

  $(function () {
      let publishdataJSON = document.querySelector("#Publication_Data").value;
      let publishData = JSON.parse(publishdataJSON);
      let arr = Object.entries(publishData);
    for(let i=0;i<arr.length;i++){
      let obj = arr[i][1];
      let objarr = Object.entries(obj);
      let publishName = objarr[0][1];
      let publishType = objarr[1][1];
      let publishfre = objarr[2][1];
      let publishcirc = objarr[3][1];

      let template = ` 
      <br>
      <fieldset class="border border-2 p-3 publishers" id="">
        <legend class="float-none w-auto">Publication - ${i+1} Details</legend>
        <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Name of Publication</label>
     <input type="text" name="published_by" value = ${publishName} style="height:32px; border-radius: 4px;" class = "w-30 m-1 published_by_name"  required>
    </div>
    <div class="form-group align-center float-child" >
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Type of Publication</label>
      <select class="w-30 m-1 type_of_publication"  required name="publication_type" class="form-control">
      <option value="Magazine" ${publishType=='Magazine'?'selected':''}>Magazine</option>
      <option value="Research Journal" ${publishType=='Research Journal'?'selected':''}>Reasearch Journal</option>
      <option value="Newsletter" ${publishType=='Newsletter'?'selected':''}>Newsletter</option>
      </select>
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Frequency of Publication</label>
     <input type="number" name="publication_freq" style="height:32px; border-radius: 4px;" class = "w-30 m-1 freq_of_publication" value = ${publishfre}  required>
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Circulation figure of Publication</label>
     <input type="number" name="circulation_fig_of_pub" style="height:32px; border-radius: 4px;" class = "w-30 m-1 publication_circulation" required  value = ${publishcirc}  >
    </div>
      </fieldset>
    `;
    $('#InsertPublishDets').append(template);
      
    }
  } 
  );
  
  $(function (){
    console.log(document.getElementById('foreign_tieup').value)
    if(document.getElementById('foreign_tieup').value == "Yes"){
      document.getElementById('ifYes').style.display="block";
    }else{
      document.getElementById('ifYes').style.display="none";}
  });
 
  

  $(function () {
      
        let tieupdataJSON = document.querySelector("#Tieup_Data").value;
        let tieupData = JSON.parse(tieupdataJSON);
        let arr = Object.entries(tieupData);
        for (let i = 0; i < arr.length; i++) {
          let obj = arr[i][1];
          let objarr = Object.entries(obj);
          let name = objarr[0][1];
          let address = objarr[1][1];
          let phone = objarr[2][1];
          let email = objarr[3][1];
          let type = objarr[4][1];
          let proof = objarr[5][1];
          let stu_ex = objarr[6][1];
          let stu_parti = objarr[7][1];

            let template = `<br>
            <fieldset class="border border-2 p-3 tieup_fields" id="">
              <legend class="float-none w-auto">Tie-Up University - ${i+1} Details</legend>
              <div class="form-group  align-center float-child">
           <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Name of University</label>
           <input type="text" name="tieup_name" style="height:32px; border-radius: 4px;" class = "w-30 m-1 tieup_uni_name"  required  value = ${name}>
          </div>
          <div class="form-group  align-center float-child">
           <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Address of University</label>
           <input type="text" name="tieup_address" style="height:32px; border-radius: 4px;" class = "w-30 m-1 tieup_uni_address"  required value = ${address}>
          </div>
          <div class="form-group  align-center float-child">
           <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Phone no. of University</label>
           <input type="tel" pattern="^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s./0-9]*$" name="tieup_phone" style="height:32px; border-radius: 4px;"   required value = ${phone} class = "w-30 m-1 tieup_uni_phone">
          </div>
          <div class="form-group  align-center float-child">
           <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Email of University</label>
           <input type="email" name="tieup_email"   value = ${email} required style="height:32px; border-radius: 4px;" class = "w-30 m-1 tieup_uni_email">
          </div>
          <div class="form-group align-center float-child" >
            <label class="w-25 required_asterisk" for="exampleFormControlInput1">Type of MoU</label>
            <select class="w-30 m-1 type_of_mou"   required name="MoU_type" class="form-control ">
              <option value="Student Exchange" ${type=='Student Exchange'?'selected':''}>Student Exchange</option>
              <option value="Faculty Exchange" ${type=='Faculty Exchange'?'selected':''}>Faculty Exchange</option>
            </select>
          </div>
          <div class="form-group align-center float-child" style="height: 6rem;" >
              <label for="exampleFormControlFile1" class="d-grid w-25 required_asterisk" style="margin-left: 4.2rem;">Proof of MoU <sub  style="width:max-content;" ><strong>(Max Size 5mb)</strong></sub></label>
              <div id = "attendance_div" style="margin-left:3rem">
                <div style="display: flex;align-items: center;justify-content: inherit;">
                <label for="">Previously Uploaded:</label>
                <label class="prev_mou_proof" for="">${proof}</label>
                </div>
                <div style="display: flex;align-items: center;justify-content: inherit;"> 
                <label for="">Change File</label>
                <input class="w-30 m-1 tieup_MoU_proof"  type="file" style="margin" accept ="application/pdf" name= "proof_mou"   class="form-control-file" id="exampleFormControlFile1" >
                </div>                                    
              </div>
            </div>
          <div class="form-group  align-center float-child">
           <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">No. of student foreign exchange prog. in prev. A.Y.</label>
           <input type="number" name="student_no_in_foreign_exchange" required style="height:32px; border-radius: 4px;" value = ${stu_ex}  class = "w-30 m-1 tieup_student_foreign_exchange">
          </div>
          <div class="form-group  align-center float-child">
           <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">% of student in foreign exchange prog. in prev. A.Y.</label>
           <input type="number" name="student_no_participated_in_foreign_exchange"  required style="height:32px; border-radius: 4px;" value = ${stu_parti}  class = "w-30 m-1 tieup_student_participated_foreign_exchange"  >
          </div>
            </fieldset>
          `;
          $('#InsertTieupDets').append(template);     
      } 
    });


  

//Infrastructure onload code ends----------------------------------------------------------------------------------------------------

  //disabled future dates
  $(function () {
    var dtToday = new Date();
      var month = dtToday.getMonth() + 1;
      var day = dtToday.getDate();
      var year = dtToday.getFullYear();
      if (month < 10) month = "0" + month.toString();
      if (day < 10) day = "0" + day.toString();
      var maxDate = year + "-" + month + "-" + day;
      $(".datesettup").each(function(){
        // console.log("mansiiii");
        $(this).attr("max", maxDate);
      });
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
  // start date set
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
     

      for (let i = 0; i < options.length; i++) {
        let optionvalue = options[i].value;
        for (let j = 0; j < selectedValues.length; j++) {
          let selectedValue = selectedValues[j];
          if (selectedValue == optionvalue) {
           
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
      let parentDiv = document.querySelector("#insertSponsDets");
      let sponData = JSON.parse(spondataJSON);
      console.log(sponData);
      let arr = Object.entries(sponData);
      // console.log(arr);
      for (let i = 0; i < arr.length; i++){
        let sponName = arr[i][0];
        let sponAmt = arr[i][1];
        let template = `<div class="sponsors" >
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

      uploadPDF();
    }
  });

});



function loadFileIcon() {
  let attendanceLinks = document.querySelectorAll(".atten_file");
  let reportLinks = document.querySelectorAll(".report_file");
  console.log(attendanceLinks);
  for (let i = 0; i < attendanceLinks.length; i++) {
    let href1 = attendanceLinks[i].getAttribute("href");
    let href2 = reportLinks[i].getAttribute("href");
    let ext = href1.split(".")[1];
    let ext2 = href2.split(".")[1];
    console.log(ext);
    if (ext == "pdf") {
      let icontemplate = `<i class="fas fa-file-pdf" style = "font-size:2rem; color: red;"></i>`;
      attendanceLinks[i].appendChild(icontemplate);
    } else if (ext == "csv" || ext == "xls" || ext == "docx") {
      let icontemplate = `<i class="fa-solid fa-file-csv" style = "font-size:2rem; color: green;"></i>`;
      attendanceLinks[i].appendChild(icontemplate);
    }

    if (ext2 == "pdf") {
      let icontemplate = `<i class="fas fa-file-pdf" style = "font-size:2rem; color: red;"></i>`;
      reportLinks[i].appendChild(icontemplate);
    } else if (ext2 == "csv" || ext2 == "xls") {
      let icontemplate = `<i class="fa-solid fa-file-csv" style = "font-size:2rem; color: green;"></i>`;
      reportLinks[i].appendChild(icontemplate);
    }
  }
}

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
//   let redirectingUrl = url[0]+'//'+url[2]+'/display_columns'
//   window.location.href = redirectingUrl;
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
  
  let template = `<input name = "id_details" class = "d-none" value = "${id}"/> <textarea name="passingColumns" class="d-none" id = 'passingColumns'>`+ columns +
    `</textarea>`;
  console.log(template);
  let child = document.createElement("div");
  child.innerHTML = template;
  document.querySelector("#insertForm").appendChild(child)
  $("#columnsDataform").submit();
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


// ----------------------Report JS Code Start -------------------------

var id = '';

function edit_content(ele){
  let text = ele.innerHTML;
  $('.modal-bg').removeClass('d-none');
  $('.edit-modal').removeClass('d-none');
  $('.modal-text').val(text);
  id = "id" + Math.random().toString(16).slice(2);
  ele.classList.add(id);
}

function close_modal(){
  $('.modal-bg').addClass('d-none');
  $('.edit-modal').addClass('d-none');
  $('.'+id).removeClass(id);
}

function save_modal_text(){
  let new_text = $('.modal-text').val();
  $('.'+id).html(new_text);
  $('.'+id).removeClass(id);
  $('.modal-bg').addClass('d-none');
  $('.edit-modal').addClass('d-none');
}

function clear_sec_text(){
  $('.modal-text').val('');
}

async function preview_report(){	

  const downloadPDF = (elements, options) => {
    let worker = html2pdf()
      .set(options)
      .from(elements[0])

    if (elements.length > 1) {
      worker = worker.toPdf() // worker is now a jsPDF instance

      // add each element/page individually to the PDF render process
      elements.slice(1).forEach((element, index) => {
        worker = worker
          .get('pdf')
          .then(pdf => {
            pdf.addPage()
          })
          .from(element)
          .toContainer()
          .toCanvas()
          .toPdf()
      })
    }

    worker = worker.save()
  }

  const pages = Array.from(document.querySelectorAll('div[aria-label^="pdf-page-"]'));
  const pdfOptions = {     
        filename: 'report.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { dpi: 96, letterRendering: true },
        margin: [0.46,0.23,0.46,0.23],//[0.23,0.23,0.23,0.23],
        jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' },
        pagebreak: { mode: 'avoid-all', after: '#page-break' } 
      };
  await downloadPDF(pages, pdfOptions)

}

//------------------------- Report JS Code End ---------------


// ------------------------students js code begins----------------------------
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

function numberOfMembers(val){
  if(val == 'Team'){
    $("#no_of_members").removeClass("d-none");
  }else{
    $("#no_of_members").addClass("d-none");
    $('#noofmembers').val("1");
  }
}

function AddInstituteName(val){
  if(val == 'MSIT'){
    $("#conducted_by").val("MSIT");
    $("#conductedBlock").addClass("d-none");
  }else{
    $("#conductedBlock").removeClass("d-none"); 
  }
}


function showFilters(){
  $("#filterDataDiv").toggleClass('d-none');
  $(".show_filter_data").each(function(e){
    $(this).val('True');
  });
}



// --------------------------students js code ends------------------------------

// --------------------------Placement JS Code Start----------------------------
function addPlacementColumns(cols){
  let ncols = parseInt(cols);
  if(ncols > 6){
    // alert("Not more than 14 columns are allowed");
    return false;
  }
  let inputColumns = document.querySelector("#insert_placement_Fields");
  let template = `
    <div class = "field_placement_columns" style = "display: flex; margin-bottom: 20px; width: 78%; align-items: center;  justify-content: center;">
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Field:</label>
      <select class="fill-columns" class="w-30 m-1" oninput="getFields()" onmouseover = "disableFields(this)" style = "height: 30px;border-radius: 4px;">
          <option value="-1">Select Values</option>
          <option value="name">Student Name</option>
          <option value="enrollmentno">Enrollment Number</option>
          <option value="department">Department Name</option>
          <option value="section">Section</option>
          <option value="passout">Passout Year</option>
          <option value="current_status">Current Status</option>
      </select>
    </div>    
  `;

  // console.log(ncols)
  removeChildren(document.getElementsByClassName("field_placement_columns"));
  for (let i = 0; i < ncols; i++) {
    let child = document.createElement("div");
    child.style = 'display: inline-block;width: 40%; margin-left: 98px;box-sizing: border-box;';
    child.innerHTML = template;
    inputColumns.append(child);
  }
  $("select").each(function () {
    $(this).select2();
  });
}

function showPlacedForm(is_placed){
  if(is_placed == "yes"){
    let offer_div = `
      <div class="form-group align-center float-child">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Number of Offers</label>
          <input class="w-30 " type="number" name="no_of_offers" id="no_of_offers" required style = "height: 32px;
          border-radius: 4px;" oninput="offerDetails(this.value)">
      </div>
    `;
    $('.placed_form').prepend(offer_div);
  }else{
    $('.placed_form').html('');
    $('.offer_details').html('');
  }
}

function offerDetails(noOfOffers){
  $('.offer_details').html('');
  noOfOffers = parseInt(noOfOffers)
  if(isNaN(noOfOffers)){
    return;
  }
  let offers = parseInt($('.existing_no_of_offers').val());
  if(isNaN(offers)){
    offers=0;
  }
  let i = offers;
  for(;i<noOfOffers+offers;i++){
    let offer = `
    <br>
      <fieldset class="border border-2 p-3 offer_detail" id="if_placed">
        <legend class="float-none w-auto">Offer - ${i+1} Details</legend>
        <div class="form-group  align-center float-child">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Company Name</label>
          <input class="w-30 company_name" type="text" name="company_name" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group  align-center float-child">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Package in LPA</label>
          <input class="w-30 package" type="number" name="package" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child" id="">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">On/Off Campus</label>
          <select class="m-1 w-30 on_off_campus" id="">
            <option value="on-campus">On-Campus</option>
            <option value="off-campus">Off-Campus</option>
          </select>
        </div>
        <div class="form-group align-center float-child">
          <label class="w-25 d-grid required_asterisk" for="exampleFormControlFile1">Upload Proof <sub style="width:max-content;" ><strong>(Max Size 5mb)</strong></sub></label>
          <input class="w-30 m-1 upload_proof" type="file" name="upload_proof" class="form-control-file" id="exampleFormControlFile1" accept ="application/pdf" style = "height: 32px;border-radius: 4px;">
        </div>
      </fieldset>
    `;
    $('.offer_details').append(offer);
  }
  uploadPDF();
  $("select").each(function () {
    $(this).select2();
  });
}

function showExamForm(has_appeared){
  if(has_appeared == "yes"){
    let exam_div = `
      <div class="form-group align-center float-child">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Number of Exams Appeared in</label>
          <input class="w-30 " type="number" name="no_of_exams" id="no_of_exams" required style = "height: 32px;
          border-radius: 4px;" oninput="examDetails(this.value)">
      </div>
    `;
    $('.exam_form').prepend(exam_div);
  }else{
    $('.exam_form').html('');
    $('.exam_details').html('');
  }
}

function examDetails(noOfExams){
  $('.exam_details').html('');
  noOfExams = parseInt(noOfExams);
  if(isNaN(noOfExams)){
    return;
  }
  let exams = parseInt($('.existing_no_of_exams').val());
  if(isNaN(exams)){
    exams=0;
  }
  let i = exams;
  for(;i<noOfExams+exams;i++){
    let unique_id = Math.random().toString(16).slice(2);
    let offer = `<br>
      <fieldset class="border border-2 p-3 exam_detail" id="">
        <legend class="float-none w-auto">Exam - ${i+1} Details</legend>
        <div class="form-group  align-center float-child">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Exam Name</label>
          <input class="w-30 exam_name" type="text" name="exam_name" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Exam Roll Number</label>
          <input class="w-30 exam_roll_no" type="number" name="exam_roll_no" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Date of Exam</label>
          <input class="w-30 exam_date" type="date" name="exam_date" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child" id="">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Qualified?</label>
          <select class="m-1 w-30 qualified" onchange="examResultDeclared(this.id)">
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
        </div>
        <div class="form-group align-center float-child ">
          <label class="w-25 " for="exampleFormControlInput1">Exam Score</label>
          <input class="w-30 exam_score" type="number" name="exam_score" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child ">
          <label class="w-25 " for="exampleFormControlInput1">Exam Rank</label>
          <input class="w-30 exam_rank" type="number" name="exam_rank" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child ">
          <label class="w-25 " for="exampleFormControlInput1">Date of Result</label>
          <input class="w-30 date_of_result" type="date" name="date_of_result" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child ">
          <label class="w-25 d-grid " for="exampleFormControlFile1">Result Proof <sub style="width:max-content;" ><strong>(Max Size 5mb)</strong></sub></label>
          <input class="w-30 m-1 result_proof" type="file" name="result_proof" class="form-control-file" id="exampleFormControlFile1" accept ="application/pdf" style = "height: 32px;border-radius: 4px;">
        </div>
      </fieldset>
    `;
    $('.exam_details').append(offer);
  }
  uploadPDF();
  $("select").each(function () {
    $(this).select2();
  });
}

function examResultDeclared(ele_id){
  if($('#'+ele_id).val() != 'not_declared'){
    // console.log($('#'+ele_id).val());
    $('.'+ele_id).each(function(){
      if(!$(this).hasClass('dont_show')){
        $(this).removeClass('d-none');
        $(this).find('input').val('');
      }
    })
  }
  else{
    $('.'+ele_id).each(function(){
      if(!$(this).hasClass('d-none')){
        $(this).addClass('d-none');
        $(this).find('input').val('');
      }
    })
  }
}

function showStatusForm(status){
  let status_details = ``;
  // console.log(status);
  if(status == "Job"){
    status_details = `
      <div class="form-group  align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Company Name</label>
        <input class="w-30 " type="text" name="job_company_name" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Date of Joining</label>
        <input class="w-30 " type="date" name="joining_date" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group  align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Company Address</label>
        <input class="w-30 " type="text" name="company_address" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group align-center float-child">
        <label class="w-25 required_asterisk d-grid" for="exampleFormControlFile1">Upload Proof(LOJ OR I-Card) <sub style="width:max-content;" ><strong>(Max Size 5mb)</strong></sub></label>
        <input class="w-30 m-1" type="file" name="job_joining_proof" class="form-control-file" id="exampleFormControlFile1" accept ="application/pdf" style = "height: 32px;border-radius: 4px;">
      </div>
    `;
  }else if(status == "Higher Education"){
    var countryData = $.fn.countrySelect.getCountryData();
    let countrySelectData = ``;
    for(let i=0;i<countryData.length;i++){
      countrySelectData += `<option value="`+countryData[i]['name']+`">`+countryData[i]['name']+`</option>`;
    }
    status_details = `
      <div class="form-group  align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">College Name</label>
        <input class="w-30 " type="text" name="college_name" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">College Address</label>
        <input class="w-30 " type="text" name="college_address" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group  align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Country</label>
        <select class="m-1 w-30 country" name="country">
        </select>
      </div>
      <div class="form-group align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Course Name</label>
        <input class="w-30 " type="text" name="course_name" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group align-center float-child">
        <label class="w-25 d-grid required_asterisk" for="exampleFormControlFile1">Upload Proof(I-Card) <sub style="width:max-content;" ><strong>(Max Size 5mb)</strong></sub></label>
        <input class="w-30 m-1" type="file" name="college_joining_proof" class="form-control-file" id="exampleFormControlFile1" accept ="application/pdf" style = "height: 32px;border-radius: 4px;">
      </div>
    `;
  }else if(status == "Entreprenurship"){
    var countryData = $.fn.countrySelect.getCountryData();
    let countrySelectData = ``;
    for(let i=0;i<countryData.length;i++){
      countrySelectData += `<option value="`+countryData[i]['name']+`">`+countryData[i]['name']+`</option>`;
    }
    status_details = `
      <div class="form-group  align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Startup Name</label>
        <input class="w-30 " type="text" name="startup_name" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group  align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Company Address</label>
        <input class="w-30 " type="text" name="startup_company_address" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Country</label>
        <select class="m-1 w-30 country" name="startup_country">
        </select>
      </div>
      <div class="form-group  align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Working Sector</label>
        <input class="w-30 " type="text" name="working_Sector" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
      <div class="form-group  align-center float-child">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Website Link</label>
        <input class="w-30 " type="text" name="website_link" id="" required style = "height: 32px;
        border-radius: 4px;">
      </div>
    `;
  }else{
    status_details = `
      <div class="form-group align-center float-child" id="">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Others</label>
        <select class="m-1 w-30" name="other">
          <option value="Entrance Exam">Preparing for Entrance Exam</option>
          <option value="Family Business">Family Business</option>
          <option value="Unknown">Unknown</option>
        </select>
      </div>
    `;
  }
  $('.status_details').html(status_details);
  uploadPDF();
  $("select").each(function () {
    $(this).select2();
  });
  var countryData = $.fn.countrySelect.getCountryData();
  for(let i=0;i<countryData.length;i++){
    console.log(countryData[i]['name'])
  }
  addCountryNames('');
}

function submitPlacementData(){
  let is_placed = $('#is_placed').val();
  if(is_placed=='yes'){
    let offers = parseInt($('#no_of_offers').val());
    if(isNaN(offers) || offers==0 || offers < 0){
      alert('Please add offer details');
    }else{
      let offer_details = {};
      let i = 1;
      $('.offer_detail').each(function(){
        let current_offer = {
          'company_name' : '',
          'package' : '',
          'on_off_campus' : '',
        }
        current_offer['company_name'] = $(this).find('.company_name').val();
        current_offer['package'] = $(this).find('.package').val();
        current_offer['on_off_campus'] = $(this).find('.on_off_campus').val();
        offer_details[i] = current_offer;
        $(this).find('.upload_proof').attr('name','upload_proof_'+i);
        i++;
      });
      $('#student_offer_data').val(JSON.stringify(offer_details));
    }
  }

  let has_appeared = $('#has_appeared').val();
  if(has_appeared == 'yes'){
    let exams = parseInt($('#no_of_exams').val());
    if(isNaN(exams) || exams==0 || exams < 0){
      alert('Please add exam details');
    }else{
      let exam_details = {};
      let i = 1;
      $('.exam_detail').each(function(){
        let current_exam = {
          'exam_name' : '',
          'exam_roll_no' : '',
          'exam_date' : '',
          'qualified' : '',
          'exam_score' : '',
          'exam_rank' : '',
          'date_of_result' : '',
        }
        current_exam['exam_name'] = $(this).find('.exam_name').val();
        current_exam['exam_roll_no'] = $(this).find('.exam_roll_no').val();
        current_exam['exam_date'] = $(this).find('.exam_date').val();
        current_exam['qualified'] = $(this).find('.qualified').val();
//         if(current_exam['qualified'] != 'not_declared'){
          current_exam['exam_score'] = $(this).find('.exam_score').val();
          current_exam['exam_rank'] = $(this).find('.exam_rank').val();
          current_exam['date_of_result'] = $(this).find('.date_of_result').val();
          exam_details[i] = current_exam;
          $(this).find('.result_proof').attr('name','result_proof_'+i);
//         }else{
//           exam_details[i] = current_exam;
//         }
        i++;
      });
      $('#student_exam_data').val(JSON.stringify(exam_details));
    }
  }

  $('#placement_detail_form').submit();
}
function removeOffer(id){
  $('.'+id).remove();
  if($('#removed_offer_data').val() != ''){
    $('#removed_offer_data').val($('#removed_offer_data').val()+','+id.split('_')[2]);
  }else{
    $('#removed_offer_data').val(id.split('_')[2]);
  }
}
function removeExam(id){
  $('.'+id).remove();
  if($('#removed_exam_data').val() != ''){
    $('#removed_exam_data').val($('#removed_exam_data').val()+','+id.split('_')[2]);
  }else{
    $('#removed_exam_data').val(id.split('_')[2]);
  }
}
function saveNewPlacementData(){
  // For existing offers
  let existing_offer = {};
  let i = 1;
  $('.existing_offers').each(function(){
      let offer = {
        'offer_id' : $(this).find('.existing_offer_detail').val(),
        'company_name' : '',
        'package' : '',
        'on_off_campus' : '',
      }
      offer['company_name'] = $(this).find('.company_name').val();
      offer['package'] = $(this).find('.package').val();
      offer['on_off_campus'] = $(this).find('.on_off_campus').val();
      existing_offer[i] = offer;
      $(this).find('.upload_proof').attr('name','upload_proof_'+i);
      i++;
  });
  $('#existing_offer_data').val(JSON.stringify(existing_offer));
  // console.log($('#existing_offer_data').val());

  // For new Offers
  let offers = parseInt($('#no_of_offers').val());
  if(!isNaN(offers) && offers!=0 && offers > 0){
    let offer_details = {};
    $('.offer_detail').each(function(){
      let current_offer = {
        'company_name' : '',
        'package' : '',
        'on_off_campus' : '',
      }
      current_offer['company_name'] = $(this).find('.company_name').val();
      current_offer['package'] = $(this).find('.package').val();
      current_offer['on_off_campus'] = $(this).find('.on_off_campus').val();
      offer_details[i] = current_offer;
      $(this).find('.upload_proof').attr('name','upload_proof_'+i);
      i++;
    });
    $('#student_offer_data').val(JSON.stringify(offer_details));
    // console.log($('#student_offer_data').val());
  }
  

  // For existing exams
  let existing_exam = {};
  i = 1;
  $('.existing_exams').each(function(){
    let exam = {
      'exam_id' : $(this).find('.existing_exam_detail').val(),
      'exam_name' : '',
      'exam_roll_no' : '',
      'exam_date' : '',
      'qualified' : '',
      'exam_score' : '',
      'exam_rank' : '',
      'date_of_result' : '',
    }
    exam['exam_name'] = $(this).find('.exam_name').val();
    exam['exam_roll_no'] = $(this).find('.exam_roll_no').val();
    exam['exam_date'] = $(this).find('.exam_date').val();
    exam['qualified'] = $(this).find('.qualified').val();
//     if(exam['qualified'] != 'not_declared'){
      exam['exam_score'] = $(this).find('.exam_score').val();
      exam['exam_rank'] = $(this).find('.exam_rank').val();
      exam['date_of_result'] = $(this).find('.date_of_result').val();
      existing_exam[i] = exam;
      $(this).find('.result_proof').attr('name','result_proof_'+i);
//     }else{
//       existing_exam[i] = exam;
//     }
    i++;
  });
  $('#existing_exam_data').val(JSON.stringify(existing_exam));
  // console.log($('#existing_exam_data').val());

  // For New Exams
  let exams = parseInt($('#no_of_exams').val());
  if(!isNaN(exams) && exams!=0 && exams > 0){
    let exam_details = {};
    $('.exam_detail').each(function(){
      let current_exam = {
        'exam_name' : '',
        'exam_roll_no' : '',
        'exam_date' : '',
        'qualified' : '',
        'exam_score' : '',
        'exam_rank' : '',
        'date_of_result' : '',
      }
      current_exam['exam_name'] = $(this).find('.exam_name').val();
      current_exam['exam_roll_no'] = $(this).find('.exam_roll_no').val();
      current_exam['exam_date'] = $(this).find('.exam_date').val();
      current_exam['qualified'] = $(this).find('.qualified').val();
//       if(current_exam['qualified'] != 'not_declared'){
        current_exam['exam_score'] = $(this).find('.exam_score').val();
        current_exam['exam_rank'] = $(this).find('.exam_rank').val();
        current_exam['date_of_result'] = $(this).find('.date_of_result').val();
        exam_details[i] = current_exam;
        $(this).find('.result_proof').attr('name','result_proof_'+i);
//       }else{
//         exam_details[i] = current_exam;
//       }
      i++;
    });
    $('#student_exam_data').val(JSON.stringify(exam_details));
    // console.log($('#student_exam_data').val());
  }
  $('#placement_detail_editform').submit();
}
function addCountryNames(country){
  var countryData = $.fn.countrySelect.getCountryData();
  let countrySelectData = ``;
  for(let i=0;i<countryData.length;i++){
    if(country == countryData[i]['name']){
      countrySelectData += `<option value="`+countryData[i]['name']+`" selected>`+countryData[i]['name']+`</option>`;
    }else{
      countrySelectData += `<option value="`+countryData[i]['name']+`">`+countryData[i]['name']+`</option>`;
    }
  }
  $('.country').each(function(){
    $(this).html(countrySelectData);
  });
  

}
// --------------------------Placement JS Code End------------------------------

// Infrastructure Code starts--------------------------------------------------------------------------------

function addPublishers(spon){
  $('#insertPublishDets').html('');
  $('#InsertPublishDets').html('');
   let nspon = parseInt(spon);
  if(isNaN(nspon)){
    return;
  }
  
  for(let i=0;i<nspon;i++){
    let template = `<br>
      <fieldset class="border border-2 p-3 publishers" id="">
        <legend class="float-none w-auto">Publication - ${i+1} Details</legend>
        <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Name of Publication</label>
     <input type="text" name="published_by" style="height:32px; border-radius: 4px;" class = "w-30 m-1 published_by_name" required>
    </div>
    <div class="form-group align-center float-child" >
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Type of Publication</label>
      <select class="w-30 m-1 type_of_publication" required name="publication_type" class="form-control">
      <option value="-1">--Select--</option>
      <option value="Magazine">Magazine</option>
      <option value="Research Journal">Reasearch Journal</option>
      <option value="Newsletter">Newsletter</option>
      </select>
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Frequency of Publication</label>
     <input type="number" name="publication_freq" style="height:32px; border-radius: 4px;" class = "w-30 m-1 freq_of_publication" required>
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Circulation figure of Publication</label>
     <input type="number" name="circulation_fig_of_pub" style="height:32px; border-radius: 4px;" class = "w-30 m-1 publication_circulation" required  >
    </div>
      </fieldset>
    `;
    $('#insertPublishDets').append(template);
    $('#InsertPublishDets').append(template);
  }
}

function addTieups(tieup){
  $('#insertTieupDets').html('');
  $('#InsertTieupDets').html('');
   let ntieup = parseInt(tieup);
  if(isNaN(ntieup)){
    return;
  }
  
  for(let i=0;i<ntieup;i++){
    let template = `<br>
      <fieldset class="border border-2 p-3 tieup_fields" id="">
        <legend class="float-none w-auto">Tie-Up University - ${i+1} Details</legend>
        <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Name of University</label>
     <input type="text" name="tieup_name" style="height:32px; border-radius: 4px;" class = "w-30 m-1 tieup_uni_name" required>
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Address of University</label>
     <input type="text" name="tieup_address" style="height:32px; border-radius: 4px;" class = "w-30 m-1 tieup_uni_address" required>
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Phone no. of University</label>
     <input type="tel" pattern="^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s./0-9]*$" name="tieup_phone" style="height:32px; border-radius: 4px;" required class = "w-30 m-1 tieup_uni_phone">
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Email of University</label>
     <input type="email" name="tieup_email" required style="height:32px; border-radius: 4px;" class = "w-30 m-1 tieup_uni_email">
    </div>
    <div class="form-group align-center float-child" >
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Type of MoU</label>
      <select class="w-30 m-1 type_of_mou" required name="MoU_type" class="form-control ">
        <option value="-1">--Select--</option>
        <option value="Student Exchange">Student Exchange</option>
        <option value="Faculty Exchange">Faculty Exchange</option>
      </select>
    </div>
    <div class="form-group align-center  float-child">
      <label class="w-25 required_asterisk d-grid" for="exampleFormControlFile1">Proof of MoU</label>
      <input class="w-30 m-1  tieup_MoU_proof" type="file" name="proof_mou" class="form-control-file" id="exampleFormControlFile1" required accept ="application/pdf" style = "height: 32px; border-radius: 4px;">
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">No. of student foreign exchange prog. in prev. A.Y.</label>
     <input type="number" name="student_no_in_foreign_exchange" required style="height:32px; border-radius: 4px;" class = "w-30 m-1 tieup_student_foreign_exchange">
    </div>
    <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">% of student in foreign exchange prog. in prev. A.Y.</label>
     <input type="number" name="student_no_participated_in_foreign_exchange" required style="height:32px; border-radius: 4px;" class = "w-30 m-1 tieup_student_participated_foreign_exchange"  >
    </div>
    <div class=mou_no>
     <div class=mou_details>

     </div>
    </div>
      </fieldset>
    `;
    $('#insertTieupDets').append(template);
    $('#InsertTieupDets').append(template);
  }
}

function addSocieties(club){
  $('#insertClubsDets').html('');
  $('#InsertClubsDets').html('');
  console.log(club)
   const nclubs = parseInt(club);
  if(isNaN(nclubs)){
    console.log(club)
    console.log(nclubs)
    console.log('hello')
    return;
  }
  
  for(let i=0;i<nclubs;i++){
    console.log(i);
    let template = `<br>
      <fieldset class="border border-2 p-3 societies" id="">
        <legend class="float-none w-auto">Society - ${i+1} Details</legend>
        <div class="form-group  align-center float-child">
     <label class=" w-25 required_asterisk" style="width:153px;" for="exampleFormControlInput1">Name of Society</label>
     <input type="text" name="name_of_society" style="height:32px; border-radius: 4px;" class = "w-30 m-1 society_name" required>
    </div>
    <div class="form-group align-center float-child">
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Type of society</label>
      <select class="w-30 m-1 society_type" required name="type_of_society" class="form-control" oninput="displaySocieties()" >
      <option value="-1">--Select--</option>
      <option value="Technical" >Technical</option>
      <option value="Non-Technical" >Non-Technical</option>
      </select>
    </div>
      </fieldset>
    `;
    $('#insertClubsDets').append(template);
    $('#InsertClubsDets').append(template);
  }
}

function addInfraColumns(cols) {
  let ncols = parseInt(cols);
  if(ncols >110){
    // alert("Not more than 14 columns are allowed");
    return false;
  }
  let inputColumns = document.querySelector("#insert_infra_Fields");
  let template = `
    <div class = "field_infra_columns" style = "display: flex; margin-bottom: 20px; width: 78%; align-items: center;  justify-content: center;">
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Field:</label>
      <select class="fill-columns" class="w-30 m-1" oninput="getFields()" onmouseover = "disableFields(this)" style = "height: 30px;border-radius: 4px;">
          <option value="-1">Select Values</option>
          <option value="for_year_infra_entry">In Year</option>
          <option value="name_of_the_institute">Institute Name</option>
          <option value="institute_category">Institute Category </option>
          <option value="name_of_affiliating_university">Affiliated University name</option>
          <option value="institution_status">Institution Status</option>
          <option value="institute_type">Type of Institute</option>
          <option value="year_of_establishment">Establishment Year</option>
          <option value="year_of_1st_passout_batch">1st passout batch year</option>
          <option value="address">Address</option>
          <option value="city">City</option>
          <option value="state">State</option>
          <option value="pincode">Pincode</option>
          <option value="campus_area">Campus Area</option>
          <option value="total_built_up_area_in_sqmtr">Total built area (sq mt.)</option>
          <option value="total_built_up_area_in_sqft">Total built area (sq ft.)</option>
          <option value="total_playground_area">Total playground area</option>
          <option value="phone">Phone No.</option>
          <option value="email">Email</option>
          <option value="website">Website</option>
          <option value="head_of_the_institute">Head of Institute</option>
          <option value="name_of_the_head_of_institution">Name of Head</option>
          <option value="available_courses">Courses Available</option>
          <option value="no_of_voluntary_programs_supported">No. of voluntrary programs supported</option>
          <option value="AICTE_approved">AICTE Approved</option>
          <option value="year_of_first_AICTE_accreditation">1st AICTE Accr. Yr</option>
          <option value="AICTE_valid_upto">AICTE valid upto</option>
          <option value="NAAC_accredited">NAAC Accredited</option>
          <option value="year_of_first_NAAC_accreditation">1st NAAC Accr. Yr</option>
          <option value="latest_NAAC_grade">Latest NAAC Grade</option>
          <option value="latest_NAAC_score">Latest NAAC Score</option>
          <option value="NAAC_accreditation_valid_upto">NAAC valid upto</option>
          <option value="date_of_last_submitted_AQAR_report">Last Submitted AQAR</option>
          <option value="ABET_accredited">ABET Accredited</option>
          <option value="NBA_accredited_courses">NBA Accredited Courses</option>
          <option value="NBA_accreditation_valid_upto">NBA Accreditation valid upto</option>
          <option value="proof_UGC_recognition">Proof UGC recognition</option>
          <option value="proof_yr_of_estb_of_college">College estb year proof</option>
          <option value="latest_AICTE_renewed_approval_certificate">Latest AICTE renewed approval certificate</option>
          <option value="NBA_accreditation_certificate">NBA Accreditation certificate</option>
          <option value="NAAC_accreditation_certificate">NAAC Accreditation certificate</option>
          <option value="latest_AQAR_submitted_to_NAAC">Latest AQAR submitted to NAAC</option>
          <option value="list_of_governing_body_members">List of governing body members</option>
          <option value="list_of_academic_advisory_body">List of academic advisory body members</option>
          <option value="list_of_members_in_anti_ragging_committee">List of anti-ragging committee</option>
          <option value="list_of_members_in_internal_complaint_committee">List of members in internal complain committee</option>
          <option value="list_of_members_in_grievance_redressal_committee">List of members in grievance redressal committee</option>
          <option value="list_of_members_in_disciplane_committee">List of members in disciplane committee</option>
          <option value="list_of_members_in_ST_SC_cell">List of members in ST/SC cell</option>
          <option value="list_of_members_in_disaster_management_cell">List of members in diasater management cell</option>
          <option value="list_of_members_in_NSS">List of members in NSS cell</option>
          <option value="number_of_classrooms">No. of classrooms</option>
          <option value="number_of_seminar_halls">No. of seminar halls</option>
          <option value="no_of_classrooms_with_audio_visual_facility">Classrooms with A-V facility</option>
          <option value="no_of_labs">No. of labs</option>
          <option value="no_of_computer_labs">No. of computer labs</option>
          <option value="no_of_auditoriums">No. of auditoriums</option>
          <option value="total_sitting_capacity_in_main_auditorium">Auditorium Capacity</option>
          <option value="no_of_conference_rooms">No. of conf. rooms</option>
          <option value="no_of_recreation_rooms">No. of recreation rooms</option>
          <option value="no_of_faculty_cabins">No. of faculty cabins</option>
          <option value="no_of_PCs_provided_to_student">No. of PCs to student</option>
          <option value="no_of_PCs_provided_to_faculty">No. of PCs to faculty</option>
          <option value="no_of_PCs_provided_to_other_than_faculty">No. of PCs to other than faculty</option>
          <option value="total_PCs_in_campus">Total number of PCs in campus</option>
          <option value="no_of_latest_instruments_in_labs">No. of latest instr.</option>
          <option value="availability_of_water_recyling_unit">Avail of water recyle unit</option>
          <option value="availability_of_anti_ragging_cell">Avail of anti-ragging cell</option>
          <option value="availability_of_grievance_redressal_mechanism">Avail of grievance mechanism</option>
          <option value="availability_of_internal_complaints_commitee">Avail of internal complaint</option>
          <option value="availability_of_NSS_cell">Avail of NSS cell</option>
          <option value="availability_of_IQAC">Avail of IQAC</option>
          <option value="availability_of_faculty_feedback_mechanism">Avail of faculty feedback mechanism</option>
          <option value="availability_of_alumini_association">Avail of alumini association</option>
          <option value="no_of_alumini">No. of alumini</option>
          <option value="availability_of_incubation_centre">Avail of incubation centre</option>
          <option value="no_of_companies_setup_in_last_5_years_by_incubation_centre">Companies in 5yr by incubation</option>
          <option value="hostel_facilities_for_boys">Boys's hostel facility</option>
          <option value="area_of_boys_hostel">Boy's hostel area</option>
          <option value="capacity_of_boys_hostel">Boy's hostel capacity</option>
          <option value="no_of_boys_in_hostel">No. of boys in hostel</option>
          <option value="hostel_facilities_for_girls">Girl's hostel facility</option>
          <option value="area_of_girls_hostel">Girl's hostel area</option>
          <option value="capacity_of_girls_hostel">Girl's hostel capacity</option>
          <option value="no_of_girls_in_hostel">No. of girls in hostel</option>
          <option value="no_of_students_availing_hostel_facilities">Total students availing hostel facility</option>
          <option value="residence_facility_for_faculty">Faculty stay facility</option>
          <option value="total_staff_quarters">Total staff quarters</option>
          <option value="how_many_faculties_residing_in_college_campus">Faculty staying in campus</option>
          <option value="no_of_faculties_visited_any_foreign_university_in_previous_AY">No. of faculty visited foreign uni. in previous AY</option>
          <option value="institute_tieup_with_foreign_university">Institue tie-up with foreign university</option>
          <option value="no_of_tie_up">Total no. of tie-up</option>
          <option value="tieup_university_details">Tie-Up Details</option>
          <option value="no_of_clubs_in_college">No. of societies/clubs in college</option>
          <option value="club_details">Society/Clubs Details</option>
          <option value="canteen">Canteen</option>
          <option value="cricket_ground">Cricket Ground</option>
          <option value="basketball_court">Basketball Court</option>
          <option value="football_ground">Football Ground</option>
          <option value="swimming_pool">Swimming Pool</option>
          <option value="lawn_tennis_court">Lawn Tennis Court</option>
          <option value="badminton_court">Badminton Court</option>
          <option value="bank_branch">Bank branch</option>
          <option value="wifi_facilities">Wifi facility</option>
          <option value="table_tennis_boards">Table Tennis Boards</option>
          <option value="gymnasium">Gymnasium</option>
          <option value="bank_ATM">Bank ATM</option>
          <option value="no_of_publications_by_college">No. of publications</option>
          <option value="publication_details">Publication Details</option>
      </select>
    </div>    
  `;
  removeChildren(document.getElementsByClassName("field_infra_columns"));
  for (let i = 0; i < ncols; i++) {
    let child = document.createElement("div");
    child.style = 'display: inline-block;width: 40%; margin-left: 98px;box-sizing: border-box;';
    child.innerHTML = template;
    inputColumns.append(child);
  } 
}

function displaySocieties() {
  let club_names = document.querySelectorAll(".society_name");
  let club_types = document.querySelectorAll(".society_type");
  let textarea = document.querySelector(".clubs_text");
  textarea.value = "";
  let value = textarea.value;
  let data_obj = {};
  for (let i = 0; i < club_names.length; i++) {
    let obj = {
      name: club_names[i].value,
      type: club_types[i].value,
    };
    data_obj[obj.name] = obj.type;
  }
  textarea.value = JSON.stringify(data_obj);
}

function submitPublishData(){
    
    let publication = parseInt($('#publication_no').val());
    if( publication==0 ){
      return;
    }else{
      let publication_details = {};
      let i = 1;
      console.log(i)
      $('.publishers').each(function(){
        let current_publication = {
          'published_by_name' : '',
          'type_of_publication' : '',
          'freq_of_publication' : '',
          'publication_circulation' : '',
        }
        current_publication['published_by_name'] = $(this).find('.published_by_name').val();
        current_publication['type_of_publication'] = $(this).find('.type_of_publication').val();
        current_publication['freq_of_publication'] = $(this).find('.freq_of_publication').val();
        current_publication['publication_circulation'] = $(this).find('.publication_circulation').val();
        publication_details[i] = current_publication;
        i++;
      });
      $('#publication_data').val(JSON.stringify(publication_details));
    }
} 

/* function submitUpdatedPublishData(){
  //$('#Publication_Data').val('');  
  let publication = parseInt($('#epublishers').val());
  if( publication==0 ){
    console.log('hi')
    return;
  }else{
    let publication_details = {};
    let i = 1;
    console.log(i);
    $('.edit_publishers').each(function(){
      let current_publication = {
        'published_by_name' : '',
        'type_of_publication' : '',
        'freq_of_publication' : '',
        'publication_circulation' : '',
      }
      current_publication['published_by_name'] = $(this).find('.published_by_name').val();
      current_publication['type_of_publication'] = $(this).find('.type_of_publication').val();
      current_publication['freq_of_publication'] = $(this).find('.freq_of_publication').val();
      current_publication['publication_circulation'] = $(this).find('.publication_circulation').val();
      publication_details[i] = current_publication;
      i++;
    });
    $('#Publication_Data').val(JSON.stringify(publication_details));
  }
}  */


function submitTieupData(){
  
  let tie_up = parseInt($('#tieups').val());
  if( tie_up==0 ){
    return;
  }else{
    let tieup_details = {};
    let i = 1;
    $('.tieup_fields').each(function(){
      let current_tieup = {
        'tieup_uni_name' : '',
        'tieup_uni_address' : '',
        'tieup_uni_phone' : '',
        'tieup_uni_email' : '',
        'type_of_mou' : '',
        'tieup_MoU_proof' : '',
        'tieup_student_foreign_exchange' : '',
        'tieup_student_participated_foreign_exchange' : '',
      }
      current_tieup['tieup_uni_name'] = $(this).find('.tieup_uni_name').val();
      current_tieup['tieup_uni_address'] = $(this).find('.tieup_uni_address').val();
      current_tieup['tieup_uni_phone'] = $(this).find('.tieup_uni_phone').val();
      current_tieup['tieup_uni_email'] = $(this).find('.tieup_uni_email').val();
      current_tieup['type_of_mou'] = $(this).find('.type_of_mou').val();
      if($(this).find('.tieup_MoU_proof').val()==''){
        current_tieup['tieup_MoU_proof'] = $(this).find('.prev_mou_proof').html();
      }
      else{
          current_tieup['tieup_MoU_proof'] = $(this).find('.tieup_MoU_proof').val();
      }
      current_tieup['tieup_student_foreign_exchange'] = $(this).find('.tieup_student_foreign_exchange').val();
      current_tieup['tieup_student_participated_foreign_exchange'] = $(this).find('.tieup_student_participated_foreign_exchange').val();
      tieup_details[i] = current_tieup;
      $(this).find('.tieup_MoU_proof').attr('name','tieup_MoU_proof_'+i);
      i++;
    });
    $('#tieup_data').val(JSON.stringify(tieup_details));
  }
} 

/* function submitUpdatedTieupData(){
    let tie_up = parseInt($('#etieups').val());
    if( tie_up==0 ){
      return;
    }else{
      let tieup_details = {};
      let i = 1;
      $('.tieup_edit_fields').each(function(){
        let current_tieup = {
          'tieup_uni_name' : '',
          'tieup_uni_address' : '',
          'tieup_uni_phone' : '',
          'tieup_uni_email' : '',
          'type_of_mou' : '',
          'tieup_MoU_proof' : '',
          'tieup_student_foreign_exchange' : '',
          'tieup_student_participated_foreign_exchange' : '',
        }
        current_tieup['tieup_uni_name'] = $(this).find('.tieup_uni_name').val();
        current_tieup['tieup_uni_address'] = $(this).find('.tieup_uni_address').val();
        current_tieup['tieup_uni_phone'] = $(this).find('.tieup_uni_phone').val();
        current_tieup['tieup_uni_email'] = $(this).find('.tieup_uni_email').val();
        current_tieup['type_of_mou'] = $(this).find('.type_of_mou').val();
        if($(this).find('.tieup_MoU_proof').val()==''){
        current_tieup['tieup_MoU_proof'] = $(this).find('.prev_mou_proof').html();
      }
        else{
          current_tieup['tieup_MoU_proof'] = $(this).find('.tieup_MoU_proof').val();
        }
        current_tieup['tieup_student_foreign_exchange'] = $(this).find('.tieup_student_foreign_exchange').val();
        current_tieup['tieup_student_participated_foreign_exchange'] = $(this).find('.tieup_student_participated_foreign_exchange').val();
        tieup_details[i] = current_tieup;
        $(this).find('.tieup_MoU_proof').attr('name','tieup_MoU_proof_'+i);
        i++;
      });
      $('#Tieup_Data').val(JSON.stringify(tieup_details));
  }
}  */

function findTotalPCs() {
  let arr = document.querySelectorAll(".countPC");
  var tot = 0;
  for (var i = 0; i < arr.length; i++) {
    if (parseInt(arr[i].value)) tot += parseInt(arr[i].value);
  }
  document.getElementById("totalPC").value = tot;
}

function findTotalStu() {
  let arr = document.querySelectorAll(".countStu");
  var tot = 0;
  for (var i = 0; i < arr.length; i++) {
    if (parseInt(arr[i].value)) tot += parseInt(arr[i].value);
  }
  document.getElementById("totalStu").value = tot;
}

function yesnoCheck(){
if(document.getElementById("yesCheck").selected){
  document.getElementById("ifYes").style.display="block";
}else{
  document.getElementById("ifYes").style.display="none";
}  
}

//Infrastructure code ends---------------------------------------------------------------------------------------------------------------------
