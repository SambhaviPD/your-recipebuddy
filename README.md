# RecipeBuddy

RecipeBuddy is a straightforward web app, leveraging Streamlit's front-end and FastAPI's back-end to provide recipe suggestions based on user input. It displays an assortment of recipes, each with a clear image, ingredient list, and preparation instructions, sourced from a diverse array of culinary sites. An uncomplicated solution for those seeking cooking inspiration tailored to their preferences.

# A quick demo (WIP)
https://recipebuddy.fly.dev/

# Further Details about RecipeBuddy
Initial target segment for RecipeBuddy is literally anyone who wants some interesting recipe ideas without doing a lot of search. 

3 APIs are written when I open sourced the repo. Testcases are written using playwright and pytest. CI is integrated as well. CD is not enabled as the repo needs to stabilize, solid features to be added. I plan to maintain a feature roadmap along with a sprint plan. 

The code was developed on Windows platform, but it's designed to run seamlessly on any other platform without modifications. To start with, the solution is deployed in [fly](https://fly.io/)

All contributions are welcome!


### How to set it up in your local machine?
- Create a virtual environment. Here's a [good link](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) that'll help you create one
- For the repository using the fork button on top right corner
- Before setting up the code, sign up at `https://spoonacular.com/food-api`
- Go to My Console -> Profile -> Generate new API Key. This will be your Spoonacular API Key
    for your local use. Free plan is good enough for local development and testing
- Open a terminal and navigate to recipebuddy/src/
- Create a .env file
- Add the following entries
    SPOONACULAR_BASE_URL="https://api.spoonacular.com/recipes"
    SPOONACULAR_API_KEY="Replace your API Key here"
- Save the file
- Now navigate to recipebuddy/src/recipebuddy_backend
- Execute `pip install -r requirements.txt`
- Once the packages are installed, navigate to recipebuddy/src/recipebuddy_frontend
- Again execute `pip install -r requirements.txt`
- Once all packages are installed, navigate to root directory i.e. recipebuddy
- Execute `docker-compose build`
- Once both the images corresponding to both images are built successfully, execute
    `docker-compose up`
- This will bring up the application in your local machine. To test, goto `https://localhost:8501`
- You should see the home page of your-recipe-buddy
- For Github Actions to work, add secrets to your repository
- Go to your Github repo of your-recipe-buddy
- Choose Settings -> Security -> Secrets and Variables -> Actions
- Click on New Repository Secret
- Add the same values as present in .env file
- Save them. Now github workflow file will run smoothly when you try to commit your code


### How to start contributing
- Follow the steps under `How to set it up in your local machine?`
- Once setup is successful, proceed to the next step
- Choose an issue to work on
- Update on comments section that you are working on a particular issue
- Create a new branch from the issue before you start working
- Checkout the newly created branch
- Work on the issue
- Add test cases to ensure that your code does what it's intended to do
- Commit your code to the branch you created
- Open a Pull Request (PR)
- On successful code review, your changes will be merged to main

### Roadmap
https://sambhavi.notion.site/RecipeBuddy-Roadmap-f6ff7c9f33a043b9b133793d2a698474

### How it started
Two reasons:  
(1) I was bored of cooking the same recipes again and again. Wanted some variety 😀
(2) I've also been wanting to open source my work, collaborate with people of similar interests and build 🤝

This situation seemed to fit both my bills. I developed a few features myself, and then opening it up so that there is a wall for everyone to start sketching.

### Contributors

