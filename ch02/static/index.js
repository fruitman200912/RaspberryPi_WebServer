let num = 0

function p() {
  num++;
  document.getElementById("num").innerText = num;
}

getElementById("path").addEventListener("click", function() {
    location.href='http://10.150.0.202:5000/save'+n
    n = 0;
    num.innerHTML = n;
})
