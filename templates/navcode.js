function onActiveUser(callback) {
  $.ajax({
    url: `http://localhost:8085/api/users/userfromtoken`,
    type: 'POST',
    contentType: 'application/json',
    data: localStorage.getItem("activeUserToken"),
    success: function(result) {
      callback(result);
    },
    error: function(error){
      console.log(error);
    }
  });
}

if (localStorage.getItem("activeUserToken")) {
  document.getElementById("login").classList.add("hidden");
  document.getElementById("sign-up").classList.add("hidden");
  onActiveUser((user) => {
    document.getElementById("username").innerText = user.username;
  });
} else {
  document.getElementById("logout").classList.add("hidden");
  document.getElementById("new-auction").classList.add("hidden");
}

document.getElementById("logout").addEventListener("click", (e) => {
  localStorage.removeItem("activeUserToken");
  location.reload();
});
