const express = require('express');
const app = express();
var mongoose = require('mongoose');
require('dotenv').config();

/* json-parser */
app.use(express.json()) // using for Content-Type: application/json
app.use(express.urlencoded({ extended: false })) // using for Content-Type: application/x-www-form-urlencoded

// environment variables
const port = process.env.PORT || 4200;
const url = process.env.URI;

// import routes
const todoRouter = require('./routes/todo');

// connect to MongoDB
mongoose.connect(url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => console.log('connected to MongoDB'))
    .catch(err => console.log(err));

app.get('/', (req, res) => {
    res.send('hello')
});

app.use("/todos", todoRouter);

app.listen(port, () => console.log(`listening on http://localhost:${port}`));
