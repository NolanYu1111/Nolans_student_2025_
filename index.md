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

### <!DOCTYPE html>
<html>
<head>
    <style>
        /* Style for the table */
        #summaryTable {
            border-collapse: collapse;
            width: 60%;
            border: 2px solid lightgreen;
            display: inline-block;
        }
        #summaryTable th, #summaryTable td {
            border: 1px solid lightgreen;
            text-align: center;
            padding: 0;
            height: 100px;
            width: 200px;
            background-color: #e0ffe0; /* Light green background */
            color: #0000ff; /* Blue text */
        }
        #summaryTable a {
            color: #0000ff; /* Blue text for links */
            text-decoration: none;
        }
        .summary {
            display: none;
            position: absolute;
            background-color: #c0e0c0; /* Lighter green background for summary */
            color: #0000ff; /* Blue text */
            padding: 10px;
            border: 1px solid lightgreen;
            width: 200px;
            z-index: 10;
            font-size: 18px;
        }
    </style>
</head>
<body>

    <!-- Project title with hyperlink -->
    <h1><a href="http://127.0.0.1:4100/Nolans_student_2025_/2024/10/16/Sprint2FinalHacks_IPYNB_2_.html" style="color: blue; text-decoration: none;">Sprint 2 Final Project</a></h1>

    <table id="summaryTable">
        <tr>
            <td><a href="https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/07/3.1homeworkhackpopcornhack_IPYNB_2_.html" onmouseover="showSummary(this, 'Variables are used to store data values. They can be changed during program execution.')" onmouseout="hideSummary()">Variables</a></td>
            <td><a href="https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/08/3.2.1homeworkandpopcornhacks_IPYNB_2_.html" onmouseover="showSummary(this, 'Data abstraction is a concept that hides complex realities while exposing only the necessary parts. It simplifies programming by reducing complexity.')" onmouseout="hideSummary()">Data Abstraction</a></td>
            <td><a href="https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/09/3-3-and-5homework_IPYNB_2_.html" onmouseover="showSummary(this, 'Mathematical expressions are combinations of numbers, variables, and operators. They are used to perform calculations and operations.')" onmouseout="hideSummary()">Mathematical Expressions</a></td>
        </tr>
        <tr>
            <td><a href="https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/08/3.4homeworkhack_IPYNB_2_.html" onmouseover="showSummary(this, 'Strings are sequences of characters used to represent text.')" onmouseout="hideSummary()">Strings</a></td>
            <td><a href="https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/09/3-3-and-5homework_IPYNB_2_.html" onmouseover="showSummary(this, 'Boolean expressions evaluate to true or false. They are fundamental in decision-making processes in programming.')" onmouseout="hideSummary()">Boolean Expressions</a></td>
            <td><a href="https://kush1434.github.io/portfolio_2025/csp/big-idea/p2/3-6" onmouseover="showSummary(this, 'Conditionals are statements that execute different actions based on whether a specified condition is true or false. They are essential for controlling the flow of a program.')" onmouseout="hideSummary()">Conditionals</a></td>
        </tr>
        <tr>
            <td><a href="https://kush1434.github.io/portfolio_2025/csp/big-idea/p2/3-7" onmouseover="showSummary(this, 'Nested conditionals are conditionals placed inside another conditional. They allow for more complex decision-making in programming.')" onmouseout="hideSummary()">Nested Conditionals</a></td>
            <td><a href="https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/04/3.8homeworkpopcornhack_IPYNB_2_.html" onmouseover="showSummary(this, 'Iteration refers to the process of repeating a set of instructions a specified number of times or until a certain condition is met. In this lesson, we used both while loops and for loops.')" onmouseout="hideSummary()">Iteration</a></td>
            <td><a href="https://nolanyu1111.github.io/Nolans_student_2025_/2024/10/04/3.10homeworkandpopcornhacks(1)_IPYNB_2_.html" onmouseover="showSummary(this, 'List operations involve manipulating data stored in lists. Common operations include adding, removing, and accessing elements in a list.')" onmouseout="hideSummary()">List Operations</a></td>
        </tr>
    </table>

    <div class="summary" id="summaryBox"></div>

    <!-- Button to link directly to the GitHub issue -->
    <button onclick="window.location.href='https://github.com/NolanYu1111/Nolans_student_2025_/issues/3'" style="margin-top: 20px; padding: 10px;">Link to my Issue</button>

    <!-- Button to link to the final overview -->
    <button onclick="window.location.href='http://127.0.0.1:4100/Nolans_student_2025_/2024/10/16/finaloverview_IPYNB_2_.html'" style="margin-left: 10px; padding: 10px;">Final Overview</button>

    <script>
        function showSummary(element, text) {
            const summaryBox = document.getElementById('summaryBox');
            const rect = element.getBoundingClientRect();
            summaryBox.innerHTML = text;
            summaryBox.style.display = 'block';
            summaryBox.style.left = `${rect.right + 10}px`;
            summaryBox.style.top = `${rect.top + window.scrollY}px`;
        }

        function hideSummary() {
            const summaryBox = document.getElementById('summaryBox');
            summaryBox.style.display = 'none';
        }
    </script>

</body>
</html>


