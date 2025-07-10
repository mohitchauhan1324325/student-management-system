const token = localStorage.getItem("token");
if (!token) {
  alert("Please login first");
  window.location.href = "login.html";
}

document.getElementById("studentForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const student = {
    name: document.getElementById("name").value,
    age: parseInt(document.getElementById("age").value),
    grade: document.getElementById("grade").value
  };

  const res = await fetch("http://127.0.0.1:8000/students", {
  method: "GET",
  headers: {
    "Authorization": `Bearer ${token}`
  }
});


  const result = await response.json();
  document.getElementById("message").innerText = result.message || "Student added!";
});
