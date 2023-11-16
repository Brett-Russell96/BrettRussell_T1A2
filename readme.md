# T1A2 Portfolio

## Overview
This portfolio website was created to demonstrate my ability to build websites using HTML and CSS elements. It also aims to offer insight into my skills and experience, reflect my personality, and provide a glimpse into my motives for pursuing web development.  

It also serves as a platform for potential employers to establish future contact with me if they find my skills align with their needs.

## Sitemap
![This is my original Sitemap](./images/Sitemap.png)
This is my original Sitemap, the structure is an 'index.html' homepage that connects to all other pages. Each page is accessible from one another using a navigation bar. 

 Initially, my plan was to include each blog post in its own separate HTML file. However, I later on made the decision to use a scroll-down link structure to keep all the posts on the same file and make the site more convenient.

 ## Site Features
 The site features a similar interface across all pages which utilises a well thought out color structure designed for clear visability and a pleasing aesthetic.

 The site was built for compatibility across 3 wireframes which are pictured below:

 ![large Wireframe](./images/large-wireframe.png) 

 ![Medium Wireframe](./images/medium-wireframe.png)

 ![small Wireframe](./images/small-wireframe.png)

 There is a navigation bar across the top of each webpage to move between each HTML file, the site logo at the top left of the display also acts as a link to the home page.  
 On smaller displays the nav bar is replaced with button links to each page for improved aesthetic and accessability. On the smaller wireframes the nav bar changes to a button display for improved accessability on tablets and smart-phones the text size and footer also changes to improve display on smaller screen widths.

 Here is the code used for the header:

 ```html
     <header>
        <div class="logo-name">
            <a href="./index.html">
                <img
                    src="Images\site-logo.png"
                    alt="Website Logo"
                    />
            </a>
        </div>
        <h1>Welcome!</h1>
        <nav id="nav-items">
            <a href="./templates/about.html" class="button">About</a>
            <a href="./templates/skills.html" class="button">Skills</a>
            <a href="./templates/blog.html" class="button">Blog</a>
            <a href="./templates/contact.html" class="button">Contact</a>
        </nav>
        <div class="background-box"></div>
    </header>
```

Here is the code for the footer:

```html
    <footer>
        <div class="social-media">
            <a href="https://twitter.com/BrettRussell96">
                <i class="fa-brands fa-square-twitter"></i>
            </a>
            <a href="https://github.com/Brett-Russell96">
                <i class="fa-brands fa-square-github"></i>
            </a>
            <a href="https://www.linkedin.com/in/brett-russell-a52929299/">
                <i class="fa-brands fa-linkedin"></i>
            </a>
        </div>
        <div class="info">
            <p>Phone: 0422861355</p>
            <p>Email: brett.russell2016@gmail.com</p>
        </div>
    </footer>
```


  
 There are separate pages which contain sections for:
 * Skills and previous experience including a link to my resume.
 * Contact where there is a link to my email address. 
 * Blog which contains an assortment of blogs and accompanying images.
 * About which contains general information about my, personality, motivations and personal interests.

 ### Home Page 
The home page is fairly simple, it contains a heading with a brief introdution to my page.

![Home Page](./images/home-screenshot.png)

I is styled using a grid, display for the layout and a flex display for each component inside the grid.

```SCSS
    @media screen and (min-width: $large) {

        main {
            display: grid;
            grid-template-columns: 30% 70%;
            grid-template-rows: 25% 25% 50%;
    
            .home-text {
                grid-column: 2;
                grid-row: 1;
                display: flex;
                justify-content: space-evenly;
                align-items: flex-start;
                margin-bottom: 300px;
                color: $secondary-color;
                font-family: Verdana, Geneva, Tahoma, sans-serif;
            }     
        } 
    }
 ```
    
Most of the pages on my site adopt a similar styling in order to keep consistancy in the display.

![Smaller-Wireframe](./images/home-small-screenshot.png)

The smaller wireframes switch to a flex display for the layout:

```SCSS
    @media screen and (max-width: $large) {
        main {
            display: flex;
            flex-direction: column;
            justify-content: space-evenly;
            align-items: center;
            margin-bottom: 40px;
    
            .home-text {
                text-align: center;
                color: $secondary-color;
                font-family:Verdana, Geneva, Tahoma, sans-serif;
                margin-bottom: 40px;
                word-wrap: break-word;
                max-width: 75%;
            }
        }
    }
```

This display styling is also used fairly consistently around the site.

