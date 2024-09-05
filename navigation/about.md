---
layout: page
title: About
permalink: /about/
---

Creator of Student 2025 - Nolan Yu 

AP Computer Science Principles
Period: 2 


---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me - Nolan Yu </title>
    <style>
        .flag-container {
            display: flex;
            align-items: center;
        }
        .flag {
            text-align: center;
            margin-right: 20px;
        }
        .flag img {
            width: 200px;
        }
    </style>
</head>
<body>
    <h1>About Me</h1>
    <p>👋 Hi, I'm <strong>Nolan Yu </strong>!</p>
    <ul>
        <li>🇮🇳 <strong>Nationality:</strong> Chinese</li>
        <li>🎂 <strong>Age:</strong> 15 years old</li>
        <li>🎓 <strong>Education:</strong> Sophomore at Del Norte High School</li>
        <li>🌍 <strong>Location:</strong> California, USA</li>
    </ul>
    <div class="flag-container">
        <div class="flag" id="californiaFlag">
            <p>California</p>
        </div>
        <div class="flag" id="chinaFlag">
            <p>China</p>
        </div>
    </div>


    <script>
        // JavaScript to dynamically insert image URLs
        var californiaFlagUrl = "https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg";
        var indiaFlagUrl = "https://en.wikipedia.org/wiki/Flag_of_China#/media/File:Flag_of_the_People's_Republic_of_China.svg


        document.getElementById('californiaFlag').innerHTML = '<img src="' + californiaFlagUrl + '" alt="California Flag"><p>California</p>';
        document.getElementById('ChinaFlag').innerHTML = '<img src="' + ChinaFlagUrl + '" alt="China Flag"><p>China</p>';
    </script>
</body>
</html>