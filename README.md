# RecipeBuddy
Webapp to suggest recipes based on a variety of input choices. Frontend using Streamlit and Backend using FastAPI

### How it started
Two reasons:  
(1) I was bored of cooking the same recipes again and again. I wanted some variety.
(2) I've also been wanting to open source my work, collaborate with people of similar interests and develop. 

This situation seemed to fit both my bills. I developed a few features myself, and then opening it up so that there is a wall for everyone to start sketching.

### Super brief roadmap
Initial idea was to just build APIs that can be consumed by any web app/modile app. For a visualization purpose, a simple frontend using Streamlit was added. At some point of time, I plan to leave behind the frontend part and just focus on backend. 

At the moment (June 11, 2023):
1. 3 APIs have been developed, both backend and frontend with testcases in playwright and pytest 
2. Docker files are written, one for backend and one for frontend
3. docker-compose.yml is added for easy deployment in local
4. CI pipeline is set up through Github actions
