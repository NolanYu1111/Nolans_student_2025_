---
{% include nav/home.html %}
layout: base
title: Nolan's Home 
description: Home Page
hide: true
---

Nolan's journey starts here - Kickin' Projects

<style>
  /* Change background color to light grey */
   {
      background-color: #f0f0f0; /* Light grey background */
  }

  /* Style for shortcut buttons */
  .button-container {
      text-align: center;
      margin: 20px 0;
  }
  
  .shortcut-btn {
      background-color: #4CAF50; /* Green button */
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      text-decoration: none;
      font-size: 16px;
      margin: 10px;
      display: inline-block;
      cursor: pointer;
  }
  
  .shortcut-btn:hover {
      background-color: #45a049; /* Darker green on hover */
  }
</style>

<!-- Add shortcut buttons -->
<div class="button-container">
  <a href="about/" class="shortcut-btn">About Me</a>
  <a href="blogs/" class="shortcut-btn">Blogs</a>
  <a href="README4YML.html/" class="shortcut-btn">Read Me</a>
</div>


<script src="https://utteranc.es/client.js"
        repo="[ENTER REPO HERE]"
        issue-term="pathname"
        theme="github-dark"
        crossorigin="anonymous"
        async>
</script>

Sprint 2 overviews of lessons

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programming Topics</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #2c2c2c;
            color: #fff;
            font-family: Arial, sans-serif;
        }

        .container {
            text-align: center;
        }

        .title {
            font-size: 2rem;
            margin-bottom: 20px;
            color: #4caf50;
        }

        .topics {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .topic {
            background-color: #333;
            padding: 15px;
            border: 1px solid #444;
            border-radius: 5px;
            position: relative;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .topic:hover {
            background-color: #555;
        }

        .description {
            display: none;
            position: absolute;
            bottom: 110%;
            left: 50%;
            transform: translateX(-50%);
            background-color: #222;
            padding: 10px;
            border: 1px solid #444;
            border-radius: 5px;
            white-space: nowrap;
        }

        .topic:hover .description {
            display: block;
        }

        .link-button {
            margin-top: 20px;
            background-color: #1e90ff;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }

        .link-button:hover {
            background-color: #0073e6;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="title">Programming Topics</div>
        <div class="topics">
            <div class="topic" onclick="window.location.href='https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/07/3.1homeworkhackpopcornhack_IPYNB_2_.html'">
                Unit 1 — Data Types
                <div class="description">Learn about various data types in programming.</div>
            </div>
            <div class="topic" onclick="window.location.href='https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/08/3.2.1homeworkandpopcornhacks_IPYNB_2_.html'">
                Unit 2 — Using Objects
                <div class="description">Understand how to work with objects.</div>
            </div>
            <div class="topic" onclick="window.location.href='https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/09/3-3-and-5homework_IPYNB_2_.html'">
                Unit 3 — Boolean Expressions
                <div class="description">Explore the fundamentals of Boolean logic.</div>
            </div>
            <div class="topic" onclick="window.location.href='https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/08/3.4homeworkhack_IPYNB_2_.html'">
                Unit 4 — Iteration
                <div class="description">Learn about loops and iterative processes.</div>
            </div>
            <div class="topic" onclick="window.location.href='https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/09/3-3-and-5homework_IPYNB_2_.html'">
                Unit 5 — Writing Classes
                <div class="description">Discover how to write and structure classes.</div>
            </div>
            <div class="topic" onclick="window.location.href='https://kush1434.github.io/portfolio_2025/csp/big-idea/p2/3-6'">
                Unit 6 — Arrays
                <div class="description">Work with arrays to store data efficiently.</div>
            </div>
            <div class="topic" onclick="window.location.href='https://kush1434.github.io/portfolio_2025/csp/big-idea/p2/3-7'">
                Unit 7 — ArrayLists
                <div class="description">Use ArrayLists for dynamic data storage.</div>
            </div>
            <div class="topic" onclick="window.location.href='https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/04/3.8homeworkpopcornhack_IPYNB_2_.html'">
                Unit 8 — 2D Arrays
                <div class="description">Learn about multi-dimensional data structures.</div>
            </div>
            <div class="topic" onclick="window.location.href='https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/04/3.10homeworkandpopcornhacks(1)_IPYNB_2_.html'">
                Unit 9 — Java Inheritance
                <div class="description">Understand the concept of inheritance in Java.</div>
            </div>
        </div>
        <a class="link-button" href="https://github.com/NolanYu1111/Nolans_student_2025_/issues/3">Go to My Issue</a>
    </div>
</body>
</html>

