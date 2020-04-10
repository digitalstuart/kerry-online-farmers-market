# Kerry Online Farmers Market

Farmers markets are popular aspects of local community life around Kerry - however, they take place at fixed locations and on specific days and times.

So how about opening up the availability of these locally grown and produced products by offering them for sale online? It is also potentially a very useful tool for farmers and producers to be able to continue selling during this period of lockdown and social isolation.

That is the purpose of Kerry Online Farmers Market. Producers can list their items and products for sale; website customers can buy them. There is also an area of the site for users to post any recipes they wish to share which include ingredients purchased from the online market.

The aim of the project at this point in its life cycle is to display what I have learnt about building an ecommerce site with Django and Python. Registered users can add objects to a database; customers can browse and select products for purchase; then there is a shopping cart and checkout functionality.

The site would require further work to make it fully functional in 'the real world', plus there are also prospects for progressive enhancement in the future, both of which are discussed later in this document.

## UX

The landing page has a very clear and prominent website heading, with a bold and attractive background image that makes it clear what the site is about.

It also has two prominent calls to action - **'Login to buy'** or **'Login to sell**'. The website's two key pieces of functionality are clearly stated to the customer.

Different navbar menu items are displayed according to the whether users are logged in or not, in particular *login/register* and *profile/logout*. It is always obvious how the user is able to interact with the site.

The website uses an attractive font for consistent headings, as well as clean Bootstrap forms. Product and recipe listings employ the same panel style of presentation.

Interaction with the site is clearly mapped through prompts and messages, which are relevant to the steps that a user can take at any given point. 

The process of selecting and purchasing a product should be achievable with just the following the steps:
* User logs in and is greeted with a 'login success' message.
* User finds desired product, selects amount and clicks 'Add'. 
* Item(s) added to cart; user clicks on 'Cart' menu item.
* User can amend number of selected products and/or click 'Checkout' button.
* User completes personal and payment details form, clicks submit and then sees a 'purchase success' message.

### User Stories

* I am a farmer/producer in Kerry who wishes to make my fresh produce and products available for sale online.

![alt text](https://i.imgur.com/3aKnszE.jpg "Kerry Online Farmers Market screenshot")
* I am a Kerry resident who likes to buy locally grown and produced items from a farmers market, but I can't always get there on the days it is held. Can I buy any of the products online?

![alt text](https://i.imgur.com/6osrbTD.jpg "Kerry Online Farmers Market screenshot")
* I'd like to find recipe ideas from other people who are using fresh local ingredients.

![alt text](https://i.imgur.com/R1JfR33.jpg "Kerry Online Farmers Market screenshot")

I used Balsamiq to create some wireframes for the project. 

SCREENSHOTS HERE

## Features

### Existing features

### Features left to implement

## Technologies

## Testing

1. Navbar

LOTS MORE TO COME IN HERE!

The site was manually viewed and tested in the Chrome and Firefox browsers on a Windows 10 laptop, as well on iOS and Android mobile/tablet devices.

This was done with a view to ensuring that: all functions and interactivity respond appropriately on both mobile and desktop; responsive changes in the navbar and site layout are all present and correct for different devices; and the site remains fully functional, useable and well presented across all screen sizes.

I also ran my code through the W3C validator tools for HTML/CSS, as well as JSHint for Javascript and http://pep8online.com for Python.

## Django database details?

## Deployment

* I created a new app in Heroku called *kerry-online-farmers-market* with the region selected as 'Europe'.
LOTS MORE TO COME IN HERE!
* I then clicked 'Open app' and my website was deployed live to https://kerry-online-farmers-market.herokuapp.com.
* In order to clone this project, you should paste https://github.com/digitalstuart/kerry-online-farmers-market.git into your chosen editor's terminal. Then type *git remote rm origin* into the terminal to sever the link with the original.

## Credits

### Content

### Acknowledgements