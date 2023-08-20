document.addEventListener("DOMContentLoaded", function () {
    var submitBtn = document.getElementById("submitBtn");
    var closeModalBtn = document.getElementById("closeModal");
    var modal = document.getElementById("myModal");
    var additionalInput = document.getElementById("additionalInput");
    var confirmBtn = document.createElement("button");

    submitBtn.addEventListener("click", function () {
        var phoneNumber = document.getElementById("phoneNumber").value;
        var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        fetch('/api/phone/authentication', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ PhoneNumber: phoneNumber }),
        })
            .then(response => response.json())
            .then(data => {
                // Обработка ответа от сервера
                var modalContent = document.querySelector(".modal-content");
                modalContent.innerHTML = `
                    <span class="close" id="closeModal">&times;</span>
                    <p>${data.GeneratedNumber}</p>
                `;
                modalContent.appendChild(additionalInput);
                modalContent.appendChild(confirmBtn);
                confirmBtn.textContent = "подтвердить";
                modal.style.display = "block";

                confirmBtn.addEventListener("click", function () {
                    var userInput = additionalInput.value.trim();
                    if (userInput == data.GeneratedNumber) {
                        var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

                        fetch('/api/referral/create', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': csrfToken,
                            },
                            body: JSON.stringify({ PhoneNumber: phoneNumber }),
                        })
                            .then(response => {
                                if (response.status === 201) {
                                    var phoneNumber = document.getElementById("phoneNumber").value;
                                    window.location.href = '/profile/?PhoneNumber=' + phoneNumber;
                                }
                            })
                            .catch(error => {
                                console.error('Ошибка при отправке запроса:', error);
                            });
                    } else {
                        console.log("Код не верен");
                    }
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    closeModalBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});