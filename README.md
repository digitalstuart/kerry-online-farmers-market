# Kerry Online Farmers Market

![alt text](https://i.imgur.com/wRvzPpQ.jpg "Kerry Online Farmers Market as seen on different devices")

Farmers markets are popular aspects of local community life around Kerry - however, they take place at fixed locations and on specific days and times.

So how about opening up the availability of these locally grown and produced products by offering them for sale online? It is also potentially a very useful tool for farmers and producers to be able to continue selling during this period of lockdown and social isolation.

That is the purpose of Kerry Online Farmers Market. Producers can list their items and products for sale; website customers can buy them. There is also an area of the site for users to post any recipes they wish to share which include ingredients purchased from the online market.

The aim of the project at this point in its life cycle is to display what I have learnt about building an ecommerce site with Django and Python. Registered users can add objects to a database; customers can browse and select products for purchase; then there is a shopping cart and checkout functionality.

The site would require further work to make it fully functional in 'the real world', plus there are also prospects for progressive enhancement in the future, both of which are discussed later in this document.

## UX

The landing page has a very clear website heading, with a bold and attractive background image that makes it clear what the site is about.

It also has two prominent calls to action - **'Login to buy'** or **'Login to sell**'. The website's two key pieces of functionality are clearly stated to the customer.

Different navbar menu items are displayed according to the whether users are logged in or not, in particular *login/register* and *profile/logout*. It is always obvious how the user is able to interact with the site.

The website uses an attractive font for consistent headings, as well as clean Bootstrap forms. Product and recipe listings employ the same panel style of presentation.

Interaction with the site is clearly mapped through prompts and messages, which are relevant to the steps that a user can take at any given point. 

The process of selecting and purchasing a product should be achievable with just the following the steps:
* User logs in and is greeted with a 'login success' message.
* User finds desired product, selects amount and clicks **'Add'**. 
* Item(s) added to cart; user clicks on **'Cart'** menu item.
* User can amend number of selected products and/or click **'Checkout'** button.
* User completes personal and payment details form, clicks submit and then sees a 'purchase success' message.

### User Stories

* I am a farmer/producer in Kerry who wishes to make my fresh produce and products available for sale online.

![alt text](https://i.imgur.com/3aKnszE.jpg "Kerry Online Farmers Market screenshot")
* I am a Kerry resident who likes to buy locally grown and produced items from a farmers market, but I can't always get there on the days it is held. Can I buy any of the products online?

![alt text](https://i.imgur.com/6osrbTD.jpg "Kerry Online Farmers Market screenshot")
* I'd like to find recipe ideas from other people who are using fresh local ingredients.

![alt text](https://i.imgur.com/R1JfR33.jpg "Kerry Online Farmers Market screenshot")

I used Balsamiq to create some wireframes for the project. They illustrate that the idea was clear from the outset and the development and final product have been consistent with the concept. 

![alt text](https://i.imgur.com/eCov7t5.jpg "Kerry Online Farmers Market wireframe")
![alt text](https://i.imgur.com/gy4vgmn.jpg "Kerry Online Farmers Market wireframe")
![alt text](https://i.imgur.com/RChkHvP.jpg "Kerry Online Farmers Market wireframe")

## Features

### Existing features

* The site has a responsive collapsible navbar, with a burger menu and dropdown items displayed for smaller devices.
* There is a **'Find'** search box available on the navbar.
* The **'Register'** option links to a user registration form, where an email address, username and password are required to register with the site.
* The **'Login to buy'** link redirects users straight to the **'Browse products'** page once they have successfully logged in.
* The **'Login to sell'** link redirects users straight to the **'Sell your product'** page once they have successfully logged in.
* Once a user is logged, the **'Login to buy'** and **'Login to sell'** links are replaced with simply **'Buy'** and **'Sell'**. The **'Cart'** link also becomes available on the navbar, while **'Register'** is no longer shown but **'Profile'** and **'Logout'** are.
* There is a form for listing products for sale. Once completed and saved, the item then becomes available on the **'Browse products'** page.
* Each product listing includes a name, image, description and price. Users can select the quantity of any item and add to their cart.
* Product listings can be edited or deleted via links displayed on the **'Browse products'** page, however these are only visible to the logged-in user who originally created the items.
* The **'Cart'** navbar link automatically updates with a 'number badge' whenever items are added.
* The shopping cart page has options to amend the quantity of items for purchase, as well as a **'Checkout'** button.
* The **'Checkout'** page itself displays the items being bought, the total cost and a simple form for personal and payment details. NB: this currently only works with the Stripe testing default of card number '4242424242424242' and security code '111'.
* A logged-in user's **'Profile'** page shows their username, registered email address and the items they have previously purchased.
* There is a **'Contact'** page where anyone can send a message to the site; this uses the Gmail SMTP server.
* The **'Recipes'** section displays a name and image linking to individual recipe pages, which contain the relevant ingredients and cooking method. There is also a link to a form for posting a new recipe on the site.
* The login pages include a link to password reset functionality, which is an email system using the Gmail SMTP server.
* All the processes for registration, logging in/out, using the contact form, password reset and making a purchase are followed by 'success' messages displayed to the user.
* There is a floating 'back to top' button, primarily a piece of functionality for when mobile users scroll down a page and the navbar disappears from view.

### Features left to implement

* As previously mentioned, the site is currently only set up to use a Stripe 'test card' - therefore, one of the most important features left to implement would be a 'real world' Stripe set-up, which could begin with all payments going to one place and sellers invoicing the website team for their payments, before a more robust system can be implemented whereby individual sellers get their money direct.
* When a user's 'purchase history' is shown on their **'Profile'** page, it would be preferable to have an **'Add to cart'** option directly available on the relevant products. A 'date purchased' field could also be useful for customers.
* In future there would be a need to give the user the ability to filter the listed products with category types including, for example, type of product, name of seller, etc. 
* As and when a substantial database of recipes has been added to the site, a *search* functionality could be added to this section.

## Technologies

This project uses HTML, CSS, JavaScript, Bootstrap, Django/Python (including a number of imported libraries), PostgreSQL, Stripe, Amazon Web Services S3, Gmail SMTP server, Travis for continuous integration testing and Heroku for deployment.

## Testing

1. Navbar
    * Clicking on **Home** defaults to the main landing page.
    * Clicking on **Contact** redirects to the **'Get in touch'** form.
    * Clicking on **Recipes** redirects to the main **'Recipes'** page.
    * Clicking on **Register** redirects to the **'Create new account'** form.
    * When any sub-sections of the site are visited, the landing page 'calls to action' of **'Login to buy'** and **'Login to sell'** are moved to the navbar.
    * When a user is logged in:
        * The **'Find'** search box becomes visible. Inputting a search term brings up the relevant results, or a message of 'Sorry, there are no products to display at the moment!'.
        * **'Login to buy'** and **'Login to sell'** become simply **'Buy'** and **'Sell'**. 
        * The **Cart** link becomes visible; clicking on it redirects to the **'Your cart'** page.
        * The **Profile** link becomes visible; clicking on it redirects to a logged-in user's profile page.
        * The **Logout** link becomes visible; this applies the correction action when clicked, it redirects to the homepage with a message of 'You have been successfully logged out'.
    * In mobile view, the burger icon correctly displays the dropdown menu items. All links behave in the expected way, as above.
    
2. Landing page
    * Clicking on **'Login to buy'** redirects the user to a login page.
    * Clicking on **'Login to sell'** redirects the user to a login page.
    * If a logged-in user happens to navigate to the homepage, these links revert to simply **'Buy'** (which redirects straight to the **'Browse products'** listings page) and **'Sell'** (which redirects straight to the **'Sell your product'** form page).

3.  Buyer login page
    * If either of the username or password fields are left blank, a warning message appears saying 'Please fill in this field'.
    * If invalid account details are entered, the message 'Your username or password is incorrect' appears.
    * If login is successful, the user is taken directly to the **'Browse products'** page in order to begin shopping, accompanied by a message of 'You have successfully logged in!'.
    * The 'Forgotten your password?' links redirects to the **'Password reset'** page.
    * The 'you can register here' link redirects to the **'Create new account'** page.

4. Seller login page
    * If either of the username or password fields are left blank, a warning message appears saying 'Please fill in this field'.
    * If invalid account details are entered, the message 'Your username or password is incorrect' appears.
    * If login is successful, the user is taken directly to the **'Sell your product'** page so they can list a product for sale, accompanied by a message of 'You have successfully logged in!'.
    * The 'Forgotten your password?' links redirects to the **'Password reset'** page.
    * The 'you can register here' link redirects to the **'Create new account'** page.

5. Contact page
    * If any of the fields are left blank, a warning message appears saying 'Please fill in this field'.
    * When all the contact form fields have been completed and the user hits 'Send', they are redirected to an **'Email confirmation'** page accompanied by a message of 'Your message has been sent and we will reply to you as soon as possible, many thanks!'.

This is a screenshot of a successfully sent and received email. The 'from' address of stuartrichardsdigital@gmail.com is the EMAIL_HOST_USER as defined in the Django *settings.py* file. This is why users are asked on the original contact form to enter their email address as part of the message.

![alt text](https://i.imgur.com/93seeRa.jpg "Email screenshot")

6. Recipes pages
    * User-submitted recipes are correctly displayed with a title and thumbnail image.
    * Clicking on a title takes the user to a specific recipe page, where the ingredients and method are shown.
    * Clicking on the link next to the 'add your own recipe' text takes the user to an **'Add your recipe'** form.
    * The **'Method'** text area is correctly filled in with the default text '1)', with the aim of encouraging the user to have numbered preparation and cooking steps in their recipe method.
    * If any of the fields are left blank, a warning message appears saying 'Please fill in this field', or 'Please select a file' in the case of the image upload field.
    * Once all fields are completed and 'Save' is clicked, the user is redirected to the main **Recipes** page, where their new recipe is automatically listed and has its own page with ingredients/method.

7. Registration page
    * The email field requires '@' in the address.
    * If there are any field requirement failures for Username, Password or Password confirmation, the registration process fails and a message appears saying 'Sorry, we were unable to register your account at this time, please check for error messages below'.
    * If all the form field requirements are met, the new user is registered and a message appears saying 'ou have successfully registered and have been automatically logged in'.

8. Product listings page
    * Products are correctly listed with a thumbnail image, name, description and price.
    * Numbers can be entered into a product's **'Quantity'** field either manually or by using the up/down arrows functionality.
    * When the user clicks **'Add'**, a yellow number badge appears beside the **Cart** link on the navbar. There is also a message saying 'The product has been added to your cart'. This is repeated for each item added to the cart.
    * Product listings also contain *'Edit this product'* and *'Delete this product'* links. These are only visible to the logged-in user who created the product object in the first place.
        * Clicking **'Edit this product'** takes the user back to the **'Sell your product'** form page, with all the fields pre-filled with their original product details. The user can make changes to any of the fields, hit 'Save' and then be returned to the **'Browse products'** page where their edited product can be seen.
        * Clicking **'Delete this product'** takes the user to a page where they are asked if they wish to confirm deletion or return to the main products page. Clicking 'Delete' returns them to the **'Browse products'** page where their item has now been removed.

9. Sell your product page
    * If any of the form fields are left blank, a warning message appears saying 'Please fill in this field', or 'Please select a file' in the case of the image upload field.
    * When all form fields have been completed and the user hits 'Save', they are redirected to the **'Browse products'** page where their new listing can be found.

10. Shopping cart page
    * 

11. Checkout page

12. Password reset

The site was manually viewed and tested in the Chrome and Firefox browsers on a Windows 10 laptop, as well on iOS and Android mobile/tablet devices.

This was done with a view to ensuring that: all functions and interactivity respond appropriately on both mobile and desktop; responsive changes in the navbar and site layout are all present and correct for different devices; and the site remains fully functional, useable and well presented across all screen sizes.

I also ran my code through the W3C validator tools for HTML/CSS, as well as JSHint for Javascript and http://pep8online.com for Python.

Travis and tests.py x2
**'Profile'** pages currently contain repetition of items, i.e. if a user bought a product called 'Carrots' on two occasions then this would be displayed twice on their profile, which is a scenario that needs to be addressed.

## Django database details?

## Deployment

* I created a new app in Heroku called *kerry-online-farmers-market* with the region selected as 'Europe'.
LOTS MORE TO COME IN HERE!
* I then clicked 'Open app' and my website was deployed live to https://kerry-online-farmers-market.herokuapp.com.

## Credits

### Content

* For specifying the *login_required* redirect URL in the *checkout* function of *checkout/views.py* - https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django.
* For using *DeleteView* to delete objects - https://www.youtube.com/watch?time_continue=105&v=Go1yHB00hl8.
* For the *models.py* and *forms.py* in my *contact* app, I referred to https://wsvincent.com/django-contact-form.
* For a message saying 'your cart is empty' when there are no shopping cart items, I referred to [this documentation](https://books.google.ie/books?id=LwO1GzMN_QsC&pg=PA96&lpg=PA96&dq=django+shopping+cart+no+checkout+if+empty&source=bl&ots=_ocGe9GF6C&sig=ACfU3U1fXQ2O_oiZyvsDp246YqZJjkt8fQ&hl=en&sa=X&ved=2ahUKEwiKkcTgrtPoAhXCUBUIHeChDp8Q6AEwA3oECAwQKg#v=onepage&q=django%20shopping%20cart%20no%20checkout%20if%20empty&f=false) .
* For running tests on Django forms - https://realpython.com/testing-in-django-part-1-best-practices-and-examples & https://www.youtube.com/watch?v=zUl-Tf-UEzw.
* For getting *'background-attachment:fixed'* to work on iOS devices - https://stackoverflow.com/questions/26372127/background-fixed-no-repeat-not-working-on-mobile.

### Acknowledgements

Thank you to the people of **Kenmare Community Chat** on Facebook for the original idea of an online farmers market. And to my project mentor Aaron Sinnott for his enthusiasm, advice, guidance and encouragement.