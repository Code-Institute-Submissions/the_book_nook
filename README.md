# The Book Nook
(Milestone Project 3 for Code Institute)

![Desktop views](static/wireframes/readmeimage.png "The Book Nook")

This is a website created for passionate book readers. It is a site to share their favorite books as well as find new favorites based on other users recommendations. 
The site owners goal is to gather a community of book readers, sharing favorite books with eachother.  

## UX

### User Stories

#### Visitor UX: stories 
 - As a user I want the site to be easily understood and navigated.
 - I want it to be easy to search for books.
 - I want to easily find where the books are.
 - I want it to be easy and convenient to sign up as a member to add my own books to the site. 
 - I want it to be easy to find where to purchase a book.
 
#### Registered user UX stories:
- As a member I want it to be easy to add a new book.
- As a member I want to find my own added books. 
- As a member I want to like/upvote a book.
- As a member I want to comment on a book.
- As a member I want to easily logout from site.
.
#### Admin user UX stories:
- As an admin I want to easily find an overview over the different categories of books on the site.
- As an admin I want to easily view, add, edit or delete any categories. 


### Site Owners Stories
- As a site owner I want the users to easily navigate and interact throughout the site.
- I want the users to sign up to the community to add their own books to the library, thereby making the community and library grow bigger.
 
## Design

Simple design throughout page with green as the baseline color with accent colors of grey and white. Continued structure throughout site with navigation bar and footer.

### Wireframes
- Index page - [View](static/wireframes/index.png)
- Book Collection page - [View](static/wireframes/bookcollection.png)
- Single Book page - [View](static/wireframes/singlebook.png)
- Register page - [View](static/wireframes/register.png)
- Log In page - [View](static/wireframes/login.png)
- Profile page - [View](static/wireframes/profile.png)
- Add Book page - [View](static/wireframes/addbook.png)
- Edit Book page - [View](static/wireframes/editbook.png)
- Categories page - [View](static/wireframes/categories.png)
- Add Category page - [View](static/wireframes/addcategory.png)
- Edit Category page - [View](static/wireframes/editcategory.png)

## Features

# Features
- Visible on all pages:
  - Navigation bar, with links displaying as dropdown feature on mobile views.
    - For **visitors** displaying links to 'Logo', 'Book Collection', 'Register' and 'Login'.
    - For **logged in users** navigation bar links 'Register' and 'Login' are replaced with 'My Books' and 'Log Out'. 
    - For **admin** the navigation bar is the same as for logged in users with the added link to 'Manage Categories'
  - Footer bar with email address to contact site-manager and social media links to Instagram and Facebook. 
-   Index page  a search bar for visitors and logged in users to use. Below search bar visitors/users will find information about the site and links to book collection, login and register pages. And finally a generated list of top three favorite books on the site.
- Book Collection page displaying all books added by users in alphabetical order in collection. On top of page visitors/users will also find a search bar. 
-   User registration functionality
-   Log in / out functionality
-   Profile page showing list of all books added by the user, as well as the ability to add a new book and edit/delete their own added books. 
- Categories site allowing admin to view all categories as well as add a new category and edit/delete existing categories. 
- Admin also have the possibility to edit/delete any book in the collection regardless who created the book.
-   Mobile responsive design.

