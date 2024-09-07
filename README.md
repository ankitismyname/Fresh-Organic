E-Commerce Website Project
Welcome to the E-Commerce Website Project! This project demonstrates a fully functional online store where users can browse products, manage their shopping cart, and access personalized profiles.

Features
Shopping Cart System: Users can add items to their cart, view the cart, and proceed to checkout. Cart allows up to 10 kg of a single product.
Login/Logout System: Secure user authentication with PBKDF2_SHA256 encryption and CSRF protection.
User Profile Pages: Users can edit details, change passwords, and view order history.
Seller Functionality: Verified users can become sellers, performing all CRUD operations on their products.
Payment Gateway: Integrated Stripe for secure online payments, with Cash on Delivery (COD) as an option (additional Rs.5 for COD).
Contact Support: Email-based system for reporting issues or seeking assistance with 24/7 support.
Technologies Used
HTML: For structuring and presenting content.
CSS: For styling and layout of the website.
Bootstrap: Ensures a responsive design with pre-built components.
DOM API: For dynamic content updates.
Django: Backend framework to manage server-side logic and database operations.
PBKDF2_SHA256 & CSRF Tokens: Secure authentication and form protection.
Stripe: Payment integration.
Tools Used
Visual Studio Code: Development environment.
Web Browser: Testing and interacting with the website.
Getting Started
To run the project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/ankitismyname/Fresh-Organic.git
Navigate to the project directory:

bash
Copy code
cd Fresh-Organic
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the development server:

bash
Copy code
python manage.py runserver
Open your web browser and visit http://127.0.0.1:8000/ to explore the website.

Acknowledgments
Special thanks to the Django and Bootstrap communities for their fantastic tools and resources.
For more information, please visit the project page.
