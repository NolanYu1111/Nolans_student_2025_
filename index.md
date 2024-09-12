---
layout: base
title: Nolan's Home 
description: Home Page
hide: true
---

Nolan's journey starts here - Kickin' Projects

# Welcome to My Soccer-Themed Page!

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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soccer Game</title>
    <style>
        canvas {
            background-color: #00a651; /* Green field */
            display: block;
            margin: 0 auto;
            border: 5px solid #fff; /* White boundary */
        }
        body {
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <h1>Simple Soccer Game</h1>
    <canvas id="gameCanvas" width="600" height="400"></canvas>

    <script src="soccer.js"></script>

</body>
</html>

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const player = {
    x: 50,
    y: canvas.height / 2 - 25,
    width: 20,
    height: 40,
    speed: 5,
    dx: 0,
    dy: 0,
    color: 'blue'
};

const ball = {
    x: canvas.width / 2 - 10,
    y: canvas.height / 2 - 10,
    radius: 10,
    dx: 3,
    dy: 3,
    color: 'white'
};

const goal = {
    x: canvas.width - 40,
    y: canvas.height / 2 - 50,
    width: 20,
    height: 100,
    color: 'yellow'
};

function drawPlayer() {
    ctx.fillStyle = player.color;
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

function drawBall() {
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
    ctx.fillStyle = ball.color;
    ctx.fill();
    ctx.closePath();
}

function drawGoal() {
    ctx.fillStyle = goal.color;
    ctx.fillRect(goal.x, goal.y, goal.width, goal.height);
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function movePlayer() {
    player.x += player.dx;
    player.y += player.dy;

    // Boundary collision detection
    if (player.x < 0) player.x = 0;
    if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;
    if (player.y < 0) player.y = 0;
    if (player.y + player.height > canvas.height) player.y = canvas.height - player.height;
}

function moveBall() {
    ball.x += ball.dx;
    ball.y += ball.dy;

    // Ball boundary collision
    if (ball.x - ball.radius < 0 || ball.x + ball.radius > canvas.width) {
        ball.dx *= -1;
    }
    if (ball.y - ball.radius < 0 || ball.y + ball.radius > canvas.height) {
        ball.dy *= -1;
    }

    // Ball-player collision
    if (ball.x - ball.radius < player.x + player.width &&
        ball.x + ball.radius > player.x &&
        ball.y - ball.radius < player.y + player.height &&
        ball.y + ball.radius > player.y) {
        ball.dx *= -1;
        ball.dy *= -1;
    }

    // Ball-goal collision (win condition)
    if (ball.x + ball.radius > goal.x && ball.y > goal.y && ball.y < goal.y + goal.height) {
        alert("Goal! You Win!");
        resetGame();
    }
}

function resetGame() {
    player.x = 50;
    player.y = canvas.height / 2 - 25;
    ball.x = canvas.width / 2 - 10;
    ball.y = canvas.height / 2 - 10;
    ball.dx = 3;
    ball.dy = 3;
}

function update() {
    movePlayer();
    moveBall();
    clearCanvas();
    drawPlayer();
    drawBall();
    drawGoal();
    requestAnimationFrame(update);
}

function keyDown(e) {
    if (e.key === 'ArrowRight') {
        player.dx = player.speed;
    } else if (e.key === 'ArrowLeft') {
        player.dx = -player.speed;
    } else if (e.key === 'ArrowUp') {
        player.dy = -player.speed;
    } else if (e.key === 'ArrowDown') {
        player.dy = player.speed;
    }
}

function keyUp(e) {
    if (
        e.key === 'ArrowRight' ||
        e.key === 'ArrowLeft' ||
        e.key === 'ArrowUp' ||
        e.key === 'ArrowDown'
    ) {
        player.dx = 0;
        player.dy = 0;
    }
}

document.addEventListener('keydown', keyDown);
document.addEventListener('keyup', keyUp);

update();