### Future features to implement
- Add a check so that a user can only like a book once, clicking again will 'unlike' book. 
- Add user-name to the comments and possibility to edit and delete own comments.  
- Affiliate link under each book.
- Ability to add more than one category to each book.

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5.com)  
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Frameworks
- [Balsamiq Wireframes]([[https://balsamiq.com/wireframes/](https://en.wikipedia.org/wiki/Balsamiq#Balsamiq_Wireframes)) 
  - was used to help create mockup and create UX-design for website.
- [Color Picker](https://htmlcolorcodes.com/) 
  - was used to choose colors for site
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Font Awesome]([https://fontawesome.com/](https://fontawesome.com/)) 
  - is used for the fonts on index-page
- [GitHub](https://github.com/) 
  - was used to store the projects code after being pushed from Git.
- [Gidpod](https://www.gitpod.io/) 
  - was used for version control by using the Gitpod terminal to commit and push to Github.
- [Google Fonts]([https://fonts.google.com/](https://fonts.google.com/)) 
  - was used to import font 'Noto Sans' which was used throughout site
- [Heroku]() - 
  - was used to deploy site.
- [JQuery](https://jquery.com/) 
  - was used when writing Javascript code.
- [MongoDB]() 
  - was used as database.
- [Stackedit](https://stackedit.io) 
  - was used to write Readme-file. 


## Testing

- Html-code tested with W3C Markup Validator, view result [here]()
- CSS-code tested with W3C CSS Validator, view result [here]()
- Responsiveness of website was checked using [Am I Responsive?](http://ami.responsivedesign.is/)

Google Dev Tools Lighthouse was run to check accessibility of page [view here]()

### Link Testing 

#### Navigation bar 
- Clicking on the logo transports the user to the start page if on another part of the site
-   All below links transports the user to the correct sites:
    - Visitor UX Stories:
      - Home 
      - Book Collection   
      - Register 
      - Log In
    -  Logged In User UX Stories: 
       - My Books
       - Log Out
    - Admin User UX Stories:
       - Manage Categories
  
#### Index Site
- Search function working correctly, user is transported to search-page where books from search result is listed.
    - If no results a message is shown instead that no books were found. 
- A list showing top 3 books of site.
  - All three book showing image, title, author, category and 'Read more'-button.
  - Beneath 'Top 3'-headline text and link is shown that transport visitor to book collection to see all books. 

#### Book Collection
- Search function working correctly, user is transported to search-page where books from search result is listed.
  - If no results a message appear that no books were found. 
- Book collection is shown in alphabetical order based on book title. 
  - Visitor User Ux Stories:
    - Book image, title, author, category is shown to user.
    - Button with text 'Read more' is shown beneath every book, transporting user to Single Book Page.
  - Logged In User UX Stories:
    - A heart is shown above image with the number of likes a book have, when heart is clicked counter is incremented with one.
    - Text showing which user added book is shown in low right corner of every book information.
  - Logged In Users Own Books UX Stories:
  - Two buttons are shown under every book that was created by user; 'Edit Book' and 'Delete Book', transporting user to 'Edit Book'-page alternatively 'Delete Book'-page. 

#### Single Book Page
- Visitor User UX Stories:
    - One button at top of page, 'Go to Book Collection', transports user back to book collection page.
    -  On page book image, title, author, category, and a short book description (added by the user who created the entry).
    - Comment section where user can read comments added by registered users about the book.
  - Logged In User UX Stories:
    - Username for author of book entry is shown.
    - Comment form below book where user can add their own comment about the book.
  - Logged In User Own Added Books UX Stories:
    - Two buttons below book description are shown; 'Edit Book' and 'Delete Book', transporting user to 'Edit Book'-page alternatively 'Delete Book'-page. 

#### Register
- Register form for visitor to type in preferred username and password, below each field text informing user that username and password must be 5-15 letters and/or numbers.
  - If 'username'-field, 'password'-field or 'confirm password'-field is left empty: a message appears asking user to fill out field
  - If 'username' is already taken, a flash message appears informing user to choose different username.
  - If 'password' and 'confirm password' is not matching a flash message appears asking user to ensure that password and confirm password is a match.
- If visitor clicks 'Cancel'-button they are transported back to 'Index'-site.
- At bottom of page user finds link to 'Log In'-page if already a member.
- Upon successful registration, the newly registered user is transported to its 'profile'-page.

#### Log In
- User fills in 'username' and 'password', if both are matching with database user is transported to its 'profile'-page. 
  - If either 'username' and/or 'password' is not a match with database a flashed message appears informing user that username and/or password is incorrect.
- If user clicks 'Cancel'-button they are transported back to 'Index'-site
- Below form user finds a link to 'Register'-page which transports user to site to register as new user.

### Logged In User UX Stories 

#### Profile
- Profile page shows two buttons, 'Go to Book Collection' and 'Add New Book'. 
  - When clicking on 'Go to Book Collection' user is transported to 'Book Collection'-page.
  - When clicking on 'Add New Book' user is transported to a new page with a form to fill in. 
- Below the two buttons all the books added by the user is shown. 
- Every book consisting of book image, title, author, category, 'created by' and 'Read more'-button, as well as 'Edit Book' and 'Delete Book'-buttons.

#### Log Out
- When clicking on 'Log Out' in navigation menu user is logged out and transported back to 'Index'-page.

#### Add Book
- Form consists of input fields for book title, author, a dropdown menu to choose book category, a text-area to write a short book description and input for image. 
  - If any input field is left empty user gets message asking user to fill out field. 
- If submit is successful, user is transported back to its 'Profile'-page where new book is added to users list of added books. 
- When clicking 'Cancel'-button user is transported back to its 'Profile'-page
- 
#### Edit Book 
- When clicking on 'Edit Book'-button user is transported to 'Edit Book'-page with a form. 
  - Form fields are already pre-filled with the books current information.
  - When clicking 'Cancel'-button user is transported back to 'Profile'-page.
- On successful submit changed are saved and user is transported back to 'Profile'-page. 

#### Delete Book
- When clicking 'Delete'-button book is deleted and user is transported to 'Profile'-page.

### Admin User UX Stories
#### Categories
- A new tab in navigation menu only visible for admin; 'Manage Categories'.
- When clicking link admin is transported to 'Categories'-page consisting of all book-categories already added. 
- At top of page admin finds 'Add New Category'-button. When clicked admin is transported to 'Add Category-page.
- Below 'Add Category'-button are all categories presented, each with a 'Edit Category' and 'Delete Category'-button. 
  - When clicking on 'Edit Category'-button admin is transported to new page 'Edit Category.
  - When clicking on Delete the category is instantly deleted. 

#### Edit Category 
- Category selected is shown in a form, with the pre-filled field for category name chosen to edit. 
  - On submit category is changed and admin is transported back to 'Category'-page.
  - On Cancel category-name remains as previous and user is transported back to 'Category'-page. 


### Further Testing 
- The Website has been tested on Google Chrome, Internet Explorer and Safari browsers.
- The website has been tested on Iphone 12, Samsung Galaxy S9, Motorola G7+, Huawei p30 Pro, OnePlus 6.

### Known Bugs
- The pages something links to http instead of https making site insecure. 
- Footer is not sticking to bottom at all pages.
- The hero-image is distorted on iPhone 12.


# Deployment

### Heroku Deployment

This project has been deployed to Heroku. Automated pushes were enabled from my GitHub repository to Heroku. The following steps were taken for setting up deployment on Heroku:

1.  In GitPod IDE create requirements.txt and Procfile file: 
- Create requirements.txt file: 
  - In terminal type in '***pip freeze > requirements.txt***'
- Create a Procfile:  
  - In terminal type in '***echo web: python app.py > Procfile'*** 

- In terminal then write commands: 
  - '***git add -A***'
  - '***git commit -m "Added requirements.txt and Procfile***' 
  - and lastly '***git push***' to ensure requirements.txt and Procfile are in the GitHub repository 
    * ! Forgetting these step means Heroku can't find the files in git and won't know how to run or deploy the app)*
2. Create new app in Heroku:  
  *(If not already create account on Heroku)* 
  - Once registered/logged in go to Dashboard: 
    - choose "**Create new App**"
    - Enter desired app name *(remember app name must be unique)*
    - Select preferred region.

3. Set up connection to Github Repository:

  -   Click the deploy tab and further down on page select GitHub - **Connect to GitHub**.
      - A prompt to find a Github repository to connect to will then be displayed.
      - Enter the repository name for the project and click search.
      - Once the repo has been found, click the **Connect** button.
 4. Once app is created go to **Settings**: 
  - Choose "**Reveal Config Vars**" *(this is to tell Heroku which variables are used/required)*
    - In the input fields add: 
      - Key: ***IP***, Value: ***0.0.0.0***
      - Key: ***PORT***, Value : ***5000***
      - Key: ***SECRET_KEY,*** Value: **-->** *!add your secret key here*
      - Key: ***MONGO_URI***, Value:  **-->** *!this can be found in your MongoDB by going to clusters > connect > connect to your application. In popup window choose Python as language. After choosing language you will see a string just below, copy it and paste it into value. Don't forget to change the <dbname> and <password> in string before saving*
      - Key: ***MONGO_DBNAME***, Value: **-->** *!Add the database name you want to connect your app to here*
 5. After that's done go to the "**Deploy**" tab: 
   - There you will choose "**Enable Automatic Deploys**" and choose deploy branch *(usually master or main)*. 
   - After deployment is finished below you will see "Your app was successfully deployed" and a '**View**'-button that will open your site in a new window-tab.
  
## Credits

### Content

### Code 
- 'CI's Miniproject - Putting It All Together' was used to help with the code to set up app as well as app.py coding for route and functionality for the register - login - search - add/edit/delete_book - add/edit/delete_category functions. 
- Javascript to make flash-message fadeout after appearing was found on [StackOverflow](
https://stackoverflow.com/questions/51822192/trying-javascript-to-have-my-flash-my-message-disappear-after-a-few-seconds-afte) 

### Media
-   Hero Photo by [Syd Wachs](https://unsplash.com/@videmusart?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/books?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Book images are users inputs from various websites.  

### Own Reflections 


### Acknowledgements
- Thank you to my mentor for valuable help and input throughout the project. He gave me great input helping me to better understand the python language. 

> Written with [StackEdit](https://stackedit.io/).