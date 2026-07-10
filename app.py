import streamlit as st

st.set_page_config(
    page_title="Mere Banoge ❤️",
    layout="centered"
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body{
background:linear-gradient(135deg,#fff1f5,#ffd6e7);
text-align:center;
font-family:sans-serif;
}

.card{
background:white;
padding:30px;
border-radius:20px;
max-width:400px;
margin:auto;
margin-top:100px;
box-shadow:0 10px 30px rgba(0,0,0,0.1);
}

button{
padding:10px 20px;
border:none;
border-radius:20px;
background:#ff4f81;
color:white;
cursor:pointer;
}
</style>
</head>

<body>

<div class="card">
<h1>Mere Banoge? ❤️</h1>

<p>Tum meri life ki special person ho.</p>

<button onclick="alert('❤️ Thank You ❤️')">
Haan ❤️
</button>

</div>

</body>
</html>
"""

st.components.v1.html(html_code,height=700)
