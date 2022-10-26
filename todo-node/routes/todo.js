const express = require("express");
const todoRouter = express.Router();
const TodoModel = require('../models/todo')
const { check } = require('express-validator/check')

todoRouter.get("/", async (req, res) => {
    try {
        const todos = await TodoModel.find();
        res.json(todos);
    } catch (err) {
        res.status(400);
    }
});

todoRouter.post("/", [
    check('task').isLength({ min: 5 }),
    check('status').isLength({ min: 6 }),
], async (req, res) => {
    var data = req.body;
    data.createdAt = new Date()
    if (!!data.note) data.note = ""
    try {
        const newTask = await TodoModel.create(data);
        var result = newTask;
        delete result['_id'];
        res.status(201).json(result)
    }
    catch (err) {
        res.sendStatus(400)
    }
});

todoRouter.get("/:id", async (req, res) => {
    try {
        const id = req.params.id;
        const task = await TodoModel.findById(id);
        if (!task) res.status(404);
        res.json(task);
    }
    catch (err) {
        res.status(404).end()
    }
})

todoRouter.put("/:id", async (req, res) => {
    const id = req.params.id;
    const data = req.body;
    await TodoModel.findByIdAndUpdate(id, data, (err, newTask) => {
        if (err || !data) {
            res.status(400).json({
                message: "Something went wrong, please try again later.",
            });
        } else {

            res.status(200).json({
                action: 'update',
                data: newTask
            });
        }
    });
})

todoRouter.delete("/:id", async (req, res) => {
    const id = req.params.id;
    await TodoModel.findByIdAndDelete(id, (err, data) => {
        if (err || !data) {
            res.status(400).json({
                message: "Something went wrong, please try again later.",
            });
        } else {
            res.status(200).json({
                action: 'delete'
            });
        }
    });
})

module.exports = todoRouter;