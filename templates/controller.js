// TO-DO: Figure out formatter.js for the phone number

new Formatter(document.getElementById('phone-input'), {
  'pattern': '({{999}}) {{999}} - {{9999}}',
  'persistent': false
});

// JS for material design
function leaveInput(el) {
		if (el.value.length > 0) {
				if (!el.classList.contains('active')) {
						el.classList.add('active');
				}
		} else {
				if (el.classList.contains('active')) {
						el.classList.remove('active');
				}
		}
}

var inputs = document.getElementsByClassName("m-input");
for (var i = 0; i < inputs.length; i++) {
		var el = inputs[i];
		el.addEventListener("blur", function() {
				leaveInput(this);
		});
}