### About Section
The about Section gives a description of my interests and motivations as well as some photos of myself. 


 ## Target Audience
 The audience for this website would ideally be an employer with technical knowledge in IT and software development who is seeking a potential developer for their team.

 ![About-Section](./images/about-screenshot.png)

 I use pseudo classes nested inside one container class for the code:

 ```html
     <main class="about-container">

        <img class="home-photo" 
            src="../images/selfie.jpeg"
            alt="Photo of myself" />
        <img class="gym-photo"
            src="../images/gym-selfie.jpeg"
            alt="2nd Photo of myself" />

        <div class="about-section">
            <h2>Who am I?</h2>
            <div class="about-text">
                My name is Brett Russell. I'm 27 years old, and my personality type is INTJ. I was born and raised in regional Victoria before moving to Melbourne in 2018.
            </div>
        </div>
        <div class="about-section">
            <h2>Why choose web development?</h2>
            <div class="about-text">
                From a very young age, I've always found great fulfilment in learning new things. In particular, I tend to find that the more complex a subject becomes while i'm learning about it, the more fascinating it becomes to me. This fascination drives me to seek out and understand further complexities within it. I'm completely new to web and software development, having no prior experience in any IT-related field. However, I thoroughly enjoy learning about the way in which coding languages are constructed and how they interconnect to create the apps, websites and software we use daily. I also believe that this industry is ever evolving, and I'm excited by the prospect of being a part of its growth or, at the very least gain an insider's perspective on the advancement of the IT industry as it moves forward. 
            </div>
        </div>
    </main>
```
I make use of the grid display in order to position my images beside my text:

```scss
@media screen and (min-width: $large) {

    .about-container {
        display: grid;
        grid-template-columns: 30% 70%;
        grid-template-rows: repeat(3, auto);
        background-color: $primary-background;

    }

    .home-photo {
        grid-column: 1;
        grid-row-start: 1;
        grid-row-end: 2; 
        margin-top: 60px;
        margin-right: 20px;
        margin-left: 20px;
        justify-self: center;
        border: 4px solid $tertiary-color;
        border-radius: 4px;
        height: 200px;
        width: 300px;
    }

    .gym-photo {
        grid-column: 1;
        grid-row-start: 2;
        grid-row-end: 4;
        align-self: center;  
        justify-self: center;
        border: 4px solid $tertiary-color;
        border-radius: 4px;
        height: 300px;
        width: 240px;
    }

    .about-section {
        grid-column: 2;
        display: flex;
        flex-direction: column;
        margin-bottom: 20px;
    }

    .about-text {
        margin-top: 10px;
        color: $secondary-color;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }

    h2 {
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        color: $primary-color;

    }
}
```
On smaller wireframes a flex diplay is utilised to position the images above the text.

![About-Small_Wireframe](./images/about-small-screenshot.png)

### Skills Section

The skills section contains a brief overview of my experience and a list of my skills, it also has a link to my resume.

![Skills-Page](./images/skills-screenshot.png)

I use an unordered list to make dot points and set a link to my resume document using a href:

```html
        <div class="skills-section">
            <h2>My Skills</h2>
            <ul>
                <li>Excellent professional communication</li>
                <li>A high level of customer service skills</li>
                <li>Ability in conflict resolution and de-escalation</li>
                <li>High attention to detail</li>
                <li>Very strong analytical and problem solving ability</li>
                <li>Competency in the use of HTML as well as CSS and SASS styling</li>
                <li>Competency with microsoft office including the use of excel spreadsheets</li>
                <li>Competency in using VS Code as well as linux based terminals</li>
                <li>Quick and solid mathematical skills</li>
                <li>The ability to work well both caloborating with a team or on solo projects</li>
                <li>High levels of professionalism and presentability</li>
            </ul>
        </div>
        <div class="skills-section">
            <div class="additional-text">
                If you would like any additional information, please feel free to download a copy of my resume below.
            </div>
            <a href="../documents/brett-russell-resume.pdf"
               class="download-link">Download Resume</a>           
        </div>
```

I used an inline block display and customised multiple parameters in order to style my link as a button:

```scss
    .download-link {
        display: inline-block;
        padding: 10px 20px;
        text-decoration: none;
        max-width: 30%;
        text-align: center;
        color: $secondary-color;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        font-weight: bold;
        background-color: $primary-color;
        border: 3px solid #333;
        border-radius: 6px;
        margin-left: 27%;
        transition: background-color 0.3s;

    }

    .download-link:hover {
        filter: brightness(75%);
    }
```

### Contact Section
This page is fairly simple, it contains a link to my email address.

![Contact_page](./images/contact-screenshot.png)

I use "mailto" in my href in order to start a draft to my email from the users mail page.

```html
     <main>
        <div class="contact-text">
            <p>If you would like any additional information, please feel free to get in touch with me using the link below. My email address, mobile number and links to my social media accounts can also be found at the bottom of each page.</p>
        </div><br>
        <a href="mailto:brett.russell2016@gmail.com" class="button">Email Me!</a>
    </main>
```

### Blog Section
The blog section contains images which act as anchor tags to their corresponding blog post within the page.

![Blog-Page](./images/blog-screenshot.png)

The anchor tag is made using the following javascript:

```java
         document.addEventListener('DOMContentLoaded', function () {
            const blogLinks = document.querySelectorAll('.blog-link');
    
            blogLinks.forEach(function (link) {
                link.addEventListener('click', function (event) {
                    event.preventDefault();
    
                    const targetId = link.getAttribute('data-target');
                    const targetElement = document.getElementById(targetId);
    
                    if (targetElement) {
                        targetElement.scrollIntoView();
                    }
                });
            });
        });
```

