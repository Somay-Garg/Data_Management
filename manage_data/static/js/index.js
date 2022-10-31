// function add_sponsors(spon) {

//   spon = parseInt(spon);
//   var spon_node = $(".clone_sponsors").find("input").clone();
//   spon_node.prop("disabled", false);
//   if (spon == 0 || isNaN(spon)) {
//     spon = 1;
//   }
//   let sponsors1 = document.querySelector(".sponsors1");
//   if(sponsors1.value == "MSIT"){
//     $('.actual_sponsors').html('');
//   }else if(sponsors1.value == "Others"){
//     $('.actual_sponsors').html('');
//     var sponsors = $(".actual_sponsors");
//     for (var i = 0; i < spon ; i++) {
//       sponsors.append(spon_node.clone());
//     }
//   }else{
//     $('.actual_sponsors').html('');
//     var sponsors = $(".actual_sponsors");
//     for (var i = 0; i < spon-1 ; i++) {
//       sponsors.append(spon_node.clone());
//     }
//   }
// }

function addSponsors(spon) {
  // let spon = document.querySelector("#no_of_sponsors");
  let nspons = parseInt(spon);
  let inputSponsors = document.querySelector("#inputSponsors");
  let sponsLabel = document.querySelector(".sponsors");
  // if(inputSponsors.childElementCount > 1)
  //   inputSponsors.removeChild(inputSponsors.lastChild);
  let tmp = `<div class="sponsors">
  <label class="w-25" for="exampleFormControlInput1">Sponsor Name</label>
  <input type="text" name="spons_name" id="" class = "w-30 m-1">
  <label class="w-25" for="exampleFormControlInput1">Sponsored Amount</label>
  <input type="number" name="spons_amount" id="" class = "w-30 m-1 spons_amount" oninput = "findTotal()" required>
</div>`;
  removeSponsors();
  for (let i = 0; i < nspons; i++) {
    let child = document.createElement("div");
    child.innerHTML = tmp;
    inputSponsors.append(child);
  }
}

function removeSponsors() {
  let inputSponsors = document.querySelector("#inputSponsors");
  var elements = inputSponsors.getElementsByClassName("sponsors");

  while (elements[0]) {
    elements[0].parentNode.removeChild(elements[0]);
  }
}

function findTotal() {
  let arr = document.querySelectorAll(".spons_amount");
  var tot = 0;
  for (var i = 0; i < arr.length; i++) {
    if (parseInt(arr[i].value)) tot += parseInt(arr[i].value);
  }
  document.getElementById("total").value = tot;
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
}
