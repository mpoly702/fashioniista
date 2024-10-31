document.addEventListener('DOMContentLoaded', function() {
  const formElement = document.getElementById('signup-form');
  const signupButton = document.getElementById('signup-btn');

  // Ensure that the signup button exists
  if (signupButton && formElement) {
      // Add event listener to the signup button
      signupButton.addEventListener('click', function(event) {
          console.log("Signup button clicked");  // Debugging to confirm the click event is working

          // Prevent default form submission behavior
          event.preventDefault();
      // Get the form field values using their IDs
      const fullName = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      const phone = document.getElementById('phone').value;


      // Create a JSON object with the form field values
      const userData = {
        'Full name': fullName,
        'Email': email,
        'Password': password,
        'Phone number': phone
      };
          // Send the form data to the Flask server using fetch
          fetch('/', {
              method: 'POST',
              body: JSON.stringify(userData), // Send JSON object as string
              headers: {
                "Content-type": 'application/json'
              },
              redirect: 'follow' 
          })
          .then(response => {
            if (response.ok) {
              alert('Signup successful!');
              window.location.href = 'login';
            } else {
              alert('Signup failed!');
            }
          })
          .catch(error => {
              // Handle any errors
              console.error("Error:", error);
              alert('Signup failed!');
          });
      });
  }
});

// login.html JavaScript code

// Get form elements
const loginForm = document.getElementById('login-form');
const emailInput = document.getElementById('logmail');
const passwordInput = document.getElementById('logpass');

// Add event listener to form submission
loginForm.addEventListener('submit', (e) => {
  e.preventDefault();

  // Get input values
  const email = emailInput.value;
  const password = passwordInput.value;

  // Validate input fields
  if (!email || !password) {
    alert('Please fill in all fields');
    return;
  }

  // Create JSON data object
  const data = {
    email,
    password
  };

  // Fetch API request
  fetch('/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.status === 'success') {
      window.location.href = '/dashboard'; // Redirect to dashboard
    } else {
      alert(data.message); // Display error message
    }
  })
  .catch((error) => console.error('Error:', error));
});



/* eye toggler */
function togglePasswordVisibility() {
  const passwordInput = document.getElementById('logpass');
  const eyeIcon = document.querySelector('.eye-icon');
  
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    eyeIcon.classList.add('active');
  } else {
    passwordInput.type = 'password';
    eyeIcon.classList.remove('active');
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const redirectLinks = document.querySelectorAll('[data-bs-toggle="redirect"]');

  redirectLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const targetUrl = link.getAttribute("data-bs-target");
      window.location.href = targetUrl;
    });
  });
});