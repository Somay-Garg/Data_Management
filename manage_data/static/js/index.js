function addSponsors(spon) {
  let nspons = parseInt(spon);
  let inputSponsors = document.querySelector("#inputSponsors");
  let sponsLabel = document.querySelector(".sponsors");

  let tmp = `<div class="sponsors">
    <label class="w-25 required_asterisk" for="exampleFormControlInput1">Sponsor Name</label>
    <input type="text" name="sponsored_by" class = "w-30 m-1 sponsored_by_name">
    <label class="w-25 required_asterisk" for="exampleFormControlInput1">Sponsored Amount</label>
    <input type="number" name="spons_amount" id="" class = "w-30 m-1 spons_amt_individually" oninput = "findTotal();displaySponsors()" required>
  </div>`;
  var elements = inputSponsors.getElementsByClassName("sponsors");

  removeChildren(elements);
  for (let i = 0; i < nspons; i++) {
    console.log("hii");
    let child = document.createElement("div");
    child.innerHTML = tmp;
    // insertAfter(child, document.querySelector("#sponsors"));
    inputSponsors.append(child);
  }
}

function addColumns(cols) {
  let ncols = parseInt(cols);
  let inputColumns = document.querySelector("#inputColumns");
  let template = `
    <div class = "field_columns">
      <label class="w-25 required_asterisk" for="exampleFormControlInput1">Field:</label>
      <select class="fill-columns" class="w-30 m-1" oninput="getFields()">
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
    child.innerHTML = template;
    inputColumns.append(child);
  }
}

function getFields() {
  let area = document.querySelector("#fillColumns");
  let cols = document.querySelectorAll(".fill-columns");
  console.log(cols);
  area.value = "";

  let arr = [];
  for (let i = 0; i < cols.length; i++) {
    arr.push(cols[i].value);
  }
  area.value = JSON.stringify(arr);
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
    var dtToday = new Date();

    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();

    if (month < 10) month = "0" + month.toString();
    if (day < 10) day = "0" + day.toString();

    var maxDate = year + "-" + month + "-" + day;
    $(".datesettup").attr("max", maxDate);
  });
  // end date set
  $(function () {
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
  });
  // strt date set
  $(function () {
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
  });

  // societyOPtions
  $(function () {
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
  });

  //departments option
  $(function () {
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
  });

  $(function () {
    let spondataJSON = document.querySelector("#sponDets").value;
    // console.log(spondataJSON);
    let parentDiv = document.querySelector("#inputSponsors");
    let sponData = JSON.parse(spondataJSON);
    console.log(sponData);
    let arr = Object.entries(sponData);
    console.log(arr);
    for (let i = 0; i < arr.length; i++) {
      let sponName = arr[i][0];
      let sponAmt = arr[i][1];
      let template = `<div class="sponsors">
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Sponsor Name</label>
        <input type="text" name="sponsored_by" class = "w-30 m-1 sponsored_by_name"  oninput = "findTotal();displaySponsors()" value = ${sponName} >
        <label class="w-25 required_asterisk" for="exampleFormControlInput1">Sponsored Amount</label>
        <input type="number" name="spons_amount" id="" class = "w-30 m-1 spons_amt_individually" oninput = "findTotal();displaySponsors()" value =${sponAmt} required></div>`;
      let child = document.createElement("div");
      child.innerHTML = template;
      parentDiv.appendChild(child);
    }
  });

  // table display
  // $(function(){
  //   let tablediv = document.querySelector("#table-fields");
  //   tablediv.style.display = "none";
  // })
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
  $('#table-fields').style.display = 'block';
}