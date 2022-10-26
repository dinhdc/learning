# Express overview

Express is a Node.js Web Framework. Node.js is an amazing tool for building networking services and applications. Express builds on top of its features to provide easy to use functionality that satisfy the needs of the Web Server use case.

## Installation

You can install Express into any project with `npm`:

`npm install express --save`

or use `yarn`:

`yarn add express`

## Parameters

| Property       | Description                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| .app           | holds a reference to the Express app object                                                                        |
| .baseUrl       | the base path on which the app responds                                                                            |
| .body          | contains the data submitted in the request body (must be `parsed` and populated manually before you can access it) |
| .cookies       | contains the cookies sent by the request (needs the `cookie-parser` middleware responds                            |
| .hostname      | the server hostname                                                                                                |
| .ip            | the server IP                                                                                                      |
| .method        | the HTTP method used                                                                                               |
| .params        | the route named parameters                                                                                         |
| .path          | the URL path                                                                                                       |
| .protocol      | the request protocol                                                                                               |
| .query         | an object containing all the query strings used in the request                                                     |
| .secure        | true if the request is secure (uses HTTPS)                                                                         |
| .signedCookies | contains the signed cookies sent by the request (needs the `cookie-parser` middleware)                             |
| .xhr           | true if the request is an `XMLHttpRequest`                                                                         |

## Manage Cookies

```javascript
Response.cookie();
```

### Cookie Examples

Example:

```javascript
res.cookie("username", "Flavio");
```

This method accepts a third parameter which contains various options:

```javascript
res.cookie("username", "Flavio", {
  domain: ".flaviocopes.com",
  path: "/administrator",
  secure: true,
});
res.cookie("username", "Flavio", {
  expires: new Date(Date.now() + 900000),
  httpOnly: true,
});
```

### Some values on options cookie

| Value    | Description                                                                        |
| -------- | ---------------------------------------------------------------------------------- |
| domain   | the `cookie domain name`                                                           |
| expires  | set the `cookie expiration date`. If missing, or 0, the cookie is a session cookie |
| httpOnly | set the cookie to be accessible only by the web server.                            |
| maxAge   | set the expiry time relative to the current time, expressed in milliseconds        |
| path     | the cookie path. Defaults to /                                                     |
| secure   | Marks the cookie HTTPS only                                                        |
| signed   | set the cookie to be signed                                                        |
| sameSite | Value of SameSite                                                                  |

## Change any HTTP header value of a response

You can change any HTTP header value using `Response.set()`:

```javascript
res.set("Content-Type", "text/html");
```

There is a shortcut for the Content-Type header however:

```javascript
res.type(".html");
// => 'text/html'
res.type("html");
// => 'text/html'
res.type("json");
// => 'application/json'
res.type("application/json");
// => 'application/json'
res.type("png");
// => image/png:
```

## Routing

### Named parameters

What if we want to listen for custom requests, maybe we want to create a service that accepts a string, and returns that uppercase, and we don't want the parameter to be sent as a query string, but part of the URL. We use named parameters:

```javascript
app.get("/uppercase/:theValue", (req, res) =>
  res.send(req.params.theValue.toUpperCase())
);
```

If we send a request to `/uppercase/test` , we'll get `TEST` in the body of the response.

You can use multiple named parameters in the same URL, and they will all be stored in `req.params`.

## CORS

If you are using Node.js and Express as a framework, use the CORS middleware package.

### Allow only specific origins

You need to configure the server to only allow one origin to serve, and block all the others.

Using the same `cors` Node library, here's how you would do it:

```javascript
const cors = require("cors");
const corsOptions = {
  origin: "https://yourdomain.com",
};
app.get("/products/:id", cors(corsOptions), (req, res, next) => {
  //...
});
```

You can serve more as well:

```javascript
const whitelist = ["http://example1.com", "http://example2.com"];
const corsOptions = {
  origin: function (origin, callback) {
    if (whitelist.indexOf(origin) !== -1) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
};
```

### Allow OPTIONS on just one resource

```javascript
var express = require("express");
var cors = require("cors");
var app = express();

//allow OPTIONS on just one resource
app.options("/the/resource/you/request", cors());
```

### Allow OPTIONS on all resource

```javascript
var express = require("express");
var cors = require("cors");
var app = express();

//allow OPTIONS on all resource
app.options("*", cors());
```

## Templating

In this example and my project, i will use Pug engine

To use Pug we must first install it:

```javascript
npm install pug // using npm
yarn add pug // using yarn
```

and when initializing the Express app, we need to set it:

```javascript
const express = require("express");
const app = express();
app.set("view engine", "pug");
```

We can now start writing our templates in `.pug` files.

Create an about view:

```javascript
app.get("/about", (req, res) => {
  res.render("about");
});
```

and the template in `views/about.pug` file:

```pug
p Hello from About Page
```

This template will create a `p` tag with the content `Hello from About Page` .

You can interpolate a variable using

```javascript
app.get("/about", (req, res) => {
  res.render("about", { name: "About" });
});
```

```pug
p Hello from #{name}
```

## Middleware

A middleware is a function that hooks into the routing process, and performs some operation at some point, depending on what it want to do.

It's added to the execution stack like this:

```javascript
app.use((req, res, next) => {
  /* */
});
```

This is similar to defining a route, but in addition to the Request and Response objects instances, we also have a reference to the next middleware function, which we assign to the `variable next`.

One example is `cookie-parser`, which is used `req.cookies` object. You install it using to parse the cookies into the `npm install cookie-parser` and you can use it like this:

```javascript
const express = require("express");
const app = express();
const cookieParser = require("cookie-parser");
app.get("/", (req, res) => res.send("Hello World!"));
app.use(cookieParser());
app.listen(3000, () => console.log("Server ready"));
```

You can also set a middleware function to run for specific routes only, not for all, by using it as
the second parameter of the route definition:

```javascript
const myMiddleware = (req, res, next) => {
  /* ... */
  next();
};
app.get("/", myMiddleware, (req, res) => res.send("Hello World!"));
```

If you need to store data that's generated in a middleware to pass it down to subsequent middleware functions, or to the request handler, you can use the `Request.locals` object. It will attach that data to the current request:

```javascript
req.locals.name = "Example";
```

## Serving static files

How to serve static assets directly from a folder in Express?

It's common to have images, CSS and more in a `public` subfolder, and expose them to the root level:

```javascript
const express = require("express");
const app = express();
app.use(express.static("public"));
/* ... */
app.listen(3000, () => console.log("Server ready"));
```

## Send files

Express provides a handy method to transfer a file as attachment: `Response.download()`

The `Response.download()` method allows you to send a file attached to the request, and the browser instead of showing it in the page, it will save it to disk.

```javascript
app.get("/", (req, res) => res.download("./file.pdf"));
```

In the context of an app:

```javascript
const express = require("express");
const app = express();
app.get("/", (req, res) => res.download("./file.pdf"));
app.listen(3000, () => console.log("Server ready"));
```

You can set the file to be sent with a custom filename:

```javascript
res.download("./file.pdf", "user-facing-filename.pdf");
```

This method provides a callback function which you can use to execute code once the file has
been sent:

```javascript
res.download("./file.pdf", "user-facing-filename.pdf", (err) => {
  if (err) {
    //handle error
    return;
  } else {
    //do something
  }
});
```