The html is comprised of 2 sections, the link section and the blog container:

```html
    <main class="link-section">
        <a href="#" class= "blog-link image1" data-target="blog-post-1">
            <img src="../images/Yuji.jpg" alt="Blog Post 1">
            <p>Blog Post 1</p>
        </a>
        <a href="#" class="blog-link image2" data-target="blog-post-2">
            <img src="../images/Gintoki.jpg" alt="Blog Post 2">
            <p>Blog Post 2</p>
        </a>
        <a href="#" class="blog-link image3" data-target="blog-post-3">
            <img src="../images/Midoriya.jpg" alt="Blog Post 3">
            <p>Blog Post 3</p>
        </a>
        <a href="#" class="blog-link image4" data-target="blog-post-4">
            <img src="../images/Tanjiro.jpg" alt="Blog Post 4">
            <p>Blog Post 4</p>
        </a>
        <a href="#" class="blog-link image5" data-target="blog-post-5">
            <img src="../images/Naruto.jpg" alt="Blog Post 5">
            <p>Blog Post 5</p>
        </a>
      </main>
          <main class="blog-container">
        <div class="blog-post" id="blog-post-1">
            <div class="blog-post-image">
                <img src="../images/Yuji.jpg" alt="Blog Post 1 Image">
            </div>
            <div class="blog-post-section">
                <h2>Blog Post 1</h2>
                <h4>Date published: 10/05/2023</h4>
                <div class="blog-text">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora autem labore alias eum officia consequuntur cum provident sed, recusandae voluptatum veniam cumque accusantium omnis, sit possimus porro optio expedita minus. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod facere libero explicabo consectetur laboriosam non? At, perspiciatis, consectetur quidem unde facilis aliquid cumque nulla accusamus expedita vitae labore. Temporibus, fuga! Lorem, ipsum dolor sit amet consectetur adipisicing elit. Minima ex ducimus dolorem repellendus unde et ratione temporibus doloremque, molestiae dolorum corrupti soluta a corporis labore voluptatum repudiandae quidem ad minus. Congratulations on finding my hidden post inside this placeholder text, you have a great eye for detail! Lorem ipsum dolor, sit amet consectetur adipisicing elit. Omnis, rerum! Molestiae fugiat quibusdam vero illum aspernatur officiis quae accusantium consectetur fugit obcaecati maxime, tempora voluptatibus odit nostrum qui ut sint.
                </div>
            </div>
        </div>
       </main>
 ```

 The styling is done uniquely for each wireframe in order to change how the links are positioned.

 Flex display for large:

 ```scss
 @media screen and (min-width: $large) {

        .link-section {
            display: flex;
            justify-content: space-around;
            align-items: center;
            min-width: 100vw;
   
            .blog-link {
                text-decoration: none;
                text-align: center;
                margin: 5px;
                border: 8px solid $tertiary-color;
                border-radius: 3px;
                background-color: $tertiary-color;

                .img {
                    height: auto;
                    margin: 0 2px;
                    width: 200px;
                    max-height: 200px;
                }

                p {
                    margin: 0;
                    font-family: Verdana, Geneva, Tahoma, sans-serif;
                    font-weight: bold;
                    color: $secondary-color;
                }
                &:hover {
                    filter: brightness(75%);
                }
            }
        }
    }
 ```

 ![Blog-Medium](./images/blog-medium-screenshot.png)

 Grid display for medium:

 ```scss
             .blog-link {
                text-decoration: none;
                border: 10px solid $tertiary-color;
                border-radius: 4px;
                max-width: 100%;
                background-color: $tertiary-color;
                justify

                img {
                    max-width: 80%;

                }
    
                p {
                    font-family: Verdana, Geneva, Tahoma, sans-serif;
                    font-weight: bold;
                    color: $secondary-color;
                    text-align: center;
                }
            }
        
        .image1 {
            grid-column-start: 1;
            grid-column-end: 2;
            grid-row: 1;
            justify-self: center;
        }

        .image2 {
            grid-column-start: 2;
            grid-column-end: 3;
            grid-row: 1;
            justify-self: center;
        }
    
 ```

 ![Blog-small](./images/blog-small-screenshot.png)

 And an alternate flex display for small:

```scss
         .link-section {
            display: flex;
            text-align: center;
            gap: 20px;
            margin-bottom: 350px;
            margin-top: 80px;

            .blog-link {
                text-decoration: none;
                border: 10px solid $tertiary-color;
                border-radius: 4px;
                margin-right: 43px;
                background-color: $tertiary-color;
    
                p {
                    font-family: Verdana, Geneva, Tahoma, sans-serif;
                    font-weight: bold;
                    color: $secondary-color;
                }

                img {
                    max-width: 90%;
                }
            }
        }
```

 ## Tech Stack
* HTML
* SCSS
* CSS
* JAVAscript
* Netlify
* Github



