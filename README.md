# RetroKings

<hr>

### Code Institute / Full Stack Frameworks with Django Milestone Project

Tasked to create a website combining knowledge from the Full Stack Frameworks with Django Development modules on the Code Institute course.

## Introducing you to
<p align="center">
  <img width="350" height="350" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/logo/RetroKingsLogo.png">
</p>

## The Idea

This Milestone project creation is the culmination of learning and study from all modules of the Full Stack Developer Course from Code Institute, culminating in the creation of this Full Stack Framework Django project. For this project i decided to build an e-commerce store that allows an admin to store and manipulate data records and also allows them to create, read, update & delete items from the store. 

RetroKings is your one stop shop for all retro Soccer, NBA, NFL & MLB jerseys.

Please ensure when testing payments in this application to use the Stripe test card numbers available [here](https://stripe.com/docs/testing#cards) from the Stripe documents. Throughout development of the application the card number used by myself and others was:

- <strong>Card number:</strong> 4242 4242 4242 4242
- <strong>Expiry date:</strong> Any date in the future
- <strong>CV2 number:</strong> Any 3 digits
- <strong>ZIP:</strong> 42424

<hr>

<a href="#">Back to top</a>

## Table Of Contents

<hr>

<a href="#">Back to top</a>

## UX

<hr>

### Business Goals:

The business goals of RetroKings:

- To sell the highest quality authentic retro jerseys.
- To engage, promote and sell across all social media platforms.
- Increase visits per month to the webpage.
- Be the no.1 store to purchase authentic retro jerseys from.

### User Stories:

###### As the developer:

1. As a Developer, I want to showcase my growing abilities as a Full Stack Software developer during my time on the Code Institute course.

2. As a Developer, I want a project that I can proudly showcase to potential employers via my Github Repository.

###### As the admin:

1. As the site administrator, I want to be able to login to an administration panel.

2. As a Site Administrator, I want to have the ability to update site content, such as add, remove and delete store products.

###### As a customer:

1. I want to browse a range of retro jerseys on the site.

2. To be able to view an in depth detail about the product i wish to purchase.

3. For the products in the store to have a rating

4. I want to be able to create a user account so that it will store previous purchase history.

5. Make a purchase on the site by way of card payment.

6. Leave a review for the item i purchased.

7. A way to contact the company with any issues or questions i may have. 

8. For the site to have an FAQ page that may answer my queries efficently withouth always needed to contact the store.

9. Terms & Conditions must be available to a user so that they have a clear view of their entitlements on returns etc.

10. As a user I want to view the site from any device (mobile, tablet, desktop).

<a href="#">Back to top</a>

## Design
 
<p align="center">
  <img width="1200" height="500" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/mockup.jpg">
</p>

<hr>

The design process is the one i enjoy the most. I enjoy learning new ways to style my projects and I feel more and more that Front End Development in particular the design aspects of it is my calling in this profession. I have enjoyed designing all of my projects but this is the one i have enjoyed the most as i have really seen over the course how i have improved in this aspect. I have tried to take on new challenges in all of my milestone projects and not be repetitive when it has come to the design of each one. 
I enjoy it all from deciding on the colour schemes to the layouts of the pages etc, and i really feel this is how you entice the user and convince him to browse your site.

### Font

The main font i chose for this site was 'Old Standard TT' from [Google Fonts](https://fonts.google.com/specimen/Old+Standard+TT?preview.text=Retro%20Kings&preview.text_type=custom&query=old+#standard-styles) In keeping with the theme of the site Old Standard reproduces a specific type of Modern (classicist) style of serif typefaces, It keeps in line to the type of vintage/classic products we have on offer. The font is clear with clean lines and reads well.

'Sans-Serif' is used as the default backup font in cases where these fonts have difficulty loading. 

### Colour Scheme

To help me choose my color scheme i used [Adobe Color Wheel](https://color.adobe.com/create/color-wheel).

This process took a long time during the wireframe stage. In the end i decided on this color scheme as it is quite vivid and bright. The gold gives it a very vivid feel and helps to highlight important points against the white backdrop and at the same time it gives the website a bold feel with the added contrast of the color black. I also used white with a mix of a gold gradient to just break the page up from being a standard white background on certain areas such as products cards, FAQ page etc.

Three primary colors were chosen when creating this project:

- ![#d4af37](https://placehold.it/15/d4af37/000000?text=+) `#d4af37` 
- ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000` 
- ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff`

The three colours are featured heavily across the site.

The navbar header is colored in ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff`, which offered a bright background to the logo and the searchbar. I used 
![#000000](https://placehold.it/15/000000/000000?text=+) `#000000` to highlight the nav-links i surround them by a background of ![#d4af37](https://placehold.it/15/d4af37/000000?text=+) `#d4af37` and also to break up the navbar from the top nav header.

The call to action buttons utilised the same navbar coloring of ![#d4af37](https://placehold.it/15/d4af37/000000?text=+) `#d4af37` as their background with a font color of 
![#000000](https://placehold.it/15/000000/000000?text=+) `#000000` where there is two buttons in view on the same page to highlight the different buttons i reveresed this procedure. When active, focused or hovered on the primary colour buttons of ![#d4af37](https://placehold.it/15/d4af37/000000?text=+) `#d4af37` with ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000` font the main background color of the button was set to reverse of ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000` with ![#d4af37](https://placehold.it/15/d4af37/000000?text=+) `#d4af37` font. The secondary colour buttons of ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000` with ![#d4af37](https://placehold.it/15/d4af37/000000?text=+) `#d4af37` font when active, focused or hovered have been set to ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff` with the font inside being set to ![#d4af37](https://placehold.it/15/d4af37/000000?text=+) `#d4af37` to show the user that this element is interact-able and something will happen when pressed.

To give the website a more colorful feel & to create a better visual experience for the user i added a subtle gradient effect to pages like the products page & the FAQ page etc using white to begin with and then adding the gradient effect working its way into gold.

### Logo

The logo was custom created by myself in photoshop. I wanted to make a bold statement with this design an so it incorporates a crown above the brand name to indicate that we are the kings of retro jerseys. I also incorporated in lines above the crown to give the effect that it is shining bright. It also features the colour scheme of the site keeping everything consistent.

My Logo can be seen in the nav header of my site and it acts as 'Home' button across all pages to ensure consistency throughout the application. This also helps to invoke the brand in the user's mind-eye.

### Background Image

The background image is also custom created by myself in photoshop. I could of used an image from numerous sources but i just couldnt find the one that suited my site theme. This ended up with me putting in several extra hours designing the logo until i was 100% happy with it. I started out by getting individual jerseys and changing the colours of each to that of the site using black and gold as the main colours. I then incorporated them all across in a horizontal line to display the type of sports jerseys we supply. In keeping with this the sports navbar dropdown also goes in the same order.
 
### Wireframes

Wireframing for this project began with Pen and paper as all my projects tend to start, but ultimately Wireframes were created using Balsamiq.

Each element was structurally planned out at this stage and even during the physical build of the application there was not much deviation from the original planning. Each page was rendered as a wireframe in all viewport sizes to show the difference between them and to show how the elements would react to differing viewport sizes.

<a href="#">Back to top</a>

<hr>

## Features

<hr>

This section will outline all the features of RetroKings implemented by page.

This project uses Django 3 in conjunction with Bootstrap 4 to structure and display elements on templates /views to the user. As Django 3 was the recent version of the templating framework, it allowed me to expand on the learning material from the course.

Python 3.8 was also used as the base Python language.

The project is fully responsive and renders on all modern browsers.

HTML, CSS and JS were used to implement the Frontend of the project and Django and Postgres where used to create and control the backend. Stripe was used to control the credit card payments and Stripe library errors.

The project boasts several key features a quick summary is below:

- User Authorisation, Authentication and Logout Features
- CRUD Functionality for the admin of the site itself.
- Amazon S3 bucket is used to host images and then passed into urlfield to render it to the template.
- Stripe Integration to allow for e-commerce functionality.
- Toast messages features all across the site to give the user feedback everytime they add or remove items from the cart or on completion of checkout etc.
- A contact form that can be utilised by public/authenticated users, which sends an email to the Administrator of the application, notifying them of a new contact form submission. For testing purposes this is currently set up to come to myself as the developer but can be changed at a later stage to the admin/owner of the site.
- Numerous user feedback such as hover on buttons and mouse over zoom on the homepage large category pictures.

### Base Template
 
###### Navbar Header
 
- The navbar header contains the search functionality of the website while the brand logo in the top left acts as a home button to bring the user back to the home page.
 
- A logged out user can access the registration page or log in page through the user icon.
 
- A logged in user can access their profile dashboard or log out through the user icon.
 
- The user can view a price summary of their current orders underneath the bag icon. Clicking on the icon will bring them to their bag for a more detailed view.

<p align="center">
  <img width="100" height="100" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/bag-icon.jpg">
</p>
 
###### Navbar
 
The navbar links feature in the centre of the navbar itself. I have 4 links in total:-

- All Jerseys (Navigates to all products in the store except the clearance items dont appear as i wanted to keep these separate).
- Sports (When clicked dropdown appears to give the user an option to browse by which sports category they would like).
- Headwear (When clicked dropdown appears this will also be referenced in my future developments).
- Special Offers (When clicked dropdown appears to show an option to view the stores clearance items).

Intuitive navigation fixed to the top of the the page that resizes for mobile devices with the hamburger icon. When pressed it expands to show the other navigable pages. On desktop when the user hovers over the nav-links the icon changes so that will show the user that this is interact-able and something will happen when clicked.

###### Custom Scrollbar

I created a custom scrollbar for my site to give it another level of customization and to move away from the standard scrollbar you see on most sites. This is also a new feature i implemented for this project as i have not incorporated this on any previous milestone projects.
 
###### Footer

The Footer contains all navigation links for easy website navigation. It also contains our Privacy Policy, Terms & Conditions & FAQ pages. Contained inside the footer is also a link to our contact information and a link to our store contact form. The shopping bag page does not feature the footer as i felt it was not good UX having to much information on that part of the screen. To do this i wrapped the footer in an empty block content of {% block footer %}{% endblock %}.
 
### 🏠 Home Page

The home (Index) page is our primary landing page.

###### Background Image

The Home Page features my custom background image and a large header. Right underneath the header you will find a small description of the store and a button which will bring you to the all products page.

<p align="center">
  <img width="500" height="200" src="https://github.com/Jmurray1989/RetroKings/blob/master/media/jersey-home-background.jpg">
</p>

###### Category Cards

It also features six large cards with images of jerseys placed inside them to indicate the different categories of sport you can browse by. When these cards are hovered over the images zoom in to indicate to user that the are interactable. 

###### Image Carousel

Below the category cards i have an image carousel displaying old photographs of some of the sporting events associated with the categories we cater for and to give the site a more vintage feel.
 
### 📝 Sign Up Page

###### Registration Form

- A user who is not logged in can create a new account using the register page where they must provide an email address, a username (which must be unique) & a password.
- The form was created using Django Crispy Forms.
 
### 🔑 Login Page

The login page itself was kept simple with some text and two input fields where the user must input there log in details of username or email & password. It also has two buttons 'Home' & 'Sign In' coloured in the theme of the site. Both buttons also contain a hover effect to indicate they are interactable to the user.

###### Log in form

- A user who is registered can log in using their username and password.
- The form was created using Django Crispy Forms.
 
### 🏬 Products Page

###### Sort By

The product listings page includes the option to sort its results by:

- Price - low to high
- Price - high to low
- Name - a to z
- Name - z to a
- Category - a to z
- Category - z to a

###### Category Filter

Underneath the products header are a list of categories that the user can use to browse by that category.

- Users can filter by the sports they wish to browse for example.

###### Products Listing

Products in the shop are displayed as thumbnail images with the product title category tag and price broken up by a horizontal line.

- Each individual product image has had its background removed (which took some time to complete) so the gradient would be much cleaner.
- When the user clicks on a product card, they are taken to the product details page of that selected product.
- If the admin is logged in, they have the rights of access to add, edit or delete a products from the store.

### 📃 Products Detail Page

This page gives an in depth view of the product with a small description about the product they are looking at. It also has a size selector box and a quantity selector box and features both 'Keep Shopping' and 'Add To Bag' buttons again styled with the theme of the website. These buttons like most buttons on the site contain a hover effect to let the user know they are interactable.

###### Listing Details

- Each product detail page features an image of the product on sale.
- The product title, price, product rating, user review counter, category tag and a brief description are all clearly visible on the product listing page to the right of the image.
- Almost all products require sizing information. If applicable, there is a size dropdown selector to allow users to choose their size. On one off items for example a Chicago Bulls jersey worn by Michael Jordan does not feature a size dropdown selector box.
- A numeric input selector allows the user to select the quantity of a product they wish to purchase. The minimum product quantity a user can purchase is 1, with the maximum being 99.
- Users can add a product to their cart by clicking the "Add to cart" button or continue shopping by clicking the "Keep shopping" buttons.

###### Toast Notifications

Toast notifications are used across the site to give the user feedback in various ways. In the product details page when the user clicks on the add to cart button they are give a toast notification informing them that they have added an item to the bag.

- When a user selects a product, they are notified of their selection through a success toast message.
- They are then given the option to go to the checkout to purchase the item or close the box to keep shopping.
 
### ⭐ User Reviews

###### Leaving a Review

- To leave a review on a product, a user must be logged in and purchase an item.
- The review form becomes available on the product details page after the item has been purchased.
- Customers who purchased the item can leave a comment and a rating in the form of a star rating which will be displayed under their comment.
- The review is published immediately and is viewable at the bottom of that products details page.
- The user while logged in can also choose to re-edit their review or remove it completely. Keeping in with the CRUD functionality.

<p align="center">
  <img width="7000" height="300" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/product-review.jpg">
</p>

###### Toast Notifications
- Toast notifications also operate on this page informing the user they have posted, edit or deleted their review.

<p align="center">
  <img width="300" height="200" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/update-review.jpg">
</p>
 
### 👤 User Profile Dashboard

The user profile dashboard contains the default deliver information for the user while showing their order history on the right hand side.

###### Billing details

- The users profile page can only be accessed by a logged in user.
- The account page contains the user's billing information that they can edit and update. This billing information will automatically be included in the checkout process to save time for the user.
- An order summary is visibile if user's have made a purchase in store. This will contain:
1. Order number
2. Date an item was purchased
3. Item(s) purchased
4. Order total

###### Toast Notifications

When a user updates their billing information they are notified of this change through a success toast message.

<p align="center">
  <img width="300" height="150" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/profile-updated.jpg">
</p>
 
### 👜 Shopping Bag

The shopping bag page features a summary of all the items the user has added to their shopping cart.

- Each item includes an image, product name, size (if applicable) SKU and price.
- The user has the ability to adjust the quantity in their cart. A user can also remove an item from their cart. When the quantity is updated. the subtotal will reflect the change.
- Cart total, delivery total and grand total of the user's cart are reflected in the order summary.
- An arrow button features at the bottom of the bag page to return the user to the top of the page. This was implemented mainly for mobile devies but i have included it across all devices as when a user adds a few items to the bag it can make it quite long on the user to have to scroll back up to the top of the page.
- The 'Secure Checkout' button proceedsto take the user to the payment screen operated by Stripe.
- To show the user the site has a secure payment facility we have included an image below the 'Secure Checkout' button.

<p align="center">
  <img width="500" height="150" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/security/img-security.png">
</p>

###### Toast notification

When a user adds an item to their cart, a toast notification displays with the item information.

- A user is notified of the free delivery threshold and how much more they would need to spend to get free delivery.
- A 'Go To Secure Checkout' button is displayed below the item information to take the user to the checkout screen.

<p align="center">
  <img width="300" height="300" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/bag-toast.jpg">
</p>
 
### 💳 Checkout Page

The checkout page features a checkout form on the left and on the right again it shows them their order summary in a detailed view with pictures etc.

###### Checkout form

- The checkout page features a form that needs to be filled out by the user.
- If this is a logged in user's first time to check out, they need to fill out their billing information.
- Details required are name, address, email address, street address, town/city, postal code, county/state/locality and country which is a selector box for ease of use.

###### Stripe

- Users can complete the checkout process by entering their card details.
- Payment is handled though the secure Stripe API.
- Once a user clicks to buy, a custom loader appears while the payment is processing and if a successful payment is made, the user is taken to the checkout success page.

###### Checkout success

- An order confirmation email is then sent to the email provided by the user which contains all the information of their purchase(s).
- The checkout success page gives the customer all their order information.
- An order number is automatically generated on checkout.
- The user is invited to check out our deals page after checkout.
 
### 📧 Contact Page
 
 The contact page features a form where by the user con contact the store if they have any queries that cannot be answered by our FAQ section. The make the contact form standout from the back is used a dropshadow effect in the colour gold keeping in with the color scheme of the site which can be viewed [here]().
 
###### Contact form

- The contact page contains a form for the user to fill in to send to the store admin.
- Name, email address and message have all been set to required fields.
- An email is sent to the store admin's email address notifiying them of a new contact enquiry in the admin dashboard.
- This message can be checked by logging in to the admin area. Preview it [here](https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/contact-form.jpg).
- After the user submits the form a 'Thank You' message is displayed informing them we will be in touch soon and that they can continue to shop our store by clicking on the 'Take Me Shopping' button while they wait.

###### Toast notification

- When a contact form has been successfully submitted, the user is notified via toast message.

<p align="center">
  <img width="350" height="150" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/toast-message.jpg">
</p>
 
### Features Left to Implement

These are a list of future features i would like to incorporate into the site. Unfortunately due to the time constraints placed on me during the course i did not have enough time to complete the list below.

###### Social Sign Up

- On the register page i would like to give the user the option to login with their social account details.

To implement this idea i would go to the Facebook developers page and create my app to link with Facebook. Django allauth comes pre-installed with templates for setting up social login.

###### Discount Codes

- I'd like to include a field for customers to enter discount codes that adjust the final cost of the shopping cart.

###### Two Step verification

- With cyber crime on the rise this is a new trend that a lot of social providers and banks are using so i would like to implement this as an added layer of security for the users of my site.

###### User Rating

- I have implemented user reviews on the site to include a star rating system. I would like to take this information so everytime a user leaves a review on a product an average rating would appear based on that review.

To implement this idea would be quite complex and a challenge i would like to take on. The steps below are how i believe i would achieve this feature.
- Once a review has been saved
- Pull reviews of product from reviews DB
- Find the sum of all of the reviews
- Divide the sum by the number of reviews of product
- Write this number into the review field of the ProductModel

<a href="#">Back to top</a>

<hr>

## Database

<hr>

The database used for this Project was Postgres, as an Installed add-on to the deployed Heroku Application. During development in gitpod Sqlite3 was used to test the User Authentication, Registration & Login, and for testing the creation of products and reviews for the store. On deployment Postgres was used from that point on.

### Database Models

When each app and its models were created and implemented, python manage.py makemigrations was run in the terminal to create the initial model package and python manage.py migrate was then used to apply the model to the database and create the table.

All models were created with Django's ability to auto-assign a Primary Key (ID).

###### User Model

The User model used is the standard one provided by Django.

###### Category Model

| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
| Name        | max_length=250     | Charfield   |
|Friendly Name|models.CharField(max_length=254, blank=True)             | Charfield      |

###### Product Model

| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
| Category        | null=True, blank=True, on_delete=models.SET_NULL     | ForeignKey   |
| Sku        | max_length=254, blank=True     | Charfield   |
|Name|max_length=254             | Charfield      |
| Description       | blank    | TextField  |
|Has Sizes| blank | BooleanField     |
| Price        | max_digits=6, decimal_places=2     | DecimalField   |
|Rating|max_digits=6,decimal_places=2, null=True, blank=True | DecimalField      |
| Image Url        | max_length=1024, blank=True     | UrlField   |
|Image|blank=True | Image Field      |

###### Order Model

| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
|Order Number|max_length=32, null=False, editable=False| Charfield   |
|User Profile|on_delete=models.SET_NULL,null=True, blank=True, related_name='orders'|ForeignKey|
|Full Name|max_length=50, null=False, blank=False| Charfield   |
|Email|max_length=254, null=False, blank=False|EmailField|
|Phone Number |max_length=20, null=False, blank=False| Charfield   |
|Country|blank_label='Country *', null=False, blank=False|CoutryField|
|Postcode|max_length=20, blank=True| Charfield   |
|Town or City|max_length=40, null=False, blank=False| Charfield      |
|Street Address 1|max_length=80, null=False, blank=False| Charfield   |
|Street Address 2|max_length=80, blank=True| Charfield      |
|County|max_length=80, blank=True| Charfield   |
|Date|auto_now_add=True| DateTimeField |
|Delivery Cost|max_digits=6, decimal_places=2, null=False, default=0| DecimalField   |
|Order Total|max_digits=10, decimal_places=2, null=False, default=0| DecimalField      |
|Grand Total|max_digits=10, decimal_places=2, null=False, default=0	| DecimalField  |
|Original Bag|null=False, blank=False, default=''| TextField|
|Stripe Pid|max_length=254, null=False, blank=False, default=''| Charfield      |

###### Order Item Model

| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
|Order|null=False, blank=False, on_delete=models.CASCADE,related_name='lineitems'| ForeignKey  |
|Product|null=False, blank=False, on_delete=models.CASCADE| ForeignKey |
|Product Size| max_length=2, blank=True XS, S, M, L, XL| CharField   |
|Quantity | null=False, blank=False, default=0 | IntegerField |
|Line Item Total| max_digits=6, decimal_places=2, null=False, blank=False, editable=False|Decimal Field|

###### Review Model

| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
| Product     |on_delete=models.CASCADE, null=True, blank=True, related_name="reviews"| ForeignKey  |
|User         |on_delete=models.CASCADE,null=True, blank=True, related_name="reviews"            | ForeignKey |
|Comment      | max_length=1000, blank=True| TextField   |
|Rating| default=1 | IntegerField |

###### Contact Model

| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
| Name        | max_length=200    | Charfield   |
|Message|max_length=200, blank=True| TextField      |
| Email        | max_length=200    | EmailField   |
|Contact Date|default=datetime.now, blank=True)| DateTimeField      |
|User Id|null=True, on_delete=models.CASCADE| ForeignKey     |

<a href="#">Back to top</a>


<hr>

## Technologies Used

<hr>

##### Languages, Frameworks, Libraries & Version Control:

###### HTML, CSS, JS & Python

* core languages used to create this multi-page CRUD application.

[Django](https://www.djangoproject.com/)  

* Used as the architectural engine following the model-template-view approach.

[Sqlite3](https://www.sqlite.org/index.html) 

* Database used in development comes preinstalled with Django.

[PostgreSQL](https://www.postgresql.org/)

* A free and open-source relational database management.

[Django Aullauth](https://django-allauth.readthedocs.io/en/latest/)

* Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

[Bootstrap](https://getbootstrap.com/)

* Used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.

[Bootstrap's Imported Javascript & JQuery](https://getbootstrap.com/)

* For the Responsive Navbar expand & collapse functionality.

[Gitpod](https://gitpod.io/)

* IDE of choice for this project.

[Github](https://github.com/)

* Used to host the repository of all previous versions of the build and linked to Heroku to push the latest changes to the deployed build version held there.

[Heroku](https://id.heroku.com/login)

* A cloud platform as a service enabling deployment for this application.

[Stripe](https://stripe.com/en-ie)

* Used to handle checkout payments.

###### Tools Used:

[Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

* Used to test the application's functionality, the responsiveness, and the CSS visualisation.

[Balsamiq](https://balsamiq.com/wireframes/)

* Used for the creation of my pre-build wireframes showing the main elements and differences in size of same through small to large screen sizes.

[Favicon Generator](https://www.favicon-generator.org/)

* Used to create favicon from custom Logo I created for the project.

[W3C Mark-up Validation](https://validator.w3.org/) and [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

* Used to check the validity and efficiency of my code.

[JSHint](https://jshint.com/)

* Using JSHint to validate the project's Javascript

[Django Extensions Plugin](https://django-extensions.readthedocs.io/en/latest/)

* For validating my templates for any jinja rendering errors.

[Autoprefixer CSS Online](https://autoprefixer.github.io/)

* Used to check for possible webkits required in the applications stylesheet ensuring Cross-browser support.

[PEP 8 Online Validator](http://pep8online.com/)

* To validate my python code to be consistent with PEP8 requirements.

[AWS S3](https://aws.amazon.com/?nc2=h_lg)

* Used to store external media and static files.

[Font Awesome Icons](https://fontawesome.com/)

* For social icons used in Footer and Iconography present throughout site.

[Adobe Colour Picker](https://color.adobe.com/create/color-wheel)

* Helped me to choose the colour scheme of the website.

[Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html?gclid=CjwKCAjww5r8BRB6EiwArcckC_fXdr_HQcxAW69oogvaq1DMY2UcB9-u8qhJEkKpt02pvonpc1YtlhoCMJgQAvD_BwE&sdid=88X75SKS&mv=search&ef_id=CjwKCAjww5r8BRB6EiwArcckC_fXdr_HQcxAW69oogvaq1DMY2UcB9-u8qhJEkKpt02pvonpc1YtlhoCMJgQAvD_BwE:G:s&s_kwcid=AL!3085!3!441704131147!e!!g!!photoshop!1423511192!58810496314)

* Used to crop, re-size, editing and to custom create my images.

[Image Background Remover](https://www.remove.bg/)

* Used to remove the backgrounds of my jersey images.

[Google Fonts](https://fonts.google.com/)

* Helped me to choose the font for my site.

[Tinypng](https://tinypng.com/)

* Used to resize my images

<hr>

## Testing

<hr>

Manual testing was my preferred choice for this project as it has been the case with all my projects.

The website has been tested across multiple browsers and on mobile devices to ensure compatibility and responsiveness of the site. Continuous testing for this application was carried out throughout the entire lifetime of the build. This was achieved through Chrome Devtools and it was used constantly to test on as many devices as possible from Android to Apple phones & tablet dimensions, and also larger device sizes. The website was tested constantly throughout the build at home using devices i had on hand.

###### Browsers

- Chrome
- Firefox 
- Safari 
- Microsoft Edge 
- Opera

As Safari is no longer developed for Windows I used a site known as [LambdaTest](https://accounts.lambdatest.com/register) to run my code in a live view for mac and safari software. It returned a few errors however as this is not official software i cannot be sure the results given are accurate. When I tested my project through chrome and other browsers on this site it showed me errors which i do not have on these browsers when ran locally.

###### Devices

- Samsung Galaxy S10 & S8 
- Xiaomi Redmi Pro 8
- Amazon Fire HD 8.

If a bug arose during testing it was dealt with during the build of the project. The build and the fix where then pushed to the repository for the latest changes to take affect on the deployed application via automatic build & deploy function set up in Heroku.

I used W3C Mark-up Validation and W3C CSS Validation to validate my html and css code. Unfortunately the W3C Validator for HTML does not understand the Djangos templating syntax, so it therefore shows a lot of errors with regards to url paths {% url 'example' %} {{ variables }}, {% block %} {% endblock %}, etc. Aside from the these warnings and errors, all of the remaining code is perfectly validating.

I stumbled across this collection of custom Django Extensions where by I could pip install it to the project and add it to the INSTALLED_APPS to enable it for use within the project. Running python manage.py validate_templates command in the terminal allowed me to check all templates for rendering errors of which there were none. Using this coupled with the HTML Validator allowed me to fully check my templates for any errors, if any existed at time of inspection. 

I used JSHint to validate the project's Javascript file which i configured to accept jQuery & ES6 New JS features, It returned 0 warnings.

I used PEP8 online to make sure my Python files are compliant to current standards.

###### Manual Testing Log:

The log provided below also answers user stories from above.

| Functionality      | Browser | Pass / Fail    |
| :---        |    :----:   |          ---: |
|User can open application via Heroku deployed link?|Chrome/Opera/Edge/Safari/FireFox	| Pass |
|Homepage loads for the user|Chrome/Opera/Edge/Safari/FireFox| Pass|
|Favicon loads in browser tab| Chrome/Opera/Edge/Safari/FireFox|Pass|
|All nav links operate correctly|Chrome/Opera/Edge/Safari/FireFox| Pass |
|All buttons operate correctly| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Jersey category cards bring the user to the correct category| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Carousel images display and operate correctly| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Users can browse the store and display the product details page| Chrome/Opera/Edge/Safari/FireFox|Pass|
|User can add items to the shopping bag| Chrome/Opera/Edge/Safari/FireFox|Pass|
|User can updated quantity and remove products from the bag| Chrome/Opera/Edge/Safari/FireFox|Pass|
|User can register for account using the form| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Once registered the user can login to view their personal dashboard| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Logged in users can leave reviews on products purchased| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Logged in users can edit their reviews or remove them if they wish| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Toast messages operate as required to inform the user of different actions they have performed| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Public user cannot leave a review if they purchase an item| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Users can contact the store by way of contact form| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Custom error pages show when required (404 & 500)|Chrome/Opera/Edge/Safari/FireFox|Pass|
|Footer displays correctly|Chrome/Opera/Edge/Safari/FireFox|Pass|
|User can checkout successfully| Chrome/Opera/Edge/Safari/FireFox|Pass|
|All form fields behave as expected| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Toast messages operate as required to inform the user of different actions they have performed| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Admin can add or remove products to the store as required| Chrome/Opera/Edge/Safari/FireFox|Pass|
|A public or logged in user cannot add or remove products to the store| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Admin can access the dashboard and view messages submitted from the contact form| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Users can view our FAQ, Privacy Policy and Terms & conditions pages in the footer| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Logged in users can logout successfully| Chrome/Opera/Edge/Safari/FireFox|Pass|
|Reset password link operates as expected| Chrome/Opera/Edge/Safari/FireFox|Pass|
|The site scales up and down depending on viewing device| Chrome/Opera/Edge/Safari/FireFox|Pass|

###### Lighthouse Report

I ran the lighthouse report to check the performance of my site and accessibility for screen readers see reports below:

###### Desktop

<p align="center">
  <img width="450" height="175" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/Desktop-LighthouseReport.jpg">
</p>

###### Mobile

<p align="center">
  <img width="450" height="175" src="https://github.com/Jmurray1989/RetroKings/blob/master/static/readme-imgs/Mobile-LighthouseReport.jpg">
</p>

<hr>

### Known Issues

I found a couple of css issues with regards to some browsers i tested. These are layed out below.

###### Mozilla Firefox

1. Not all hr elements take on the color effects i implemented.
2. My product reviews star field is not coloured.
3. My dropshadow effect on the contact form did not take effect on this browser.

I have not found any other issues.

<a href="#">Back to top</a>

## Deployment

<hr>

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

<a href="#">Back to top</a>


## Credits

<a href="#">Back to top</a>

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

<a href="#">Back to top</a>

### Media
- The photos used in this site were obtained from ...

<a href="#">Back to top</a>

### Acknowledgements

- I received inspiration for this project from X

<a href="#">Back to top</a>
