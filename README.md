
BUGS FOUND:
Slidebar does not work properly on aulth pages
Delivery banner and footer horizontal scroll - fix setting   max-width: 100%;
  overflow-x: hidden;
- Heroku wasnt posting to S3, just receiving 
Product details:
- maybe remove image url or host imgs on cloud


# [Cheltenham Organics](https://cheltenham-organics.herokuapp.com/)
![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/project-img.PNG)


 Cheltenham Organics is an ecommerce web application for customers seeking to purchase organic food online.

 You can test the card payment functionality without making a purchase. 

 Use card details for it: 4242 4242 4242 4242 - CVC and 5-number postal code at the end of the card can be any numbers.

 
 [Click here](https://cheltenham-organics.herokuapp.com/) to visit the deployed site.

To access admin, click [here](https://cheltenham-organics.herokuapp.com/admin/)
- If you want to access admin, contact me! (The admin user and password in the version history no longer exist!)

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

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/kanban-board.JPG)
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

## User Experience

 ### Structure

 #### Wireframes
- [Check the wireframes used to this project - LARGE SCREEN](https://github.com/arthurvguide/cheltenham-organics/tree/main/docs/wireframes-large-screen). 
- [Check the wireframes used to this project - MOBILE SCREEN](https://github.com/arthurvguide/cheltenham-organics/tree/main/docs/wireframes-mobile).

 ### Database

The SQLite database was used for the development environment, and the Postgres database for production once the project was deplyed on Heroku. Both are relational databases and work well with the Django framework used for this project. Check the data model below.

 - [Check the diagrams (database scheme) used to this project](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/database%20scheme-cheltenham%20organics.png). 


  [Back to Table of contents](#table-of-contents)

### Features
##### User Features

    - User can buy products without having an account
    - User can checkout using a secure system (stripe)
    - User can subscribe for newsletter and receive offers

    - User can create an account and have benefits
    - User logged-in can buy products and save their address for future purchases
    - User logged-in can review products
    - User logged-in can send positive or negative feedback about their historic orders
    - User logged-in can add and remove products to their wishlist
    

##### Admin Features

    - Admin can create a product category
    - Admin can create products
    - Admin can delete reviews without using admin dashboard, so can avoid spam reviews
    - Admin can check the orders feedback by accessing the orders in the admin dashboard

### Future Features

    - User can procces payment using apple pay, google pay and paypal.
    - User can rate the products as well, not only review.
    - User can use vouncher Wcodes
    
    - Admin can have stock control
    - Admin can add products without using admin dashboard
    - Admin can put discounts on products
    - Admin can generate vouncher codes

 [Back to Table of contents](#table-of-contents)

### Screenshots and website breakdwon with its features

#### Home Page and Navigation 

- Hero section and the navbar. In the Navbar user can log in, create accounts, go into a shopping bag, and use the search bar to look for products. In the hero section, there's a "call to action" button, calling the customer to shop.

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/home-page/home-page-1.PNG)

- Explaining a bit more about the organic food system to the user

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/home-page/home-page-2.PNG)
![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/home-page/home-page-3.PNG)

- In the footer user can signup for newsletter mail, receiving offers direct to their email. Also user can access the Home, Privacy Police, Terms of use and social links. 

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/home-page/home-page-footer.PNG)

#### Products pages

- All Products pages - User can select desired product and then goes to product detail page.

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/products/all-products.PNG)

- Product details page - User can add the product to the cart, if logged-in can read, write reviews, and delete their reviews it they desire so. If not logged-in they can just read reviews. Logged-in user can add the product to the wishlist. 

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/products/product-details.PNG)

#### Profile page

- Logged-in user has a profile page, where they can access ther order history and change default delivery address and also access wishlist.

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/profile/my-profile.PNG)

- A wishlist where the customer can save products they want to buy at some point. If the product is clicked, they are taken to the product detail page.

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/profile/profile-wishlist.PNG)

#### Admin Dashboard

- The website Admin has control over everything in the app. Through this, the admin can create new products to be displayed, and categories and also can read the feedback from the customer who purchased something. 

![](https://github.com/arthurvguide/cheltenham-organics/blob/main/docs/project-screenshots/admin/admin-dash.PNG)

## Technologies Used

### Languages
- Python 3.8 was used for backend programming

- HTML5 was used for building all web pages

- CSS3 was utilized for styling the website

- JavaScript for frontend programming

### Frameworks, Libraries and Other Resources

- Bootstrap 4 

- JavaScript framework JQuery 

- Font Awesome fonts

- Google Fonts

- Facebook Pages was used to create the Facebook Business Page that is linked on the site.

- Mailchimp was used to create the newsletter signup form.

- Git - Version control system used to commit and push to Github via Gitpod.

- Github - The projects repository and all its branches were commited, and pushed to Github.

- Stripe - Used to process the users payments and handle webhooks.

- Gitpod - All code was written and tested with the Gitpod web-based IDE.

- Balsamiq Wireframes was used to create wireframe for the project

- Lucidchart was used to create the visual model schema for the project.

- Heroku - Used to deploy the application.

- AWS S3 Bucket - Used to host media (images) and static(CSS and JavaScript) files for the site.


[Back to Table of contents](#table-of-contents)

## Validation


 - [Click here]().

## Testing
 
## Deployment

### Forking the GitHub Repository

To make a clone, or 'Fork' this repository, follow the steps below.

    - Access your GitHub account and find the relevant repository.
    - Click on 'Fork' on the top right of the page.
    - You will find a copy of the repository in your own Github account.

### Making a Local Clone

    - Access your GitHub account and find the relevant repository.
    - Click the 'Code' button next to 'Add file'.
    - To clone the repository using HTTPS, under clone with HTTPS, copy the link.
    - Open Git Bash.
    - Access the directory you want the clone to be have.
    - In your IDE's terminal type 'git clone' and the paste the URL you copied.
    - Press Enter.
    - You now have a local clone.

### Heroku
This application has been deployed from Github using Heroku. Here's how:

    - Create an account at heroku.com
    - Create a new app, add app name and your region
    - Click on create app
    - Go to "Settings"
    - Under Config Vars, add your sensitive data (creds.json for example)
    - For this project, I set buildpacks to and in that order.
    - Go to "Deploy" and at "Deployment method", click on "Connect to Github"
    - Enter your repository name and click on it when it shows below
    - Choose the branch you want to buid your app from
    - If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository
    - All done!

### AWS S3

The deployed version of this website has static(CSS and JavaScript) and media files hosted to it via a web based service called Amazon Web Services S3 Bucket.

The steps to take are:

    - Create an account at aws.amazon.com
    - Navigate to the IAM application and create a user and group
    - Set the AmazonS3FullAccess for the user and copy the AWS ACCESS and SECRET keys as config vars to your workspace and deployment environment
    - Create a new Bucket within the S3 application with an appropriate name.
    - Enable public access for your bucket so users can access and use the services on your website (upload, view, download, etc). More info can be read in the official       documentation at https://aws.amazon.com/s3/

## Credits

#### Content
 * All content was written by me.

#### Media
 * Website logo was made by me.

 * All images came from [Unsplash](https://unsplash.com/.).

[Back to Table of contents](#table-of-contents)

