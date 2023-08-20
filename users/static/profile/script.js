document.getElementById("submitBtn").addEventListener("click", function () {
    var referralCode = document.getElementById("referralCode").value;

    var urlParams = new URLSearchParams(window.location.search);
    var phoneNumber = urlParams.get("PhoneNumber");

    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    fetch('/api/referral/patch/' + phoneNumber + '/', {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ ReferralCode: referralCode }),
    })
        .then(response => {
            // ваш код обработки ответа
        })
        .catch(error => {
            console.error('Ошибка при отправке запроса:', error);
        });
});