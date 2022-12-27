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
    // let icon = document.createElement("i")
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

function showAllCols(){
  $("#fillColumns").val("id,event_name,type_of_event,Audience,Societies,Departments,Organized_by,Conducted_by,sponsors_details,total_sponsored_amt,start_date,end_date,no_of_participants,upload_attendance,upload_report");
  $("#no_of_cols").val('14');
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
    AddMemberDetails(1)
  }
}

function AddMemberDetails(size){
    size = parseInt(size)
    if(size <= 0 || isNaN(size)){
        size = 1;
    }

    $("#member_details").removeClass("d-none");

    $("#insert_member_details").html('');
    for(let i=0;i<size;i++){
        let tmp = `<fieldset class="border border-2 p-3 member_detail">
        <legend  class="float-none w-auto">Member's Details</legend>
        <div class="form-group  align-center float-child">
            <label class="w-25 required_asterisk" for="exampleFormControlInput1">Student Name</label>
            <input required class="w-30 student_name " type="text" name="name" id=""  style = "height: 32px;
            border-radius: 4px;">
        </div>
        <div class="form-group  align-center float-child">
            <label class="w-25 required_asterisk" for="exampleFormControlInput1">Enrollment Number</label>
            <input required class="w-30 student_eroll_no" type="number" name="eroll_no" id=""  style = "height: 32px;
            border-radius: 4px;">
        </div>
        
        <div class="form-group  align-center float-child" >
            <label class="w-25 required_asterisk" for="exampleFormControlInput1">Semester</label>
            <select required id=""  name="semester" class="m-1 w-30 semester" >
                <option value="-1">Select Values</option>
                <option value="1" >1</option>
                <option value="2" >2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
            </select>
        </div>
        <div class="form-group  align-center float-child" id = "departments-involved">
            <label class="w-25 required_asterisk" for="exampleFormControlInput1">Departments Involved</label>
            <select required id="department" name="Departments" class="m-1 w-30 departments">
                <option value="-1">Select Values</option>
                <option value="CSE" >CSE</option>
                <option value="IT">IT</option>
                <option value="ECE">ECE</option>
                <option value="EEE">EEE</option>
                <option value="Applied Science">Applied Science</option>
            </select>
        </div>
                                
        <div class="form-group  align-center float-child" >
            <label class="w-25 required_asterisk" for="exampleFormControlInput1">Class/Section</label>
            <select required id="" name="Class" class="m-1 w-30 class_section">
                <option value="-1">Select Values</option>
                <option value="1" >I</option>
                <option value="2" >II</option>
                <option value="3">III</option>
                <option value="Evening">Evening</option>
            </select>
        </div>
        <div class="form-group  align-center float-child">
            <label class="w-25 required_asterisk" for="exampleFormControlInput1">Mobile Number</label>
            
            <input required type="tel"  placeholder="" pattern="[1-9]{1}[0-9]{9}" maxlength="10" class = "mobileNo" title="Ten digits code"  name="mobile_no" style = "height: 32px;border-radius: 4px;" />    
        </div>
        <div class="form-group  align-center float-child">
            <label class="w-25 required_asterisk" for="exampleFormControlInput1">Email Id</label>
            <input required class="w-30 emailID " type="email" name="mail_id" id=""  style = "height: 32px;
            border-radius: 4px;">
        </div>
    </fieldset> <br>   
    `
        $("#insert_member_details").append(tmp);
    }
}

function showFilters(){
  $("#filterDataDiv").removeClass('d-none');
  $(".show_filter_data").each(function(e){
    $(this).val('True');
  });
}

