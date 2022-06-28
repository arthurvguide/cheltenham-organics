
BUGS FOUND:
Slidebar does not work properly on aulth pages
Delivery banner and footer horizontal scroll
- Heroku wasnt posting to S3, just receiving 
Product details:
- maybe remove image url or host imgs on cloud

# [Cheltenham Organics](#)
![](#)

 Cheltenham Organics is an ecommerce web application for customers seeking to purchase organic food online.

 You can test the card payment functionality without making a purchase. 

 Use card details for it: 4242 4242 4242 4242 - CVC and 5-number postal code at the end of the card can be any numbers.

 
 [Click here](https://cheltenham-organics.herokuapp.com/) to visit the deployed site.

To access admin, click [here](https://cheltenham-organics.herokuapp.com/admin/)
- User: Organics
- Password: NoneOrg123

---

# Table of contents
1. [Agile Workflow](#agile-workflow)
2. [Business Strategy](#business-strategy)
2. [Owner/Admin Stories](#owner/admin-stories)
3. [User Stories](#user-stories)
4. [Structure](#structure)
5. [Features](#features)
    1. [User Features](#user-features)
    2. [Owner/Admin Features](#owner/admin-features)
6. [Technologies Used](#technologies-used)
    1. [Main Tech](#Main-Tech)
    2. [Applications and Platforms](#applications,-libraries-and-platforms)       
7. [Validation](#validation)
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Credits](#credits)

## Agile Workflow

![](#)
I've tried to implement the basic Agile strategy, creating issues for my user stories, a Kanban board for the project, Milestones for each epic and moving the stories from TO DO to, PROGRESS to DONE.

As Github is limited with ways to do this, I have chosen to have the Milestones as Epics instead of sprints in this project.
The Kanban board can be viewed [here](https://github.com/arthurvguide/cheltenham-organics/projects/1).

[Back to Table of contents](#table-of-contents)

## Business Strategy

### Business Model

I chose a traditional B2C app, which has a simple and user-friendly interface. This online store offers self-made products (organic food). Products are collected from their land and then offered for sale on the website. With delivery charge of just £2 nationwide (UK).

The business flow is as follows:

 1. Cheltenham Organics produces its organic foods.

 2. The website handles the selling of products to the website user.

The intentions should be obvious and users should know as soon as they enter the site what it offers and how to use it's features.

### Marketing

This site has a Facebook Business page with a link on the page footer. 

Upon registering for an account, customers can check a box to receive news and offers through email via Mailchimp.

Upon registering, the user ir redirected to a new page confirming their subscription. The site owner can now see the new subscriber on their audience dashboard, and new campaigns will be sent to them too.

### Search Engine Optimisation

I have generated a sitemap.xml and robots.txt file, and only included relevant canonical links which help Google map the pages of the site.

## User Stories

### EPIC - REGISTRATION AND USER ACCOUNTS

####  USER STORY: Register an account

- As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits.

####  USER STORY: View profile

- As a logged-in user, I can view a profile page, so that I can view my previous orders, and view, update or remove my delivery and contact details.

####  USER STORY: Email confirm upon signing up

- As a user, I have to confirm my email address to complete my account registration.

####  USER STORY: Recover Password

- As a user, I can easily recover my password in case I forget it, so that I access my account.

### EPIC - BASE FUNCTIONALITY AND EASE OF USE

####  USER STORY: Site navigation

- As a user, I can access important links such as home, products, my cart, sign in/out, and profile by scrolling and/or clicking once, regardless of where on the site I am, so that I can easily navigate the site.

####  USER STORY: Newsletter Signup

- As a user, I can see a form to register for newsletters repeatedly throughout the website, so that I can receive news and offers.

####  USER STORY: Facebook Business Page

- As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook.

####  USER STORY: Authentication visibility

- As a user, it is visible if I am signed in or not so I am made aware of this.

####  USER STORY: Home Page

- As a user I can navigate through the home page so that I get to know the website's purpose and what it offers.

### EPIC - PRODUCTS

####  USER STORY: Products list

- As a user, I can browse a list of products for sale on the site so that I can find the product I wish

####  USER STORY: Product searching

- As a user, I can perform a search, so that products matching the search appear in the products list.

####  USER STORY: Products sorting

- As a user, I can sort the products list by category, so that I can quickly find the product I wish

####  USER STORY: Product main infos 

- As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that I know most details without having to click on the product.

####  USER STORY: Product quantity

- As a user, I can select the quantity of the product to purchase the correct quantity desired.

####  USER STORY: Product detail page

- As a user, I can click the product in the products list so that I can view the further details of the product.

### EPIC - THE CART

####  USER STORY: Viewing the cart contents

- As a user, I can view the products added to my cart by clicking the cart icon.

####  USER STORY: Removing product

- As a user, I can click the remove button, so that I can easily remove products from my cart.

####  USER STORY: Total cart cost

- As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be.

### EPIC - CHECKOUT

####  USER STORY: Proceed to checkout

- As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart

####  USER STORY: Purchase successful

- As a user, I am informed of whether my purchase was successful or not.

####  USER STORY: Secure Card Payment

- As a user, I can enter my card details on the checkout page with security, so that I can make the desired purchase.

### EPIC - WISH LIST

####  USER STORY: Add to Wish List

- As a logged-in user, I can add a product to my Wish List, so that I can easily view it later.

####  USER STORY: Remove from Wish List

- As a logged-in user, I can remove a product from my Wish List if I want to.

### EPIC - REVIEWS

####  USER STORY: Read reviews

- As a user, I can read user reviews from other users, so that I easier know if the product is right for me.

####  USER STORY: Write reviews

- As a logged-in user, I can review products in the list so that other users can benefit from this.

#### USER STORY: Remove review

- As a logged-in user, I can remove my review of a product, so that it no longer is there.

 [Back to Table of contents](#table-of-contents)

 


## Structure
 ### Wireframes
- [Check the wireframes used to this project](). 

 ### Diagrams
 
 - [Check the diagrams used to this project](). 

  [Back to Table of contents](#table-of-contents)

## Features
#### User Features


#### Owner/Admin Features


## Future Features


 [Back to Table of contents](#table-of-contents)
## Technologies Used

### Main Tech
 - [Django](https://www.djangoproject.com/) 
 - [Java Script](https://www.javascript.com/)
 - [Bootstrap](https://getbootstrap.com/)


### Applications, Libraries and Platforms


[Back to Table of contents](#table-of-contents)

## Validation


 - [Click here]().

## Testing
 


## Credits

#### Content
 * All content was written by me.

#### Media
 * Website logo was made by me.

 * All images came from [Unsplash](https://unsplash.com/.).

[Back to Table of contents](#table-of-contents)

## Screenshots

### Home
![]()
![]()
![]()

### Shoppiing
![]()

### Cart
![]()
![]()
![]()

### Page 2
![]()

### Page 3  
![]()

###  Page 4
![]()

[Back to Table of contents](#table-of-contents)