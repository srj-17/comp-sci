$(document).ready(function () {
    $("#myForm").submit(function (e) {
        e.preventDefault();
        $("#username-error").text("");
        $("#password-error").text("");

        let username = $("#username").val();
        let password = $("#password").val();

        if (!username) {
            $("#username-error").text("Username can't be empty.");
            return false;
        }

        if (!password) {
            $("#password-error").text("Password can't be empty");
            return false;
        }

        return true;
    });
});