function submit_member_data(){
    let members_data = {};
    let i=1;
    $('.member_detail').each(function(){
        let member = {
            'student_name':'',
            'eroll_no':'',
            'semester':'',
            'class':'',
            'department':'',
            'mobile_no':'',
            'email_id':'',
        }

        member['student_name'] = $(this).find(".student_name").val();
        member['eroll_no'] = $(this).find(".student_eroll_no").val();
        member['semester'] = $(this).find(".semester").val();
        member['class'] = $(this).find(".class_section").val();
        member['department'] = $(this).find(".departments").val();
        member['mobile_no'] = $(this).find(".mobileNo").val();
        member['email_id'] = $(this).find(".emailID").val();
        
        members_data[i] = member;
        i++;
    })
    
    $("#member_details_data").val(JSON.stringify(members_data));
    console.log(JSON.stringify(members_data));

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
    let offer = `<br>
      <fieldset class="border border-2 p-3 offer_detail" id="if_placed">
        <legend class="float-none w-auto">Offer - `+ (i+1) +` Details</legend>
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
          <label class="w-25 required_asterisk" for="exampleFormControlFile1">Upload Proof</label>
          <input class="w-30 m-1 upload_proof" type="file" name="upload_proof" class="form-control-file" id="exampleFormControlFile1" accept ="application/pdf" style = "height: 32px;border-radius: 4px;">
        </div>
      </fieldset>
    `;
    $('.offer_details').append(offer);
  }
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
        <legend class="float-none w-auto">Exam - `+ (i+1) +` Details</legend>
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
          <select class="m-1 w-30 qualified" id=`+ unique_id +` onchange="examResultDeclared(this.id)">
            <option value="yes">Yes</option>
            <option value="no">No</option>
            <option value="not_declared" selected>Not Declared</option>
          </select>
        </div>
        <div class="form-group align-center float-child `+ unique_id +` d-none">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Exam Score</label>
          <input class="w-30 exam_score" type="number" name="exam_score" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child `+ unique_id +` d-none">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Exam Rank</label>
          <input class="w-30 exam_rank" type="number" name="exam_rank" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child `+ unique_id +` d-none">
          <label class="w-25 required_asterisk" for="exampleFormControlInput1">Date of Result</label>
          <input class="w-30 date_of_result" type="date" name="date_of_result" id="" required style = "height: 32px;
          border-radius: 4px;">
        </div>
        <div class="form-group align-center float-child `+ unique_id +` d-none">
          <label class="w-25 required_asterisk" for="exampleFormControlFile1">Result Proof</label>
          <input class="w-30 m-1 result_proof" type="file" name="result_proof" class="form-control-file" id="exampleFormControlFile1" accept ="application/pdf" style = "height: 32px;border-radius: 4px;">
        </div>
      </fieldset>
    `;
    $('.exam_details').append(offer);
  }
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
        <label class="w-25 required_asterisk" for="exampleFormControlFile1">Upload Proof(LOJ OR I-Card)</label>
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
        <label class="w-25 required_asterisk" for="exampleFormControlFile1">Upload Proof(I-Card)</label>
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
          <option value="entrance_exam">Preparing for Entrance Exam</option>
          <option value="jobs">Jobs</option>
        </select>
      </div>
    `;
  }
  $('.status_details').html(status_details);
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
          'exam_score' : 'Not Declared',
          'exam_rank' : 'Not Declared',
          'date_of_result' : '',
        }
        current_exam['exam_name'] = $(this).find('.exam_name').val();
        current_exam['exam_roll_no'] = $(this).find('.exam_roll_no').val();
        current_exam['exam_date'] = $(this).find('.exam_date').val();
        current_exam['qualified'] = $(this).find('.qualified').val();
        if(current_exam['qualified'] != 'not_declared'){
          current_exam['exam_score'] = $(this).find('.exam_score').val();
          current_exam['exam_rank'] = $(this).find('.exam_rank').val();
          current_exam['date_of_result'] = $(this).find('.date_of_result').val();
          exam_details[i] = current_exam;
          $(this).find('.result_proof').attr('name','result_proof_'+i);
        }else{
          exam_details[i] = current_exam;
        }
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
      'exam_score' : 'Not Declared',
      'exam_rank' : 'Not Declared',
      'date_of_result' : '',
    }
    exam['exam_name'] = $(this).find('.exam_name').val();
    exam['exam_roll_no'] = $(this).find('.exam_roll_no').val();
    exam['exam_date'] = $(this).find('.exam_date').val();
    exam['qualified'] = $(this).find('.qualified').val();
    if(exam['qualified'] != 'not_declared'){
      exam['exam_score'] = $(this).find('.exam_score').val();
      exam['exam_rank'] = $(this).find('.exam_rank').val();
      exam['date_of_result'] = $(this).find('.date_of_result').val();
      existing_exam[i] = exam;
      $(this).find('.result_proof').attr('name','result_proof_'+i);
    }else{
      existing_exam[i] = exam;
    }
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
        'exam_score' : 'Not Declared',
        'exam_rank' : 'Not Declared',
        'date_of_result' : '',
      }
      current_exam['exam_name'] = $(this).find('.exam_name').val();
      current_exam['exam_roll_no'] = $(this).find('.exam_roll_no').val();
      current_exam['exam_date'] = $(this).find('.exam_date').val();
      current_exam['qualified'] = $(this).find('.qualified').val();
      if(current_exam['qualified'] != 'not_declared'){
        current_exam['exam_score'] = $(this).find('.exam_score').val();
        current_exam['exam_rank'] = $(this).find('.exam_rank').val();
        current_exam['date_of_result'] = $(this).find('.date_of_result').val();
        exam_details[i] = current_exam;
        $(this).find('.result_proof').attr('name','result_proof_'+i);
      }else{
        exam_details[i] = current_exam;
      }
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
