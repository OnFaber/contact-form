'use strict';

document.addEventListener('DOMContentLoaded', function () {
    const flashMessages = document.querySelectorAll('.success');

    flashMessages?.forEach((message, index) => {
	setTimeout(() => {
	    message.classList.add('show');
	}, 100 + index * 500); // Ritardo crescente per ogni messaggio

	// Nasconde il messaggio automaticamente dopo 3 secondi
	setTimeout(() => {
	    message.classList.remove('show');
	}, 3000 + index * 500);
    })
})
