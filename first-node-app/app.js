const { application, request } = require('express')
const express = require('express')
const app = express()
app.set('view engine', 'pug')
// set up middleware
/* json-parser */
app.use(express.json()) // using for Content-Type: application/json
app.use(express.urlencoded({ extended: false })) // using for Content-Type: application/x-www-form-urlencoded

app.get('/', (req, res) => {
    console.log(req.query); // ?query1=value1&query2=value2....
    console.log(req.headers); // get header of request
    res.send('Hello World!')
})

app.post('/', (req, res) => {
    const data = req.body // get data from request post
    console.log("data~~", data);
    // Use end() to send an empty response
    // res.end();

    // send status
    // res.sendStatus(200)

    // send json response
    res.json(data);
})

// parameters in routing request
app.get('/hi/:name', (req, res) => {
    res.send(`Hello ${req.params.name.toUpperCase()}`)
})

// about page
app.get("/about", (req, res) => {
    res.render("about", { name: "About" });
});

app.listen(3000, () => console.log('Server ready'))