```scss
@import "../defaults/colors";
@import "../defaults/breakpoints";

@media screen and (min-width: $large) {

    .image-section {
        display: flex;
        justify-content: space-around;
        align-items: center;
    
        .blog-link {
            text-decoration: none;
            text-align: center;
            margin: 10px;
            border: 8px solid $tertiary-color;
            border-radius: 3px;
            background-color: $tertiary-color;

        
            .img {
                max-width: 100%;
                height: auto;
                margin: 0 2px;
            }

            p {
                margin: 0;
                font-family: Verdana, Geneva, Tahoma, sans-serif;
                font-weight: bold;
                color: $secondary-color;
            }
        }
    }

    .blog-section {
        display: grid;
        grid-template-columns: 30% 70%;
        grid-template-rows: repeat(5, 15%);
        gap: 1px;

        .blog-post-image {

            img{
                max-width: 100%;
                height: auto;
                display: block;
                width: 100%;
            }
        }

            #blog-image-1 {
                grid-column-start: 1;
                grid-row-start: 1;
            }

            #blog-image-2 {
                grid-column-start: 1;
                grid-row-start: 3;
            }

            #blog-image-3 {
                grid-column-start: 1;
                grid-row-start: 5;
            }

            #blog-image-4 {
                grid-column-start: 1;
                grid-row-start: 7;
            }

            #blog-image-5 {
                grid-column-start: 1;
                grid-row-start: 9;
            }
        }
    
        
    

    .grid-container {
        display: grid;
        grid-template-columns: 30% 70%;
        grid-template-rows: repeat(3, auto);
        background-color: $primary-background;
    }
    li {
        color: $secondary-color;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        font-weight: bold;
        margin-bottom: 3px;
    }
    .additional-text {
        color: $secondary-color;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        text-align: center;
        word-wrap: break-word;
        max-width: 70%;
        margin-top: 50px;
        margin-bottom: 20px;
        margin-left: 10%;
    }
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
    main {
        display: grid;
        grid-template-columns: 30% 70%;
        grid-template-rows: 25% 25% 25% 25%;


        .custom-text {
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

@media screen and (max-width: $large) {
    main {
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
        margin-bottom: 40px;

        li {
            color: $secondary-color;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            margin-bottom: 10px;
        }

        .additional-text {
            color: $secondary-color;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            text-align: center;
            word-wrap: break-word;
            max-width: 70%;
            margin-top: 50px;
            margin-bottom: 20px;
            margin-left: 14%;
        }
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
            margin-left: 1%;
            transition: background-color 0.3s;
    
        }
    
        .download-link:hover {
            filter: brightness(75%);
        }

        .about-section {
            text-align: center;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            word-wrap: break-word;
            max-width: 75%;
            h2 {
                color: $primary-color;
            }
            .about-text {
                color: $secondary-color
            }

        }

        .custom-text {
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