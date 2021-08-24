function hide(id_) {
    var x = document.getElementById(id_);
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }