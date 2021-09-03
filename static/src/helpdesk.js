.video-container {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 */
    height: 0;
    }

.video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    }

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-img-top {
  object-fit: cover;
  object-position: center;
  /* height: 650px;
  width: 540px; */
}

.jumbotron-fluid {
    background: url("../static/screenshots/back.jpg") center center / cover no-repeat;
}

body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 25px;
  background-image: url("../static/screenshots/jumbo.jpg");
  padding: 30px;
  line-height: 1.6;
}

h1 {
  /* text-align: center; */
  margin-bottom: 30px;
  border-bottom: 1px #ccc solid;
}

h3 {
  margin-top: 20px;
}

input[type="text"] {
  border: 1px #ccc solid;
  width: 300px;
  padding: 4px;
  height: 35px;
  margin-top: 20px;
}

.card {
  margin: 20px 0;
  border: #ccc 1px solid;
  padding: 20px
  object-fit: cover;
}
