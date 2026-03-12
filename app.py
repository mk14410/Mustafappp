<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>3D Heart</title>

<style>
body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:#111;
    perspective:1000px;
}

.heart{
    width:120px;
    height:120px;
    position:relative;
    transform-style:preserve-3d;
    animation:rotate 6s linear infinite, beat 1s infinite;
}

.heart::before,
.heart::after{
    content:"";
    position:absolute;
    width:120px;
    height:120px;
    background:red;
    border-radius:50%;
}

.heart::before{
    left:-60px;
}

.heart::after{
    top:-60px;
}

.square{
    position:absolute;
    width:120px;
    height:120px;
    background:red;
    transform:rotate(45deg);
}

@keyframes rotate{
    0%{ transform:rotateY(0deg) rotateX(0deg); }
    100%{ transform:rotateY(360deg) rotateX(360deg); }
}

@keyframes beat{
    0%,100%{ scale:1; }
    50%{ scale:1.2; }
}
</style>
</head>

<body>

<div class="heart">
<div class="square"></div>
</div>

</body>
</html>
