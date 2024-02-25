 <style>
/* PUT THIS IN THE HEAD SECTION OF THE FUNNEL SETTINGS */
body {
       display: none !important;
     }
</style>

<script type="text/javascript">
      // PUT THIS IN THE BODY SECTION OF THE FUNNEL SETTINGS
      (function() {
        var correctPassword = 'yourPassword'; // Replace 'yourPassword' with the actual password
        var userInput = prompt('Please enter the password to access this page:');

        if(userInput === correctPassword) {
          // Correct password: Remove the style hiding the body
          document.body.style.display = 'block';
        } else {
          // Incorrect password: Optionally, clear the body content or redirect
          alert('Access Denied');
          document.body.innerHTML = ''; // Clear the body content
        }
      })();
    </script>
