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

<a href="#top">Back to top</a>

## Table Of Contents

<hr>

 <a href="#top">Back to top</a>

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

[Back to top]()

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

[Back to top]()

## Features

This section will outline all the features of RetroKings implemented by page.

This project uses Django 3 in conjunction with Bootstrap 4 to structure and display elements on templates /views to the user. As Django 3 was the recent version of the templating framework, it allowed me to expand on the learning material from the course.

Python 3.8 was also used as the base Python language.

The project is fully responsive and renders on all modern browsers.

HTML, CSS and JS were used to implement the Frontend of the project and Django and Postgres where used to create and control the backend. Stripe was used to control the credit card payments and Stripe library errors.

The project boasts several key features a quick summary is below:

- User Authorisation, Authentication and Logout Features
- CRUD Functionality for the admin of the aite itself..
- Amazon S3 bucket is used to host images and then passed into urlfield to render it to the template.
- Stripe Integration to allow for e-commerce functionality.
- Toast messages to give the user feedback everytime they add or remove items from the cart or on completion of checkout etc.
- A contact form that can be utilised by public/authenticated users, which sends an email to the Administrator of the application, notifying them of a new contact form submission. For testing purposes this is currently set up to come to myself as the developer but can be changed at a later stage to the admin/owner of the site.
- Numerous user feedback such as hover on buttons and mouse over zoom on the homepage large category pictures.

 ### Base Template
 
 ### Home Page
 
 ### Sign Up Page
 
 ### Login Page
 
 ### Products Page
 
 ### Products Detail Page
 
 ### User Reviews
 
 ### User Profile Dashboard
 
 ### Shopping Bag
 
 ### Checkout Page
 
 ### Contact Page
 
 

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
