function setLoggedIn(userId) {
  $.ajax({
    url: `http://localhost:8085/api/users/${userId}`,
    type: 'GET',
    success: function(result) {
      const username = result.username;
      $("#username").text(username);
    },
    error: function(error){
      console.log(error);
    }
  });
}

const userId = localStorage.getItem("activeUserId");
if (userId) {
  document.getElementById("login").classList.add("hidden");
  document.getElementById("sign-up").classList.add("hidden");
  setLoggedIn(userId);
} else {
  document.getElementById("logout").classList.add("hidden");
  document.getElementById("new-auction").classList.add("hidden");
}

document.getElementById("logout").addEventListener("click", (e) => {
  localStorage.removeItem("activeUserId");
  location.reload();
});
