
BUGS FOUND:
Slidebar does not work properly on aulth pages
Delivery banner and footer horizontal scroll

Product details:
- maybe remove image url or host imgs on cloud

# [Cheltenham Organics](#)
![](#)

 Cheltenham Organics is an ecommerce web application for customers seeking to purchase organic food online.

 You can test the card payment functionality without making a purchase. 

 Use card details for it: 4242 4242 4242 4242 - CVC and 5-number postal code at the end of the card can be any numbers.

 
 [Click here](#) to visit the deployed site.

To access admin, click [here](#)
- User: Organics
- Password: NoneOrg123

---

# Table of contents
1. [Agile Workflow](#agile-workflow)
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


## Owner/admin Stories


[Back to Table of contents](#table-of-contents)  

## User Stories

### EPIC - REGISTRATION AND USER ACCOUNTS

#### Register an account

- As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits.

#### View profile

- As a logged-in user, I can view a profile page, so that I can view my previous orders, and view, update or remove my delivery and contact details.

#### Email confirm upon signing up

- As a user, I have to confirm my email address to complete my account registration.

#### Recover Password

- As a user, I can easily recover my password in case I forget it, so that I access my account.

### EPIC - BASE FUNCTIONALITY AND EASE OF USE

#### Site navigation

- As a user, I can access important links such as home, products, my cart, sign in/out, and profile by scrolling and/or clicking once, regardless of where on the site I am, so that I can easily navigate the site.

#### Newsletter Signup

- As a user, I can see a form to register for newsletters repeatedly throughout the website, so that I can receive news and offers.

#### Facebook Business Page

- As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook.

#### Authentication visibility

- As a user, it is visible if I am signed in or not so I am made aware of this.

#### Home Page

- As a user I can navigate through the home page so that I get to know the website's purpose and what it offers.

### EPIC - PRODUCTS

#### Products list

- As a user, I can browse a list of products for sale on the site so that I can find the product I wish

#### Product searching

- As a user, I can perform a search, so that products matching the search appear in the products list.

#### Products sorting

- As a user, I can sort the products list by category, so that I can quickly find the product I wish

#### Product main infos 

- As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that I know most details without having to click on the product.

#### Product quantity

- As a user, I can select the quantity of the product to purchase the correct quantity desired.

#### Product detail page

- As a user, I can click the product in the products list so that I can view the further details of the product.

### EPIC - THE CART

#### Viewing the cart contents

- As a user, I can view the products added to my cart by clicking the cart icon.

#### Removing product

- As a user, I can click the remove button, so that I can easily remove products from my cart.

#### Total cart cost

- As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be.

### EPIC - CHECKOUT

#### Proceed to checkout

- As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart

#### Purchase successful

- As a user, I am informed of whether my purchase was successful or not.

#### Secure Card Payment

- As a user, I can enter my card details on the checkout page with security, so that I can make the desired purchase.

### EPIC - WISH LIST

#### Add to Wish List

- As a logged-in user, I can add a product to my Wish List, so that I can easily view it later.

#### Remove from Wish List

- As a logged-in user, I can remove a product from my Wish List if I want to.

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
- Enable public access for your bucket so users can access and use the services on your website (upload, view, download, etc). More info can be read in the official documentation: [AWS S3](https://aws.amazon.com/s3/)

 [Back to Table of contents](#table-of-contents)

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