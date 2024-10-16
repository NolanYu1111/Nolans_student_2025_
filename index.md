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


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dropdown Boxes</title>
    <style>
        body {
            background-color: #1e1e1e;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-gap: 20px;
            max-width: 900px;
        }

        .box {
            background-color: #222;
            color: #00bfff;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.3s;
            position: relative;
        }

        .box:hover {
            background-color: #333;
        }

        .box:hover .tooltip {
            visibility: visible;
            opacity: 1;
        }

        .tooltip {
            visibility: hidden;
            background-color: #555;
            color: #fff;
            text-align: center;
            padding: 5px 10px;
            border-radius: 5px;
            position: absolute;
            bottom: 120%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 1;
        }

        .tooltip::after {
            content: "";
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            border-width: 5px;
            border-style: solid;
            border-color: #555 transparent transparent transparent;
        }
    </style>
</head>
<body>
    <div class="grid-container">
        <div class="box" onclick="window.location.href='https://example.com/variables'">
            Variables
            <div class="tooltip">Variables store data values.</div>
        </div>
        <div class="box" onclick="window.location.href='https://example.com/data-abstraction'">
            Data Abstraction
            <div class="tooltip">Data Abstraction hides complexity by using data models.</div>
        </div>
        <div class="box" onclick="window.location.href='https://example.com/math-expressions'">
            Mathematical Expressions
            <div class="tooltip">Mathematical expressions involve calculations and operations.</div>
        </div>
        <div class="box" onclick="window.location.href='https://example.com/strings'">
            Strings
            <div class="tooltip">Strings represent text in programming.</div>
        </div>
        <div class="box" onclick="window.location.href='https://example.com/boolean-expressions'">
            Boolean Expressions
            <div class="tooltip">Boolean expressions evaluate to true or false.</div>
        </div>
        <div class="box" onclick="window.location.href='https://example.com/conditionals'">
            Conditionals
            <div class="tooltip">Conditionals control the flow of a program based on conditions.</div>
        </div>
        <div class="box" onclick="window.location.href='https://example.com/nested-conditionals'">
            Nested Conditionals
            <div class="tooltip">Nested conditionals are conditionals within conditionals.</div>
        </div>
        <div class="box" onclick="window.location.href='https://example.com/iteration'">
            Iteration
            <div class="tooltip">Iteration repeats actions or operations.</div>
        </div>
        <div class="box" onclick="window.location.href='https://example.com/list-operations'">
            List Operations
            <div class="tooltip">List operations involve manipulating lists or arrays.</div>
        </div>
    </div>
</body>
</html>




