const title = document.querySelector('.title');
const changeColor = document.querySelector('.changeColor');

title.style.color = 'red';

axios.get("http://127.0.0.1:5000/some/names")
.then(response => {console.log(response.data)})
.catch(error => console.error(error));

console.log("Hello World");