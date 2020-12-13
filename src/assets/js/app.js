new function() {
	const hamburger = document.getElementById('hamburger');
	let navHidden = true;

	if (window.IntersectionObserver) {
		const socialActions = document.querySelector('.social-actions');
		const getInTouch = document.getElementById('get-in-touch');

		const getInTouchObserver = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					socialActions.classList.add('return');
				} else {
					socialActions.classList.remove('return');
				}
			});
		});
		if (getInTouch) getInTouchObserver.observe(getInTouch);

		const animationObserver = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					entry.target.classList.add(entry.target.getAttribute('data-animation'));
					entry.target.classList.remove('animate');
					animationObserver.unobserve(entry.target);
				}
			});
		});
		document.querySelectorAll('.animate').forEach((element) => {
			animationObserver.observe(element);
		});

		const videoObserver = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						entry.target.play();
						videoObserver.unobserve(entry.target);
					}
				});
			},
			{ threshold: 0.5 }
		);
		document.querySelectorAll('video').forEach((element) => {
			videoObserver.observe(element);
		});
	} else console.log('IntersectionObserver not present');

	if (hamburger)
		hamburger.addEventListener('click', () => {
			if (navHidden) {
				showNav();
			} else {
				hideNav();
			}
		});

	function showNav() {
		let navElements = document.querySelectorAll('#home, #projects, #about, #contact');
		hamburger.classList.add('icon--hamburger--active');
		document.getElementById('bg-video').pause();

		navElements.forEach((element) => {
			element.classList.add('nav__element');
			element.classList.add('nav__element--' + element.id);
			element.addEventListener('click', () => {
				hideNav();
				location.href = '#' + element.id;
			});
		});
		navHidden = false;
	}

	function hideNav() {
		let navElements = document.querySelectorAll('#home, #projects, #about, #contact');
		hamburger.classList.remove('icon--hamburger--active');
		document.getElementById('bg-video').play();
		navElements.forEach((element) => {
			element.classList.remove('nav__element');
			element.classList.remove('nav__element--' + element.id);
		});
		navHidden = true;
	}
}();
