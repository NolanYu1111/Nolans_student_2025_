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


<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  /* Main container: 3x3 Grid */
  .main-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 20px;
  }
  /* Each menu */
  .menu {
    width: 300px;
    border-radius: 8px;
    background-color: #333;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    overflow: hidden;
    transition: transform 0.2s;
  }
  .menu:hover {
    transform: scale(1.05);
  }
  .menu-title {
    background-color: #444;
    padding: 15px;
    cursor: pointer;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    transition: background-color 0.3s;
  }
  .menu-title:hover {
    background-color: #555;
  }
  .menu-content {
    max-height: 0;
    overflow: hidden;
    background-color: #222;
    transition: max-height 0.5s ease-out;
    padding: 0 15px;
  }
  .menu-content.open {
    max-height: 200px;
    padding: 15px;
  }
</style>

<div class="main-container">
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent1')">Box 1</div>
    <div class="menu-content" id="menuContent1">
      <p>Description for Box 1</p>
    </div>
  </div>
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent2')">Box 2</div>
    <div class="menu-content" id="menuContent2">
      <p>Description for Box 2</p>
    </div>
  </div>
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent3')">Box 3</div>
    <div class="menu-content" id="menuContent3">
      <p>Description for Box 3</p>
    </div>
  </div>
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent4')">Box 4</div>
    <div class="menu-content" id="menuContent4">
      <p>Description for Box 4</p>
    </div>
  </div>
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent5')">Box 5</div>
    <div class="menu-content" id="menuContent5">
      <p>Description for Box 5</p>
    </div>
  </div>
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent6')">Box 6</div>
    <div class="menu-content" id="menuContent6">
      <p>Description for Box 6</p>
    </div>
  </div>
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent7')">Box 7</div>
    <div class="menu-content" id="menuContent7">
      <p>Description for Box 7</p>
    </div>
  </div>
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent8')">Box 8</div>
    <div class="menu-content" id="menuContent8">
      <p>Description for Box 8</p>
    </div>
  </div>
  <div class="menu">
    <div class="menu-title" onclick="toggleMenu('menuContent9')">Box 9</div>
    <div class="menu-content" id="menuContent9">
      <p>Description for Box 9</p>
    </div>
  </div>
</div>

<script>
  function toggleMenu(contentId) {
    const content = document.getElementById(contentId);
    content.classList.toggle('open');
  }
</script>



