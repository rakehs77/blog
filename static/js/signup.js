$().ready(function() {
    $("#signup_form").validate({
        rules: {
            username: {
                required: true,
                minlength: 6,
            },
            email: {
                required: true,
                email: true
            },
            password1: {
                required: true,
                minlength: 8,
            },
            password2: {
                required: true,
                minlength: 8,
                equalTo: "#id_password1"
            },
        },
        messages: {
            username: {
                required: "Please enter a username",
                minlength: "Your username must consist of at least 6 characters",
            },
            password1: {
                required: "Please enter a password",
                minlength: "Your password must consist of at least 8 characters long"
            },
            password2: {
                required: "Please enter a password",
                minlength: "Your password must consist of at least 8 characters long",
                equalTo: "Please enter same password as above"
            },
        }
    })
})